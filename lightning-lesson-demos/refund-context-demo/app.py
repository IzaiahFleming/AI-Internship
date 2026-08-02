"""Lightning lesson demo: prompt-only vs context-packed refund decision.

Run:  uvicorn app:app --reload --port 8765
Open: http://127.0.0.1:8765
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel, Field

from prompts import CONTEXT, LOCKED_REQUEST

load_dotenv(Path(__file__).resolve().parent / ".env")

app = FastAPI(title="Context > Prompt — Refund Demo")
STATIC = Path(__file__).resolve().parent / "static"


class RunRequest(BaseModel):
    mode: str = Field(..., pattern="^(prompt|context)$")


class RunResponse(BaseModel):
    mode: str
    answer: str
    model: str


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/api/demo")
def demo_payload():
    return {
        "locked_request": LOCKED_REQUEST,
        "context": CONTEXT,
    }


@app.post("/api/run", response_model=RunResponse)
def run(req: RunRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY missing. Symlink or copy a .env into this folder.",
        )

    client = OpenAI()
    if req.mode == "prompt":
        system = (
            "You are a customer support lead. Use only facts present in the user message. "
            "If policy rules or order details needed for a decision are missing, do not invent them — "
            "say what you need and hedge rather than approving or denying with certainty."
        )
        content = LOCKED_REQUEST
    else:
        system = (
            "You are a customer support lead. Follow the instructions and knowledge in the user message. "
            "Prefer current/effective policy over archived. Be warm, decisive, and brief."
        )
        content = CONTEXT

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": content},
    ]

    try:
        completion = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0.3,
            max_tokens=220,
            messages=messages,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    answer = (completion.choices[0].message.content or "").strip()
    return RunResponse(mode=req.mode, answer=answer, model=completion.model)


app.mount("/static", StaticFiles(directory=STATIC), name="static")
