# Idempotent shipment ledger

Python 3.11+, standard library only. Sandbox fixture; no credentials or network.

Run `python3 -m unittest -v` in this directory. The starter intentionally fails.

## Task
Stable receipts across retries and reopen; reject invalid quantity and changed intent. Scope is a single tenant. Explain how to extend uniqueness for multiple tenants.

Time box: 45 minutes. First capture failure, then state the invariant, patch app.py, add an edge-case test and write review notes. Do not weaken existing assertions.

Reference is in a separate solution download. It is one approach, not a production system.
