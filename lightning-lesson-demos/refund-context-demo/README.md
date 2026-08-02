# Context > Prompt — Refund Decision Demo

Two-run live demo for lightning lessons: same locked request, with and without retrieved context.

## Setup

```bash
cd lightning-lesson-demos/refund-context-demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

`.env` is symlinked to `ai-engineering-bootcamp-v2/week-1v2/.env` (`OPENAI_API_KEY`). Or copy `.env.example` → `.env`.

## Run

```bash
cd lightning-lesson-demos/refund-context-demo
source .venv/bin/activate
uvicorn app:app --reload --port 8765
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765)

## Demo flow

1. **Run 1 — Prompt only** → expect a weak / hedged answer (no order age, no policy).
2. **Run 2 — With context** → expect **approve** + cite Jan 2025 defective-item clause (60 days; order is day 44).
