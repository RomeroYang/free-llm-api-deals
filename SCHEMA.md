# `deals.json` schema

This document describes the public data contract used by the AI Plug deals dataset. JSON `null` means that a value is not published or does not apply; it must not be interpreted as zero.

## Top-level object

| Field | Type | Contract |
|---|---|---|
| `generated_at` | string | ISO 8601 UTC timestamp for the dataset snapshot. Consumers can derive the snapshot date from this value. |
| `entries` | array | Deal entry objects. Entry identity is the `id` field. |

## Entry fields

| Field | Type | Contract |
|---|---|---|
| `id` | string | Stable, source-oriented identifier and deduplication key. |
| `title` | string | Chinese display title. |
| `title_en` | string, optional | English display title. Consumers should fall back to `title` when absent or empty. |
| `summary` | string | Chinese factual summary of the offer and its material limits. |
| `summary_en` | string, optional | English factual summary. Consumers should fall back to `summary` when absent or empty. |
| `model` | string | Provider model identifier, a list of model identifiers, or a service-level label when an offer covers multiple models. |
| `provider` | string | Provider or endpoint through which the offer is available. |
| `kind` | string enum | Offer classification. It must be one of the five values defined below. |
| `rpm` | integer or `null` | Published requests-per-minute limit, when a single applicable value is available. |
| `rpd` | integer or `null` | Published requests-per-day limit, when a single applicable value is available. |
| `credit_usd` | number or `null` | One-time or included credit denominated in US dollars, when applicable. |
| `card_needed` | boolean | Whether obtaining the offer requires a payment card. This is independent of `kind`. |
| `openai_compatible` | boolean | Whether the offer is available through an OpenAI-compatible API interface. |
| `coding` | boolean | Maintainer-reviewed coding-agent usability. `true` requires a coding or suitable general-purpose model/service, tool or function calling, at least an 8K context window, and practically usable free-tier rate limits. It is not generated automatically. |
| `verified_at` | string | ISO 8601 calendar date on which the entry's evidence was last checked. |
| `expires_at` | string or `null` | ISO 8601 calendar date for a published offer end date. `null` means no end date was published; it does not guarantee permanence. |
| `source_url` | string | URL of the evidence supporting the entry. Every entry must provide one. |
| `tags` | array of strings | Search and filtering labels. Tags are descriptive and are not a substitute for `kind`. |
| `verify_needle` | string, optional | Exact source text used by the verifier when a human-readable source name differs from `model`. If present, the verifier checks this value instead of inferring a lookup string from the model identifier. |

Additional operational fields may appear on a live pipeline copy (for example, a stale marker produced by verification). Consumers should ignore fields they do not recognize.

## Closed `kind` values

`kind` is a closed set. A claim needs source evidence before it can be assigned one of these values.

| Value | Meaning |
|---|---|
| `always-free` | A specified model or endpoint has both input and output unit prices of `$0`, with no published end date. |
| `free-tier` | A recurring, capped zero-cost allowance within a paid service. RPM, RPD, or TPM limits may apply. A `$0` spend tier that only changes throughput while calls remain fully priced is not a free tier. |
| `time-limited` | An offer explicitly described as temporarily free. `expires_at` is required when the provider publishes an end date and may be `null` otherwise. |
| `trial-credit` | A one-time trial allowance for a new account. |
| `price-cut` | A source-supported price reduction below an explicit reference price. |

`card-required` is deliberately not a `kind`; use `card_needed` for that fact.

## Expiry convention

An entry is expired when its non-null `expires_at` date is earlier than the dataset date derived from `generated_at`. An entry whose expiry equals the dataset date remains in the live set for that date. Offers without a published expiry sort after dated live offers.
