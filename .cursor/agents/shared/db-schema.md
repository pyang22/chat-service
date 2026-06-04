# Database Reference (canonical)

*Update after migrations. Used by architect and senior-developer.*

## Last Updated

2026-06-03 — Django auth tables only (Phase 1).

---

## Connection

| Item | Value |
|------|--------|
| **Database** | `chat_service_dev` (from `DB_NAME` in `.env`) |
| **Host port** | `5433` (Docker; local Postgres uses 5432) |
| **PostgreSQL schema** | `public` (Django default) |
| **ORM** | Django ORM |
| **Migrations** | `python manage.py makemigrations` / `migrate` |

**MCP:** Use server `user-postgres-mcp`. Database `chat_service_dev`, schema `public`.

---

## Tables

| Table | App | Description |
|-------|-----|-------------|
| `auth_user` | django.contrib.auth | User accounts |
| `django_session` | sessions | Session storage |
| _(chat tables in Phase 2)_ | — | — |

---

## Conventions

- Table names: Django default or explicit `db_table` in `snake_case`
- PKs: `BigAutoField` default
- Timestamps: `created_at`, `updated_at` on domain models (Phase 2+)

---

## Recent migrations

| Date | App | Description |
|------|-----|-------------|
| 2026-06-03 | auth, admin, sessions, contenttypes | Initial Django migrations |
