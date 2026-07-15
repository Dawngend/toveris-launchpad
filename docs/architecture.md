# Architecture decision record

## Context

The prototype needs a credible end-to-end payment workflow today and a clean migration path to Stellar tomorrow.

## Decision

Business rules live in `app/domain`; HTTP, persistence, and ledger services are adapters. `LedgerPort` is the seam between the transaction use case and any chain implementation. The supplied adapter writes deterministic simulated transaction records in SQLite.

## Consequences

- Tests can validate risk and transfer rules without an API server or blockchain node.
- Replacing the simulation requires a new adapter, rather than edits to core banking rules.
- Ledger transaction IDs are explicitly labelled simulated and must not be represented as live Stellar transactions.
