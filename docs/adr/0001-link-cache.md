# ADR 0001: Link cache

- Status: Superseded by [ADR 0003](0003-in-process-cache.md)
- Date: 2026-10-15

## Context

Redirects look up the target URL for a short code on every request. Each of our 3 API replicas
(across 2 regions) keeps its own in-process LRU. Every deploy starts 3 cold caches, and invalidation
after a link edit only reaches the replica that handled the edit (#1).

## Decision

Move the link cache into a shared Redis instance with a 24-hour TTL. Editing a link deletes its key.

## Alternatives considered

- **Keep the in-process LRU and add pub/sub invalidation.** Rejected: with 3 replicas across 2 regions,
  that is more moving parts than one Redis.

## Consequences

- The cache stays warm across deploys; an edit is a single delete.
- Every redirect makes a network hop, expected to cost ~1-2 ms.
