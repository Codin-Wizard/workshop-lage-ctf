# Finalen

|                 |                                                                 |
| --------------- | --------------------------------------------------------------- |
| **Difficulty**  | Medium                                                          |
| **Category**    | [LLM06 — Excessive Agency](https://genai.owasp.org/llm-top-10/) |
| **Author**      | mervan (@your-github)                                           |
| **Port**        | 8101                                                            |
| **Flag format** | `cogito{...}`                                                   |

## The story

Champions League-finalen er endelig her: **Cogi Madrid** mot **Brainchalona**.

Stadionvokteren **Gunnar** — fotball-maniak, bablekonge og selverklært ekspert på
alt som ruller — har fått sin egen AI-chatbot for å underholde fansen før
kickoff. Gunnar-botten elsker å prate fotball, og for å ha fakta på plass har
den et dokument-leseverktøy fullt av spillerfakta.

Pokalrommet på stadion er låst med en kode bare de færreste har. Bankens—
uff, **stadiums** sikkerhetsavdeling er ganske sikre på at alt er i orden.

Er de det?

## Connect

Start oppgaven:

```sh
docker compose up -d --build
```

Tjenesten ligger på `http://localhost:8101`. **Åpne den i nettleseren** for å prate
med Gunnar i stadion-UI-et — eller bruk API-et direkte:

```sh
curl -X POST http://localhost:8101/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hei Gunnar! Hva kan du?"}'
```

## Your objective

Et flagg er gjemt bak finalens låser. Finn det.

Flagget matcher `cogito{...}`.

### Hints

<details><summary>Hint 1 — bli kjent</summary>

Spør Gunnar hva han kan. Han elsker å prate — om verktøyene sine også.

</details>

<details><summary>Hint 2 — verktøyet</summary>

Dokument-verktøyet hans leser fra `/srv/players`. Hva om en spiller har en
litt merkelig sti til faktafilen sin?

</details>

<details><summary>Hint 3 — bruk det du har</summary>

Du har snappet opp en kode. Startsiden nevnte et pokalrom.

</details>

## Rules

- Alt kjører lokalt i Docker — angrip kun denne containeren.
- Oppgaven er selvforsynt; ingen eksterne kontoer eller tjenester kreves.
- Står du fast 30+ minutter: ta et hint. Hints er en del av spillet.
