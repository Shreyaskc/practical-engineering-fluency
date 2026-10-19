# Tenant report query repair

Python 3.11+, standard library only. Sandbox fixture; no credentials or network.

Run `python3 -m unittest -v` in this directory. The starter intentionally fails.

## Task
Remove N+1 queries and supply an index that supports tenant/status filtering. Verify result isolation and a one-query budget. Explain index write overhead and why plan checks alone do not prove latency.

Time box: 45 minutes. First capture failure, then state the invariant, patch app.py, add an edge-case test and write review notes. Do not weaken existing assertions.

Reference is in a separate solution download. It is one approach, not a production system.
