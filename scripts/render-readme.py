#!/usr/bin/env python3
"""Render README.md from deals.json using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "deals.json"
README_PATH = ROOT / "README.md"


def markdown_cell(value: Any) -> str:
    """Make a value safe inside a Markdown table cell."""
    if value is None:
        return "—"
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    return text.replace("|", "\\|").replace("\n", "<br>")


def parse_date(value: str, field: str) -> date:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be an ISO 8601 date: {value!r}") from exc


def dataset_date(generated_at: str) -> date:
    try:
        return datetime.fromisoformat(generated_at.replace("Z", "+00:00")).date()
    except (AttributeError, ValueError) as exc:
        raise ValueError(
            f"generated_at must be an ISO 8601 timestamp: {generated_at!r}"
        ) from exc


def english_text(entry: dict[str, Any], field: str) -> str:
    english = entry.get(f"{field}_en")
    return str(english if english else entry.get(field, ""))


def limits(entry: dict[str, Any]) -> str:
    parts: list[str] = []
    if entry.get("rpm") is not None:
        parts.append(f'{entry["rpm"]} RPM')
    if entry.get("rpd") is not None:
        parts.append(f'{entry["rpd"]} RPD')
    if entry.get("credit_usd") is not None:
        parts.append(f'${entry["credit_usd"]} credit')
    return ", ".join(parts) if parts else "—"


def source_link(entry: dict[str, Any]) -> str:
    url = str(entry.get("source_url", ""))
    safe_url = (
        url.replace(">", "%3E")
        .replace("|", "%7C")
        .replace("\n", "")
        .replace("\r", "")
    )
    return f"[Source](<{safe_url}>)"


def live_row(entry: dict[str, Any]) -> str:
    title = markdown_cell(english_text(entry, "title"))
    summary = markdown_cell(english_text(entry, "summary"))
    offer = f"**{title}**<br><sub>{summary}</sub>" if summary else f"**{title}**"
    expires = markdown_cell(entry.get("expires_at") or "No announced end date")
    return " | ".join(
        [
            f"| {offer}",
            markdown_cell(entry.get("provider")),
            f'`{markdown_cell(entry.get("kind"))}`',
            markdown_cell(limits(entry)),
            expires,
            "Yes" if entry.get("coding") else "No",
            markdown_cell(entry.get("verified_at")),
            f"{source_link(entry)} |",
        ]
    )


def expired_row(entry: dict[str, Any]) -> str:
    title = markdown_cell(english_text(entry, "title"))
    return " | ".join(
        [
            f"| **{title}**",
            markdown_cell(entry.get("provider")),
            f'`{markdown_cell(entry.get("kind"))}`',
            markdown_cell(entry.get("expires_at")),
            f"{source_link(entry)} |",
        ]
    )


def render(data: dict[str, Any]) -> str:
    generated_at = data.get("generated_at")
    entries = data.get("entries")
    if not isinstance(generated_at, str) or not isinstance(entries, list):
        raise ValueError("deals.json must contain generated_at and an entries array")

    as_of = dataset_date(generated_at)

    def expiry(entry: dict[str, Any]) -> date | None:
        value = entry.get("expires_at")
        return parse_date(value, f'{entry.get("id", "<unknown>")}.expires_at') if value else None

    live: list[dict[str, Any]] = []
    expired: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("every entries item must be an object")
        end = expiry(entry)
        (expired if end is not None and end < as_of else live).append(entry)

    live.sort(
        key=lambda entry: (
            expiry(entry) is None,
            expiry(entry) or date.max,
            str(entry.get("provider", "")).casefold(),
            str(entry.get("id", "")),
        )
    )
    expired.sort(
        key=lambda entry: (
            -(expiry(entry) or date.min).toordinal(),
            str(entry.get("provider", "")).casefold(),
            str(entry.get("id", "")),
        )
    )

    lines = [
        "# Free LLM API Deals",
        "",
        "A source-linked, machine-readable collection of free tiers, trial credits, "
        "limited-time offers, and price cuts across LLM API providers. This is a "
        "community resource first: use `deals.json` directly, cite it, or build your "
        "own view on top of it.",
        "",
        "The data is published by [AI Plug](https://aiplug.work/en/deals), a self-hosted "
        "multi-provider LLM API relay. The [Chinese deals page](https://aiplug.work/deals) "
        "shows the same collection. Every entry carries a `source_url` and a "
        "`verified_at` date, so each claim can be checked against its source and its "
        "freshness is explicit.",
        "",
        f"**Dataset generated:** `{generated_at}`<br>",
        f"**Status cutoff:** `{as_of.isoformat()}` (derived from `generated_at`)<br>",
        f"**Entries:** {len(live)} live, {len(expired)} expired",
        "",
        "## Live deals",
        "",
        "Dated offers are ordered by the soonest expiry, followed by offers with no "
        "announced end date.",
        "",
        "| Offer | Provider | Kind | Limits / credit | Expires | Coding-ready | Verified | Evidence |",
        "|---|---|---|---|---|:---:|---|---|",
    ]
    lines.extend(live_row(entry) for entry in live)
    if not live:
        lines.append("| _No live entries in this snapshot._ | — | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## Expired offers",
            "",
            "Expired entries remain available as a record of previously verified offers.",
            "",
        ]
    )
    if expired:
        lines.extend(
            [
                "| Offer | Provider | Kind | Expired | Evidence |",
                "|---|---|---|---|---|",
                *(expired_row(entry) for entry in expired),
            ]
        )
    else:
        lines.append("No entries had expired by this snapshot's status cutoff.")

    lines.extend(
        [
            "",
            "## Data contract",
            "",
            "`deals.json` contains a top-level generation timestamp and an `entries` "
            "array. Each entry identifies the offer and provider, classifies it as one "
            "of five closed `kind` values, records practical limits and compatibility, "
            "and links the evidence used for verification. See [SCHEMA.md](SCHEMA.md) "
            "for the field-by-field contract.",
            "",
            "| Field | Type | Meaning |",
            "|---|---|---|",
            "| `generated_at` | ISO 8601 timestamp | Dataset snapshot time. |",
            "| `entries` | array | Deal entry objects. |",
            "| `id` | string | Stable entry and deduplication key. |",
            "| `title`, `summary` | string | Chinese display text. |",
            "| `title_en`, `summary_en` | string, optional | English display text; fall back to the Chinese field when absent. |",
            "| `model`, `provider` | string | Model/service identifier and provider. |",
            "| `kind` | closed string enum | Offer classification. |",
            "| `rpm`, `rpd` | integer or null | Published request limits. |",
            "| `credit_usd` | number or null | Credit value in US dollars. |",
            "| `card_needed` | boolean | Whether a payment card is required. |",
            "| `openai_compatible` | boolean | Whether an OpenAI-compatible interface is available. |",
            "| `coding` | boolean | Maintainer-reviewed coding-agent usability. |",
            "| `verified_at` | ISO 8601 date | Date the evidence was checked. |",
            "| `expires_at` | ISO 8601 date or null | Published offer end date, if any. |",
            "| `source_url` | URL string | Evidence for the entry. |",
            "| `tags` | array of strings | Search and filtering labels. |",
            "| `verify_needle` | string, optional | Exact source text used for mechanical verification. |",
            "",
            "The five offer kinds are `always-free`, `free-tier`, `time-limited`, "
            "`trial-credit`, and `price-cut`. `card_needed` is an independent field, "
            "not an offer kind. `coding` is a maintained usability judgement based on "
            "coding suitability, tool calling, context size, and usable rate limits.",
            "",
            "## Refresh and reuse",
            "",
            "The upstream AI Plug deals dataset is refreshed daily. This repository is "
            "a publishable snapshot of that dataset; `generated_at` and each entry's "
            "`verified_at` make the snapshot's age visible.",
            "",
            "Regenerate this README after updating the JSON:",
            "",
            "```console",
            "$ python3 scripts/render-readme.py",
            "$ python3 scripts/render-readme.py --check",
            "```",
            "",
            "The data is licensed under [CC BY 4.0](LICENSE). Attribution should link "
            "to [AI Plug's English deals page](https://aiplug.work/en/deals).",
            "",
            "<!-- This file is generated by scripts/render-readme.py. -->",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero when README.md does not match deals.json",
    )
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = render(data)

    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else None
        if current != rendered:
            print(
                "README.md is stale; run scripts/render-readme.py",
                file=sys.stderr,
            )
            return 1
        print("README.md is up to date")
        return 0

    README_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {README_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
