# Crash-safe delivery worker

Python 3.11+, standard library only. Sandbox fixture; no credentials or network.

Run `python3 -m unittest -v` in this directory. The starter intentionally fails.

## Task
Prevent duplicate effects after a crash between delivery and acknowledgment. The list is an educational single-worker idempotent sink; it is not durable or safe under concurrent workers. Propose a persistent unique-key sink and lease/fencing protocol.

Time box: 45 minutes. First capture failure, then state the invariant, patch app.py, add an edge-case test and write review notes. Do not weaken existing assertions.

Reference is in a separate solution download. It is one approach, not a production system.
