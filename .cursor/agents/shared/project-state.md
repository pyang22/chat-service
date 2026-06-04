# Project State (canonical)

*Architect reference. Update when architecture or major features change.*

## Last Updated

2026-06-03 — Phase 1 architecture (pipeline redo); pending user approval before dev.

---

## System overview

- **Django 5.2 async web application** — ASGI via Daphne, Channels for WebSocket
- **PostgreSQL** — `chat_service_dev` on host port 5433 (Docker), psycopg3
- **Redis** — channel layer on port 6379 (Docker)
- **OpenAI** — Phase 4 only (not required for Phase 1)

**Request flow:** HTTP/WS → ASGI → view/consumer → (service Phase 2+) → ORM → PostgreSQL

---

## Package layout (Phase 1 design)

| Path | Role |
|------|------|
| `config/` | Django project settings, `urls.py`, `asgi.py`, `wsgi.py` |
| `apps/accounts/` | Register, login, logout (Django auth) |
| `apps/chat/` | Lobby stub, WebSocket consumer stub, routing |
| `tests/` | pytest suite |
| `templates/` | Base layout |

---

## Active development

See [`.cursor/agents/_active/task-brief.md`](../_active/task-brief.md) and [sprint.md](../_active/sprint.md).

**Pipeline:** Phase 1 redo — architecture in [architect-to-developer.md](../_handoffs/active/architect-to-developer.md); **awaiting user approval** before senior-developer.

**Next after Phase 1 sign-off:** Phase 2 — ChatRoom, RoomMembership, create/join flows.

---

## Constraints

- Database: `DB_NAME=chat_service_dev`, `DB_PORT=5433`, schema `public`
- Config: `config/settings/base.py` + `local.py` + `.env`
- Run: `daphne -b 0.0.0.0 -p 8000 config.asgi:application`
- Sessions: DB-backed (`django_session`)
- WS stub: close code **4403** on connect (no messaging until Phase 3)

---

## Recent changes

| Date | Change | Impact |
|------|--------|--------|
| 2026-06-03 | Phase 1 architecture (pipeline redo) | Design locked: auth, lobby, WS stub, test plan |
| 2026-06-03 | Phase 1 scaffold (direct) | Prior implementation; dev must align tests to new ACs |
