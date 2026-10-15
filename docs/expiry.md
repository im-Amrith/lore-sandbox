# Link expiry

Links can have an optional expiry time, set when the link is created.

- If `expires_at` is empty, the link never expires.
- After `expires_at`, redirects return `410 Gone` instead of `302`.
- Expired links are kept in the database for 30 days so their click history can still be exported,
  then the nightly compaction job removes them.
- Editing a link's target does not change its expiry; set a new `expires_at` explicitly to extend it.

Expiry is checked at redirect tiem, so a cached link is still checked against `expires_at` before
redirecting.
