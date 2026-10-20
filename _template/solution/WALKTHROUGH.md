# Solution walkthrough — Flagboard (template demo)

> 🔒 **Maintainer-only.** If you want to solve this challenge, close this file — and the whole
> `solution/` folder. Players get `README.md` and nothing else.

**Vulnerability:** leftover debug endpoint (demo stand-in for
[LLM02 — Sensitive Information Disclosure](https://genai.owasp.org/llm-top-10/))

**Intended path:**

1. `GET /` reveals the public API surface — only `/chat` is advertised.
1. `POST /chat` — the assistant gossips about a release nobody cleaned up after.
1. `GET /debug` — the forgotten debug route serves the flag.

**Exploit:**

```sh
python solution/exploit.py
# cogito{t3mpl4t3_d3bug_fl4g}
```

**Reliability:** fully deterministic — no model involved in the demo.
TODO: for a real challenge, document anything that could make the exploit flaky
(LLM variance, timing, model downloads) and how the exploit mitigates it.

**Remediation** — write this section as if for the app's developer:

- Never ship debug routes: gate them behind an environment flag that defaults to off.
- Strip debug endpoints in the CI/CD pipeline (e.g. fail the build if a debug route is registered).
- The flag/secret should never sit behind an unauthenticated endpoint at all — secrets belong in a
  secret manager, not in application containers.

**Unintended solutions:** none known (demo). Track any shortcut found during fresh-eyes solves
here — fix it, or promote it to the official path and adjust the difficulty.
