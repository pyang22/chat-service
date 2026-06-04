# chat-service

Multi-user chat web application with AI room agents. Built with Django async, Django Channels, PostgreSQL, and OpenAI.

## Prerequisites

- Python 3.12+
- Docker (PostgreSQL + Redis)

## Quick start

```bash
# 1. Virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Environment
cp .env.example .env
# Edit .env if needed (OPENAI_API_KEY for Phase 4)

# 3. Infrastructure
docker compose up -d

# 4. Database
python manage.py migrate

# 5. Run (ASGI via Daphne)
daphne -b 0.0.0.0 -p 8000 config.asgi:application
```

Open http://localhost:8000 — register, login, and land on the lobby.

Optional admin access: `python manage.py createsuperuser` then visit `/admin/`.

## WebSocket stub

Phase 1 exposes `ws/chat/<room_slug>/` but closes immediately with code **4403** (chat arrives in Phase 3).

## Development

| Service | Host port | Notes |
|---------|-----------|-------|
| PostgreSQL | 5433 | Avoids conflict with local Postgres on 5432 |
| Redis | 6379 | Channels channel layer |
| App | 8000 | Daphne ASGI server |

```bash
pytest
python manage.py check
```

## Project layout

```
config/          Django project (settings, urls, asgi)
apps/accounts/   Auth (register, login, logout)
apps/chat/       Chat app (rooms, WebSocket — Phases 2–4)
tests/           pytest suite
```

## Feature pipeline

Agent workflow lives in `.cursor/agents/`. Invoke `@feature-pipeline` to orchestrate PM → architect → dev → QA.

## Implementation phases

1. **Scaffold** (done) — Django, Channels, PostgreSQL, Redis, auth stubs
2. **Rooms** — create/join public & private chat rooms
3. **Real-time chat** — WebSocket messaging + DB persistence
4. **AI agent** — selective OpenAI participation per room persona
5. **Polish** — tests, README, demo script
