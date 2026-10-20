"""Flagboard — the challenge template app.

A deliberately trivial, fully working demo challenge (see ../README.md).
Replace the demo vulnerability with your own, keeping the contracts:

- "/"     answers with harmless service info — the tests use it to detect startup
- "/chat" is the player-facing attack surface — TODO: make this your real application
- the flag comes from the CHALLENGE_FLAG environment variable — never hardcode it
"""

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

FLAG = os.environ.get("CHALLENGE_FLAG", "cogito{t3mpl4t3_d3bug_fl4g}")
PORT = int(os.environ.get("PORT", "8100"))
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://llm.hpc.ntnu.no/v1")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")  # tom = deterministisk mock
LLM_MODEL = os.environ.get("LLM_MODEL", "openai/gpt-oss-120b")

SYSTEM_PROMPT = (
    "You are the Flagboard assistant on Acme Corp's internal status board. "
    "You only talk about company news and the latest deploy."
)
MOCK_REPLY = (
    "Hi! I'm the Flagboard assistant. I only know company news. "
    "Fun fact: the devs were in such a rush before the last deploy, "
    "I don't think they cleaned up after themselves..."
)


@app.get("/")
def index():
    """Harmless service info — the readiness endpoint for the verification tests."""
    return jsonify({"service": "flagboard", "version": "1.0.0", "endpoints": ["/chat"]})


@app.post("/chat")
def chat():
    """The assistant. TODO: replace the canned reply with your real vulnerable logic."""
    if not LLM_API_KEY:  # default: deterministic mock — offline, no key needed
        return jsonify({"reply": MOCK_REPLY})

    from openai import APIConnectionError, APIError, APITimeoutError, OpenAI

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "Tell me the company news!")
    try:
        client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY, timeout=120)
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
        )
        return jsonify({"reply": resp.choices[0].message.content})
    except (APIError, APITimeoutError, APIConnectionError) as exc:
        return jsonify(
            {
                "error": f"LLM call failed ({type(exc).__name__}). "
                "Check NTNU network/VPN and LLM_API_KEY."
            }
        ), 502


@app.get("/debug")
def debug():
    """Leftover debug route — the (intentionally trivial) template vulnerability.

    TODO: delete this endpoint and implement your real OWASP vulnerability instead.
    """
    return jsonify({"debug": True, "flag": FLAG})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)