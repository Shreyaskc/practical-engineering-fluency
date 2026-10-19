# Bounded async enrichment

Python 3.11+, standard library only. Sandbox fixture; no credentials or network.

Run `python3 -m unittest -v` in this directory. The starter intentionally fails.

## Task
Bound active fetch calls, preserve ordering, propagate caller cancellation and drain tasks. Extension: bound task allocation and add an overall timeout using asyncio.timeout.

Time box: 45 minutes. First capture failure, then state the invariant, patch app.py, add an edge-case test and write review notes. Do not weaken existing assertions.

Reference is in a separate solution download. It is one approach, not a production system.
