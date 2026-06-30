## Review demo: add a user store helper

Adds `review-demo/user-store.js`, a small helper for looking up users and
checking admin status.

This PR exists as a **teaching fixture for Lab 12** (the `claude ultrareview`
step). It is intentionally left **open** for the duration of the course so
students can run a real cloud review against it:

```bash
claude ultrareview <this PR number>
```

The file contains several deliberate, real issues (a hardcoded secret, a SQL
injection, a loose-equality admin check, insecure token generation, and an
unhandled async path that logs a password) so the deep review has concrete
findings to surface.

**Do not merge** while the course is running.
