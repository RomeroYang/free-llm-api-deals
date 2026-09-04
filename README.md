# Free LLM API Deals

A source-linked, machine-readable collection of free tiers, trial credits, limited-time offers, and price cuts across LLM API providers. This is a community resource first: use `deals.json` directly, cite it, or build your own view on top of it.

The data is published by [AI Plug](https://aiplug.work/en/deals), a self-hosted multi-provider LLM API relay. The [Chinese deals page](https://aiplug.work/deals) shows the same collection. Every entry carries a `source_url` and a `verified_at` date, so each claim can be checked against its source and its freshness is explicit.

**Dataset generated:** `2026-09-04`<br>
**Status cutoff:** `2026-09-04` (derived from `generated_at`)<br>
**Entries:** 43 live, 0 expired

## Live deals

Dated offers are ordered by the soonest expiry, followed by offers with no announced end date.

| Offer | Provider | Kind | Limits / credit | Expires | Coding-ready | Verified | Evidence |
|---|---|---|---|---|:---:|---|---|
| **GPT 5.6 Sol 50% off**<br><sub>OpenCode Zen offers GPT 5.6 Sol at 50% off through September 18, 2026.</sub> | OpenCode Zen | `price-cut` | — | 2026-09-18 | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **Dots Studio Dots3-Note Preview (free)**<br><sub>Free MoE, 512K context, ends September 30, 2026.</sub> | OpenRouter | `time-limited` | — | 2026-09-30 | No | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **Cerebras $5 trial credit**<br><sub>New accounts receive $5 in trial credit, usable across all Cerebras models.</sub> | Cerebras Inference | `trial-credit` | $5.0 credit | No announced end date | No | 2026-08-31 | [Source](<https://www.cerebras.ai/pricing>) |
| **Cloudflare Workers AI free tier**<br><sub>10,000 neurons per day, about 300 RPM for text models.</sub> | Cloudflare Workers AI | `free-tier` | 300 RPM | No announced end date | No | 2026-08-31 | [Source](<https://developers.cloudflare.com/workers-ai/platform/pricing/>) |
| **Cohere Evaluation Key free tier**<br><sub>Free evaluation key: 20 RPM, with 1,000 requests per month shared across the account.</sub> | Cohere | `free-tier` | 20 RPM | No announced end date | No | 2026-08-31 | [Source](<https://docs.cohere.com/docs/rate-limits>) |
| **Fireworks Serverless Inference $1 trial credit**<br><sub>New accounts receive $1 in trial credit, usable across all serverless models.</sub> | Fireworks AI | `trial-credit` | $1.0 credit | No announced end date | No | 2026-08-31 | [Source](<https://fireworks.ai/pricing>) |
| **Gemini 3 Flash Preview (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal, preview track (source: ai.google.dev/gemini-api/docs/pricing). Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 5 RPM, 20 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview>) |
| **Gemini 3.1 Flash-Lite (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal, cheaper than 3.5-Lite. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 15 RPM, 500 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite>) |
| **Gemini 3.5 Flash (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal, supports function calling and structured output. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 5 RPM, 20 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash>) |
| **Gemini 3.5 Flash-Lite (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal, cheapest in the 3.x family. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 15 RPM, 500 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite>) |
| **Gemini 3.6 Flash (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal, supports function calling and structured output. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 5 RPM, 20 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/pricing>) |
| **Gemini 3.7 Flash (free tier)**<br><sub>Google AI Studio free tier, 1M input / 65K output, multimodal (text/image/video/audio/PDF), supports function calling, structured output and thinking; grounding is not offered on the free tier. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific). Heavily queued on the free tier: 27-148s per request when measured.</sub> | Google AI Studio (Gemini API) | `free-tier` | 5 RPM, 20 RPD | No announced end date | Yes | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash>) |
| **Gemini Embedding 2 (free)**<br><sub>Fully multimodal embedding model, available on the free tier. Rate limits measured by us on 2026-09-02 (Google no longer publishes free-tier limits; quota is per project, not per key, and RPD resets at midnight Pacific).</sub> | Google AI Studio (Gemini API) | `free-tier` | 100 RPM, 1000 RPD | No announced end date | No | 2026-09-02 | [Source](<https://ai.google.dev/gemini-api/docs/pricing>) |
| **Groq Compound (free tier)**<br><sub>Groq free tier: 30 RPM / 250 RPD / 70K TPM.</sub> | Groq | `free-tier` | 30 RPM, 250 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://console.groq.com/docs/rate-limits>) |
| **GPT OSS 120B (free tier)**<br><sub>Groq free tier: 30 RPM / 1K RPD / 8K TPM / 200K TPD.</sub> | Groq | `free-tier` | 30 RPM, 1000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://console.groq.com/docs/rate-limits>) |
| **GPT OSS 20B (free tier)**<br><sub>Groq free tier: 30 RPM / 1K RPD / 8K TPM / 200K TPD.</sub> | Groq | `free-tier` | 30 RPM, 1000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://console.groq.com/docs/rate-limits>) |
| **Qwen 3 27B (free tier)**<br><sub>Groq free tier: 30 RPM / 1K RPD / 8K TPM / 200K TPD.</sub> | Groq | `free-tier` | 30 RPM, 1000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://console.groq.com/docs/rate-limits>) |
| **Whisper Large v3 (free tier)**<br><sub>Groq free tier: 20 RPM / 2K RPD, 7.2K audio seconds per minute.</sub> | Groq | `free-tier` | 20 RPM, 2000 RPD | No announced end date | No | 2026-08-31 | [Source](<https://console.groq.com/docs/rate-limits>) |
| **Hugging Face Inference Providers monthly free credits**<br><sub>Free users receive $0.10 monthly; PRO users receive $2.00 monthly, usable across all providers.</sub> | Hugging Face Inference Providers | `free-tier` | $0.1 credit | No announced end date | No | 2026-08-31 | [Source](<https://huggingface.co/docs/api-inference/pricing>) |
| **DeepSeek V4 Pro (free endpoint)**<br><sub>Direct NVIDIA free endpoint, 1M-token context, MoE, positioned for coding and agentic use.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/deepseek-ai/deepseek-v4-pro-0813>) |
| **OpenAI GPT OSS 120B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, OpenAI open weights, supports tool calling.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/openai/gpt-oss-120b>) |
| **OpenAI GPT OSS 20B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, compact OpenAI open-weights model, supports tool calling.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/openai/gpt-oss-20b>) |
| **Kimi K3 (free endpoint)**<br><sub>Direct NVIDIA free endpoint, ~2.8T hybrid KDA+MLA MoE, multimodal, long-horizon coding and agentic tool use.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/moonshotai/kimi-k3>) |
| **Meta Muse-Glimmer 30B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, multimodal reasoning, supports tool calling.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/meta/muse-glimmer-30b>) |
| **minimax-M3 (free endpoint)**<br><sub>Direct NVIDIA free endpoint, multimodal MoE VLM (source: build.nvidia.com model list)</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/minimaxai/minimax-m3>) |
| **NVIDIA Nemotron 3 Embed 1B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, 1B-parameter embedding model for RAG.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | No | 2026-08-31 | [Source](<https://build.nvidia.com/nvidia/nemotron-3-embed-1b>) |
| **NVIDIA Nemotron 3 Ultra 550B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, 1M-token context, 550B MoE (55B active), hybrid Mamba+Attention.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/nvidia/nemotron-3-ultra-550b-a55b>) |
| **NVIDIA Nemotron 3 Nano Omni 30B (free endpoint)**<br><sub>Direct NVIDIA free endpoint, omni-modal (image/video/speech/text), MoE reasoning.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | No | 2026-08-31 | [Source](<https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning>) |
| **Poolside Laguna XS 2.1 (free endpoint)**<br><sub>Direct NVIDIA free endpoint, 33B MoE, positioned for agentic coding.</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | Yes | 2026-08-31 | [Source](<https://build.nvidia.com/poolside/laguna-xs-2.1>) |
| **NVIDIA Riva Translate 4B Instruct v2 (free endpoint)**<br><sub>Direct NVIDIA free endpoint, translation across 37 languages (source: build.nvidia.com model list)</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | No | 2026-08-31 | [Source](<https://build.nvidia.com/nvidia/riva-translate-4b-instruct-v2>) |
| **StepFun Step 3.7 Flash (free endpoint)**<br><sub>Direct NVIDIA free endpoint, sparse MoE multimodal reasoning (source: build.nvidia.com model list)</sub> | NVIDIA (integrate.api.nvidia.com) | `free-tier` | 40 RPM, 10000 RPD | No announced end date | No | 2026-08-31 | [Source](<https://build.nvidia.com/stepfun-ai/step-3.7-flash>) |
| **Big Pickle (free for a limited time)**<br><sub>OpenCode Zen stealth model, free for a limited time; data may be used for training.</sub> | OpenCode Zen | `time-limited` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **Hy3 (free for a limited time)**<br><sub>Free on OpenCode Zen for a limited time.</sub> | OpenCode Zen | `time-limited` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **MiMo-V2.5 (free for a limited time)**<br><sub>Free on OpenCode Zen for a limited time.</sub> | OpenCode Zen | `time-limited` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **Nemotron 3 Ultra Free (free)**<br><sub>NVIDIA free endpoint for testing only; do not submit sensitive data.</sub> | OpenCode Zen (NVIDIA 端点) | `time-limited` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **Nemotron 3.5 Lightning Free (free)**<br><sub>NVIDIA free endpoint for testing only; do not submit sensitive data.</sub> | OpenCode Zen (NVIDIA 端点) | `time-limited` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://opencode.ai/docs/zen>) |
| **Ling 3.0 Flash Fin (free)**<br><sub>Always free on OpenRouter, finance-focused MoE, up to 32,768 output tokens per request.</sub> | OpenRouter | `always-free` | — | No announced end date | No | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **LiquidAI LFM2.5-2.6B (free)**<br><sub>Free compact reasoning model suited to agents and RAG.</sub> | OpenRouter | `always-free` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **NVIDIA Nemotron 3.5 Lightning (free)**<br><sub>Always free on OpenRouter, 1M context, 3B active / 30B total MoE.</sub> | OpenRouter | `always-free` | — | No announced end date | No | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **Poolside Laguna S 2.1 (free)**<br><sub>Free coding agent model, 70.2% on Terminal-Bench 2.1.</sub> | OpenRouter | `always-free` | — | No announced end date | Yes | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **Thinking Machines Inkling (free)**<br><sub>Free large multimodal reasoning model, 1M context, 41B active / 975B total.</sub> | OpenRouter | `always-free` | — | No announced end date | No | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **Thinking Machines Inkling Small (free)**<br><sub>Free multimodal MoE, 1M context, 12B active / 276B total.</sub> | OpenRouter | `always-free` | — | No announced end date | No | 2026-08-31 | [Source](<https://openrouter.ai/api/v1/models>) |
| **Ternary Bonsai 27B (free)**<br><sub>Together AI's only free serverless model, by Prism ML, 262K context; no function calling or structured output, dynamic limits (see 429 headers)</sub> | Together AI | `always-free` | — | No announced end date | No | 2026-08-31 | [Source](<https://docs.together.ai/docs/serverless-models>) |

## Expired offers

Expired entries remain available as a record of previously verified offers.

No entries had expired by this snapshot's status cutoff.

## Data contract

`deals.json` contains a top-level generation timestamp and an `entries` array. Each entry identifies the offer and provider, classifies it as one of five closed `kind` values, records practical limits and compatibility, and links the evidence used for verification. See [SCHEMA.md](SCHEMA.md) for the field-by-field contract.

| Field | Type | Meaning |
|---|---|---|
| `generated_at` | ISO 8601 timestamp | Dataset snapshot time. |
| `entries` | array | Deal entry objects. |
| `id` | string | Stable entry and deduplication key. |
| `title`, `summary` | string | Chinese display text. |
| `title_en`, `summary_en` | string, optional | English display text; fall back to the Chinese field when absent. |
| `model`, `provider` | string | Model/service identifier and provider. |
| `kind` | closed string enum | Offer classification. |
| `rpm`, `rpd` | integer or null | Published request limits. |
| `credit_usd` | number or null | Credit value in US dollars. |
| `card_needed` | boolean | Whether a payment card is required. |
| `openai_compatible` | boolean | Whether an OpenAI-compatible interface is available. |
| `coding` | boolean | Maintainer-reviewed coding-agent usability. |
| `verified_at` | ISO 8601 date | Date the evidence was checked. |
| `expires_at` | ISO 8601 date or null | Published offer end date, if any. |
| `source_url` | URL string | Evidence for the entry. |
| `tags` | array of strings | Search and filtering labels. |
| `verify_needle` | string, optional | Exact source text used for mechanical verification. |

The five offer kinds are `always-free`, `free-tier`, `time-limited`, `trial-credit`, and `price-cut`. `card_needed` is an independent field, not an offer kind. `coding` is a maintained usability judgement based on coding suitability, tool calling, context size, and usable rate limits.

## Refresh and reuse

The upstream AI Plug deals dataset is refreshed daily. This repository is a publishable snapshot of that dataset; `generated_at` and each entry's `verified_at` make the snapshot's age visible.

Regenerate this README after updating the JSON:

```console
$ python3 scripts/render-readme.py
$ python3 scripts/render-readme.py --check
```

The data is licensed under [CC BY 4.0](LICENSE). Attribution should link to [AI Plug's English deals page](https://aiplug.work/en/deals).

<!-- This file is generated by scripts/render-readme.py. -->
