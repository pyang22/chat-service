# QA Test Checklist

Record results in `_handoffs/active/qa-to-pm.md`.

## API (`http://localhost:8000`)

- [ ] Endpoints match `shared/api-inventory.md`
- [ ] Happy path vs PM acceptance criteria
- [ ] Validation errors return correct status + error envelope
- [ ] Auth required endpoints reject unauthenticated requests
- [ ] Cross-user resource access denied (IDOR)
- [ ] Pagination and filtering behave correctly
- [ ] OpenAPI docs match actual behavior

## Browser (if UI involved)

Start app in a separate terminal (see `shared/api-inventory.md`).

- [ ] Feature happy path vs PM acceptance criteria
- [ ] Empty / loading / error states
- [ ] Navigation regressions on other pages
- [ ] Real-time updates (if applicable): connect, disconnect, reconnect

## Unit / integration tests

- [ ] Commands from `active/developer-to-qa.md` pass
- [ ] New behavior covered; no critical gaps
- [ ] Edge cases: empty lists, concurrent writes, invalid input

## Security

- [ ] No secrets in responses or logs
- [ ] Input sanitization on user-generated content
- [ ] Rate limiting (if configured) triggers correctly

## Architecture

- [ ] Matches `active/architect-to-developer.md`
- [ ] View → service → model layering respected
- [ ] `active/developer-deviations.md` empty or architect-acknowledged

## Sign-off

| Area | Pass/Fail | Notes |
|------|-----------|-------|
| API | | |
| Browser | | |
| Unit/integration tests | | |
| Security | | |
| Architecture | | |
| **Overall** | | |
