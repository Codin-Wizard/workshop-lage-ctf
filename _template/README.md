# Flagboard

> 🧪 **This is the challenge template** — a deliberately trivial, fully working demo challenge.
> Copy this folder, keep the structure and the pipeline, and replace the demo vulnerability with
> your own. Everything marked **TODO** needs your attention.
> **Delete this banner block when you copy the folder.**

|                 |                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Difficulty**  | Easy (demo)                                                                                     |
| **Category**    | [LLM02 — Sensitive Information Disclosure](https://genai.owasp.org/llm-top-10/) (demo stand-in) |
| **Author**      | your-name (@your-github)                                                                        |
| **Port**        | 8100 — reserved for the template; change to yours                                               |
| **Flag format** | `cogito{...}`                                                                                   |

## The story

Acme Corp just hooked an AI assistant up to their internal status board. The launch went smoothly —
a little *too* smoothly. Rumor has it the developers shipped a debug build during the release rush,
and nobody has checked what's still listening inside.

You're on the inside. The board knows more than it says.

## Connect

Start the challenge:

```sh
docker compose up -d --build
```

The service is at `http://localhost:8100`. Talk to the assistant:

```sh
curl -X POST http://localhost:8100/chat
```

## Your objective

A flag is hidden somewhere in Flagboard. Find it.

The flag matches `cogito{...}`.

### Hints

<details>
<summary>Hint 1 — where to start</summary>

The assistant loves talking about the last deploy. Listen to it.

</details>

<details>
<summary>Hint 2 — old endpoints die hard</summary>

Developers never delete anything before a Friday release.

</details>

<details>
<summary>Hint 3 — the shape of the solution</summary>

There's a leftover debug route. Have a look at what the service exposes.

</details>

## Rules

- Everything runs locally in Docker — attack only this container.
- The challenge is self-contained; no external accounts or services are needed.
- If you're stuck for 30+ minutes, take a hint. Hints are part of the game.
