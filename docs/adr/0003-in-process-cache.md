# ADR 0003: In-process link cache with pub/sub invalidation

- Status: Accepted
- Date: 2026-10-15
- Supersedes: [ADR 0001](0001-link-cache.md)

## Context

ADR 0001 moved the link cache into a shared Redis instance because 3 replicas across 2 regions each
kept a cold, stale in-process cache. Since then:

- The Redis hop pushed p99 redirect latency from 4 ms to 12 ms (#6).
- We now run 2 replicas in a single region, so the main reason for a shared cache is gone.

## Decision

Each replica keeps an in-process LRU. A link edit publishes an invalidation message that every
replica applies. Cold starts after deploys are handled by warming the top 10k links on boot.

## Alternatives considered

- **Keep the shared Redis cache.** Rejected: it costs a network hop on every redirect, which is now
  our biggest latency cost, and we no longer need cross-region sharing.

## Consequences

- Redirects for cached links make no network call.
- Invalidation depends on pub/sub delivery; a missed message leaves one replica stale until eviction.
- Boot takes a little longer while the top 10k links load.
