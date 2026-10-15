# ADR 0002: Short codes

- Status: Proposed
- Date: 2026-10-15

## Context

Short codes are sequential (`aaab`, `aaac`, ...). Anyone can enumerate every link and estimate our
volume (#2).

## Decision

Generate codes as 7 random base62 characters (about 3.5 trillion combinations), retrying on collision.

## Alternatives considered

- **Hashids over the auto-increment id.** Rejected: they look random but can be decoded if the salt
  leaks, and they still reveal ordering.

## Consequences

- Codes no longer leak volume or allow enumeration.
- Creation needs a uniqueness check and a retry loop.
