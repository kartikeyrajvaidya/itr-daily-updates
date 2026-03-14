# Tax AI Board Architecture

**Project:** ITR Stats  
**Document version:** v1.0  
**Date:** 2026-03-13  
**Status:** Draft for review

---

## 1. Goal

Build an AI-powered "Tax + Delay Board" for `itrstats.in` that can:

1. Answer Indian tax questions with source-backed responses.
2. Answer delay/processing questions using ITR Stats data (`data/daily.csv`) and official portal stats.
3. Give actionable next steps ("what to do next") without collecting sensitive filing credentials.

---

## 2. Scope (v1)

### In scope

1. Form selection and eligibility guidance (ITR-1/2/3/4/5/6/7).
2. Tax explainer Q&A across supported topics (ITR forms, deadlines, regime basics, common compliance paths).
3. Delay analytics from your dataset:
   - e-verified vs processed gap
   - recent processing velocity
   - queue expansion/contraction signals
4. Citation-backed answers with confidence labels.
5. Feedback loop for answer quality.

### Out of scope (v1)

1. Filing returns on user’s behalf.
2. Storing PAN, password, OTP, bank details, AIS files, Form 16 uploads.
3. Personalized legal/tax advisory equivalent to CA engagement.
4. Guaranteed individual refund-date prediction.

---

## 3. Product Behavior

### 3.1 Answer contract shown to user

Every response should include:

1. **Direct answer**
2. **Why / logic**
3. **Sources**
4. **Confidence** (`High`, `Medium`, `Low`)
5. **Next actions**
6. **Disclaimer** for legal/tax-risk contexts

### 3.2 Intent buckets

The router classifies each prompt into one bucket:

1. `itr_form_selection`
2. `itr_eligibility_rule`
3. `deadline_and_penalty`
4. `refund_delay_analytics`
5. `portal_how_to`
6. `calculator_guidance`
7. `out_of_scope`
8. `needs_clarification`

---

## 4. Recommended Architecture

This repo is static (GitHub Pages), so AI must run on a separate backend.

### 4.1 Deployment shape

1. **Frontend:** Existing static site (`itrstats.in`) + chat widget JS.
2. **Backend API:** `api.itrstats.in` (serverless, stateless compute).
3. **Data stores:** relational DB + vector index + cache + object storage.
4. **Ingestion jobs:** scheduled sync for rules/sources/metrics.

### 4.2 Suggested stack (pragmatic)

1. **Backend runtime:** TypeScript on Cloudflare Workers (or Vercel Functions; same API contract).
2. **Relational DB:** Postgres (Neon/Supabase) for sessions, answers, metrics, feedback.
3. **Vector search:** `pgvector` in same Postgres for simplicity.
4. **Cache/rate limit:** Redis/Upstash.
5. **Blob storage:** R2/S3 for source snapshots.
6. **LLM provider:** OpenAI responses/chat endpoint via backend only.

### 4.3 High-level data flow

```text
Browser Widget (itrstats.in)
  -> POST /v1/assistant/query
     -> Guardrails + Intent Classifier
        -> Tool Router
           -> Deterministic Rules Engine (for ITR logic)
           -> Delay Analytics Engine (for daily.csv-derived metrics)
           -> Retrieval Engine (official docs + internal content)
        -> Answer Composer (citations + confidence + actions)
  <- JSON response (or SSE stream)
```

---

## 5. Backend Modules

## 5.1 API layer

Responsibilities:

1. Request validation.
2. Authentication/session handling.
3. Rate limiting.
4. Response serialization.
5. Trace ID assignment.

## 5.2 Guardrail engine

Responsibilities:

1. Block unsafe prompts (credential theft, impersonation, evasion).
2. Redact sensitive user text before persistence.
3. Enforce disclaimer requirements on high-risk intents.
4. Route uncertain cases to `needs_clarification`.

## 5.3 Orchestrator

Responsibilities:

1. Classify intent.
2. Invoke correct tools.
3. Merge tool outputs.
4. Create final answer object.

## 5.4 Tool: deterministic tax rules

Responsibilities:

1. Evaluate structured tax logic (e.g., ITR form selection).
2. Return machine-readable reasoning path.
3. Return deterministic confidence (usually high when inputs complete).

## 5.5 Tool: delay analytics

Responsibilities:

1. Query `metrics_daily`.
2. Compute standardized derived values:
   - `gap = eVerifiedReturns - TotalProcessedRefund`
   - `processing_ratio = TotalProcessedRefund / eVerifiedReturns`
   - rolling deltas (7d, 14d)
3. Return narrative-ready summary + numeric payload.

## 5.6 Tool: retrieval

Responsibilities:

1. Semantic retrieval from curated corpus.
2. Rank by source authority + recency + relevance.
3. Return citations with chunk IDs and URLs.

## 5.7 Answer composer

Responsibilities:

1. Build concise answer from tool results.
2. Attach citations and confidence.
3. Add next actions and disclaimer.

---

## 6. API Contracts (Public)

All endpoints are versioned under `/v1`.

## 6.1 POST `/v1/assistant/query`

Primary synchronous endpoint.

### Request JSON

```json
{
  "message": "Can I file ITR-1 if I have salary and freelance income?",
  "session_id": "ses_01JX...",
  "context": {
    "page_url": "https://itrstats.in/calculator/itr-form/",
    "page_type": "calculator",
    "locale": "en-IN"
  },
  "user_profile": {
    "residency_hint": "resident_individual"
  }
}
```

### Response JSON

```json
{
  "request_id": "req_01JX...",
  "session_id": "ses_01JX...",
  "intent": "itr_form_selection",
  "status": "answered",
  "answer": {
    "text_markdown": "No, in this case you generally file ITR-3 or ITR-4...",
    "confidence": "high",
    "confidence_score": 0.92,
    "disclaimer": "This is informational guidance, not professional tax advice."
  },
  "next_actions": [
    "Check presumptive eligibility under 44ADA/44AD",
    "Use ITR form selector and verify edge conditions"
  ],
  "citations": [
    {
      "source_id": "src_foportal_itr1_help_2026",
      "title": "Return applicable - ITR-1",
      "url": "https://www.incometax.gov.in/...",
      "authority": "official",
      "published_or_updated_at": "2026-03-01"
    }
  ],
  "tool_trace": {
    "rules_engine": "used",
    "delay_engine": "not_used",
    "retrieval": "used"
  },
  "usage": {
    "input_tokens": 615,
    "output_tokens": 196,
    "latency_ms": 1240
  }
}
```

### Error response

```json
{
  "request_id": "req_01JX...",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "message is required",
    "details": []
  }
}
```

## 6.2 POST `/v1/assistant/stream`

Server-sent events endpoint for streaming answers.

### Request

Same body as `/query`.

### SSE events

1. `event: meta` -> request/session IDs
2. `event: token` -> incremental text
3. `event: citation` -> structured citation object
4. `event: done` -> final metadata + confidence
5. `event: error` -> error payload

## 6.3 POST `/v1/assistant/feedback`

Capture quality signal.

### Request JSON

```json
{
  "request_id": "req_01JX...",
  "session_id": "ses_01JX...",
  "rating": "thumbs_down",
  "reason": "Incorrect ITR classification",
  "comment": "HUF case routed wrong."
}
```

### Response JSON

```json
{
  "status": "ok"
}
```

## 6.4 GET `/v1/sources/{source_id}`

Return source metadata used in a response.

### Response JSON

```json
{
  "source_id": "src_foportal_itr1_help_2026",
  "title": "Return applicable - ITR-1",
  "url": "https://www.incometax.gov.in/...",
  "authority": "official",
  "snapshot_url": "https://storage.../src_foportal_itr1_help_2026.html",
  "last_ingested_at": "2026-03-12T09:30:00Z"
}
```

## 6.5 GET `/v1/health`

Liveness/readiness endpoint.

### Response JSON

```json
{
  "status": "ok",
  "version": "v1.0.0",
  "time": "2026-03-13T10:00:00Z"
}
```

---

## 7. API Contracts (Internal Tool Interfaces)

## 7.1 `rules_engine.evaluate_form`

### Input

```json
{
  "taxpayer_type": "resident_individual",
  "has_business_income": true,
  "business_mode": "presumptive",
  "flags": {
    "director": false,
    "unlisted_shares": false,
    "foreign_assets": false,
    "multi_house_property": false,
    "income_over_50l": false,
    "agri_over_5000": false
  }
}
```

### Output

```json
{
  "recommended_form": "ITR-4",
  "confidence": "high",
  "reasoning_steps": [
    "Resident individual with business income",
    "Presumptive scheme selected",
    "No disqualifier flags triggered"
  ],
  "rule_version": "itr_rules_2026_03_v2"
}
```

## 7.2 `delay_engine.get_metrics`

### Input

```json
{
  "as_of_date": "2026-03-12",
  "window_days": 14
}
```

### Output

```json
{
  "as_of_date": "2026-03-12",
  "everified_returns": 87644016,
  "processed_returns": 84826116,
  "gap_proxy": 2817900,
  "processing_ratio": 0.9678,
  "delta_everified_14d": 153783,
  "delta_processed_14d": 118605,
  "clearance_ratio_14d": 0.771
}
```

## 7.3 `retrieval_engine.search`

### Input

```json
{
  "query": "Can RNOR file ITR-4?",
  "top_k": 6,
  "filters": {
    "authority": ["official", "internal_verified"]
  }
}
```

### Output

```json
{
  "results": [
    {
      "chunk_id": "chk_01JX...",
      "source_id": "src_foportal_itr4_faq_2026",
      "score": 0.91,
      "text": "...",
      "url": "https://www.incometax.gov.in/..."
    }
  ]
}
```

---

## 8. Data Model (Backend)

Recommended relational schema:

## 8.1 `sessions`

1. `id` (PK, text)
2. `created_at` (timestamptz)
3. `last_seen_at` (timestamptz)
4. `locale` (text)
5. `page_url` (text)
6. `ip_hash` (text, nullable)
7. `ua_hash` (text, nullable)

## 8.2 `requests`

1. `id` (PK, text)
2. `session_id` (FK)
3. `message_raw` (text)
4. `message_redacted` (text)
5. `intent` (text)
6. `status` (text)
7. `latency_ms` (int)
8. `input_tokens` (int)
9. `output_tokens` (int)
10. `created_at` (timestamptz)

## 8.3 `answers`

1. `request_id` (PK/FK)
2. `answer_markdown` (text)
3. `confidence_label` (text)
4. `confidence_score` (numeric)
5. `disclaimer` (text)
6. `tool_trace_json` (jsonb)
7. `created_at` (timestamptz)

## 8.4 `citations`

1. `id` (PK)
2. `request_id` (FK)
3. `source_id` (FK)
4. `url` (text)
5. `authority` (text)
6. `score` (numeric)

## 8.5 `feedback`

1. `id` (PK)
2. `request_id` (FK)
3. `session_id` (FK)
4. `rating` (text)
5. `reason` (text)
6. `comment` (text)
7. `created_at` (timestamptz)

## 8.6 `metrics_daily`

Loaded from your existing data pipeline.

1. `date` (PK, date)
2. `last_updated` (date)
3. `indv_reg_users` (bigint)
4. `aadhar_linked_pan` (bigint)
5. `everified_returns` (bigint)
6. `processed_returns` (bigint)
7. `delta_indv_reg_users` (int)
8. `delta_aadhar_linked_pan` (int)
9. `delta_everified_returns` (int)
10. `delta_processed_returns` (int)
11. `source` (text)

## 8.7 `sources`

1. `id` (PK)
2. `title` (text)
3. `url` (text)
4. `authority` (text)
5. `effective_from` (date, nullable)
6. `effective_to` (date, nullable)
7. `checksum` (text)
8. `last_ingested_at` (timestamptz)
9. `snapshot_uri` (text)

## 8.8 `source_chunks`

1. `id` (PK)
2. `source_id` (FK)
3. `chunk_index` (int)
4. `text` (text)
5. `embedding` (vector)
6. `token_count` (int)

## 8.9 `rule_sets`

1. `id` (PK)
2. `name` (text)
3. `version` (text)
4. `rules_json` (jsonb)
5. `is_active` (bool)
6. `published_at` (timestamptz)

---

## 9. Security, Privacy, and Compliance

## 9.1 Data minimization

1. Do not request PAN, Aadhaar, password, OTP, bank account number.
2. Auto-redact patterns before persistence.
3. Keep session IDs opaque and non-PII.

## 9.2 Rate limiting and abuse controls

1. Anonymous cap: e.g., `15 requests / 5 min / IP`.
2. Progressive challenge (Turnstile/Captcha) after threshold.
3. Hard blocks for prompt abuse patterns.

## 9.3 Legal/quality guardrails

1. Mark all responses as informational, not professional advice.
2. Always cite source for rule-based answers.
3. Refuse definitive legal conclusions on ambiguous facts; ask clarifying questions.

## 9.4 Retention policy (suggested)

1. Raw prompts: 30 days.
2. Aggregated analytics: 12 months.
3. Feedback/comments: 12 months.
4. Manual deletion capability by session ID.

---

## 10. Reliability and Observability

## 10.1 SLO targets

1. API availability: `99.5%` monthly.
2. P95 latency: `< 2.5s` sync endpoint.
3. Citation coverage: `>= 95%` for tax-rule intents.
4. Deterministic tool usage for form-selection intents: `100%`.

## 10.2 Metrics to track

1. Requests per intent bucket.
2. Error rate by code.
3. Hallucination proxy (thumbs-down + “incorrect” reason).
4. Avg confidence by intent.
5. Cost per answered request.

## 10.3 Logging payload fields

1. `request_id`
2. `session_id`
3. `intent`
4. `tools_used`
5. `latency_ms`
6. `model`
7. `token_in`, `token_out`
8. `error_code`

---

## 11. Ingestion and Knowledge Update Pipeline

## 11.1 Source categories

1. `official`: Income Tax portal pages, notifications, statutory references.
2. `internal_verified`: your calculators/specs/data pages verified by your rules.
3. `secondary`: external explainers (lower rank).

## 11.2 Pipeline steps

1. Fetch source content.
2. Normalize HTML/PDF to clean text.
3. Chunk with metadata.
4. Embed + index.
5. Validate checksums for update detection.
6. Activate source version.

## 11.3 Cadence

1. Delay metrics sync: daily (after your `data/daily.csv` update).
2. Tax rules sync: weekly + on-notification release.
3. Full corpus re-embed: monthly or on model upgrade.

---

## 12. Frontend Integration Contract

## 12.1 Widget bootstrap

Add a lightweight script to pages:

```html
<script defer src="/scripts/tax-ai-widget.js"></script>
```

The widget calls:

1. `POST https://api.itrstats.in/v1/assistant/query`
2. `POST https://api.itrstats.in/v1/assistant/feedback`

## 12.2 UI states

1. `idle`
2. `typing`
3. `streaming`
4. `answered`
5. `needs_clarification`
6. `error`

## 12.3 CORS policy

Allow origins:

1. `https://itrstats.in`
2. `https://www.itrstats.in`
3. `http://localhost:*` (dev only)

---

## 13. Backend Repository Layout (proposed)

```text
backend/
  src/
    index.ts
    routes/
      health.ts
      assistant.query.ts
      assistant.stream.ts
      assistant.feedback.ts
      sources.get.ts
    core/
      orchestrator.ts
      intent-classifier.ts
      guardrails.ts
      answer-composer.ts
    tools/
      rules-engine.ts
      delay-engine.ts
      retrieval-engine.ts
    data/
      repos/
        sessions.repo.ts
        requests.repo.ts
        metrics.repo.ts
        sources.repo.ts
      migrations/
    schemas/
      api.schemas.ts
      db.schemas.ts
    observability/
      logger.ts
      tracing.ts
  tests/
    contract/
    integration/
    regression/
```

---

## 14. Versioning and Compatibility

1. Public API path versioning: `/v1`.
2. Non-breaking additions only within v1.
3. Breaking changes require `/v2`.
4. Rule-set version emitted in every response.

---

## 15. Rollout Plan

## Phase 0: Spec and contracts (this doc)

Deliverables:

1. Finalized API contracts.
2. Approved intent taxonomy.
3. Approved risk policy.

## Phase 1: Deterministic MVP (no broad RAG answers yet)

Deliverables:

1. `itr_form_selection` and `refund_delay_analytics` intents.
2. Rules engine + delay engine.
3. Basic chat UI.
4. Feedback capture.

## Phase 2: Hybrid AI

Deliverables:

1. Retrieval engine + citation rendering.
2. Confidence scoring and clarification loop.
3. Expanded intent coverage.

## Phase 3: Quality hardening

Deliverables:

1. Regression suite of known tricky tax scenarios.
2. Prompt/version management.
3. Evaluation dashboard and SLI/SLO tracking.

---

## 16. Known Risks and Mitigations

1. **Regulatory rule drift**
   - Mitigation: rule-set versioning + scheduled rule review + source validity windows.
2. **Hallucinated legal answers**
   - Mitigation: deterministic-first routing + mandatory citations + low-confidence fallback.
3. **Abuse/spam**
   - Mitigation: IP rate limits + challenge gate + moderation.
4. **Ambiguous user inputs**
   - Mitigation: `needs_clarification` workflow with structured follow-up questions.

---

## 17. Open Decisions Needed From You

1. Preferred runtime: Cloudflare Workers vs Vercel Functions.
2. Preferred DB: Supabase/Neon Postgres vs managed alternative.
3. LLM provider and model budget targets.
4. Data retention window (30/60/90 days).
5. Languages for v1 (`English only` vs `English + Hindi`).

---

## 18. Appendix A: Standard Error Codes

1. `VALIDATION_ERROR` (400)
2. `UNAUTHORIZED` (401)
3. `FORBIDDEN` (403)
4. `NOT_FOUND` (404)
5. `RATE_LIMITED` (429)
6. `POLICY_BLOCKED` (422)
7. `UPSTREAM_MODEL_ERROR` (503)
8. `INTERNAL_ERROR` (500)

---

## 19. Appendix B: Delay Metric Definitions (v1)

From existing fields:

1. `everified_returns` -> `eVerifiedReturns`
2. `processed_returns` -> `TotalProcessedRefund` (portal key naming)
3. `gap_proxy = everified_returns - processed_returns`
4. `processing_ratio = processed_returns / everified_returns`
5. `clearance_ratio_Nd = sum(delta_processed_Nd) / sum(delta_everified_Nd)`

Important: present these as **portal-derived operational indicators**, not statutory SLA commitments.

---

## 20. Appendix C: Example Clarification Workflow

If user asks: "I have salary + side hustle + mutual funds; which form?"

Clarifying questions:

1. Are you using presumptive taxation (`44AD/44ADA/44AE`)?
2. Any foreign assets/income?
3. Total income above Rs 50 lakh?
4. Any brought-forward capital losses?

Then route to deterministic engine and return ITR-3 vs ITR-4 with reasoning path.

