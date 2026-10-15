# Tern

Tern is a demo URL shortener: it creates short links, redirects visitors and counts clicks.

> **This is synthetic demo data.** This repository, its issues, pull requests, people and history were
> created for the [Lore](https://github.com/im-Amrith) hackathon project. Tern is not a real product.
> Some commit dates are backdated to simulate project history.

## Layout

- `api/`: HTTP handlers, short-code generation, limits
- `cache/`: link cache used by redirects
- `analytics/`: click counting and CSV export
- `storage/`: database access and compaction
- `docs/`: ADRs and feature docs
