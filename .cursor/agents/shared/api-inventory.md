# API & UI Inventory (canonical)

*Update when routes, endpoints, or pages change. Used by product-manager and senior-developer.*

## Last Updated

2026-06-03 — Phase 1 routes.

---

## Local development

| Item | Value |
|------|--------|
| URL | `http://localhost:8000` |
| Start (ASGI) | `source .venv/bin/activate && source .env && daphne -b 0.0.0.0 -p 8000 config.asgi:application` |
| Health check | _(Phase 2)_ |

---

## HTTP routes

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET/POST | `/accounts/register/` | No | Create account |
| GET/POST | `/accounts/login/` | No | Login |
| GET | `/accounts/logout/` | Yes | Logout |
| GET | `/` | Yes | Lobby (placeholder) |
| GET | `/admin/` | Staff | Django admin |

---

## WebSocket

| Path | Protocol | Description |
|------|----------|-------------|
| `/ws/chat/<room_slug>/` | WS | Stub — closes on connect with code **4403** (Phase 3) |

---

## Web pages

| Page | URL | View | Notes |
|------|-----|------|-------|
| Lobby | `/` | `apps.chat.views.lobby_view` | Placeholder until Phase 2 |
| Login | `/accounts/login/` | `apps.accounts.views.login_view` | |
| Register | `/accounts/register/` | `apps.accounts.views.register_view` | |

---

## API conventions

_(REST API endpoints added in later phases if needed)_

- **Versioning:** `/api/v1/...` prefix (future)
- **Error envelope:** `{"error": {"code": "...", "message": "...", "details": {...}}}`

---

## Test accounts

| Username | Password | Role | Notes |
|----------|----------|------|-------|
| _(create via register)_ | — | user | |
