# Practical Engineering Fluency

Python-first work-like engineering practice for experienced engineers. Original sandbox exercises; complements DSA. No hiring guarantees. No service credentials, production access, trackers, paid services or build dependencies.

## Start

`python3 -m http.server 8000` in this folder, then open http://localhost:8000. Do not use file:// because lessons load from JSON. Open index.html through HTTP. Browser progress uses localStorage, with an in-memory fallback. Reset through the course footer section.

## Navigation

12 sequenced lessons → four downloadable broken labs → 60-minute simulation and five-dimension rubric → glossary, cheat sheet and primary sources. Courses navigation lists verified live siblings only. Extend the registry at the top of app.js after checking a new course is launched. Current links: AI Learning, System Design Fluency and DSA Fluency.

## Labs

Python 3.11+ standard library. Unzip a starter and run `python3 -m unittest -v`. Broken starters intentionally fail. Read each README, capture baseline, fix app.py and add tests. Separate references/ and reference ZIPs contain opt-in solutions; hidden means spoiler-separated, not secure. Do not treat reference code as production code. Outbox uses a single-worker in-memory sink to isolate the crash window; real sinks require durable atomic deduplication. Fanout bounds active calls but not allocated tasks; worker-pool allocation is an extension. Ledger models one tenant. Query fixtures test query count and plan shape, not production throughput.

## Verification and contribution

Run `python3 tools/check.py`: all starters must fail and all references must pass, ZIP members must be safe and lesson IDs complete. Run `node --check app.js`. For a new lab provide a realistic defect, deterministic reproduction, meaningful invariant tests, a reference with documented limits, and separate downloadable archives. Regenerate ZIPs after edits. Keep all fixture identities fictional. Do not add credentials or paid content.

Manual UI checks: search including no results; expand lesson and hint; toggle completion and reload; reset progress; timer start/pause/reset; all score selectors; starter and reference downloads; keyboard focus and narrow layout. Timing and scoring are practice aids. Readable source is intentionally public.

## References

Anthropic’s Staff+ Infrastructure posting explicitly describes work-like coding, a company/role-specific statement: https://job-boards.greenhouse.io/anthropic/jobs/4970314008 (checked 2026-10-19). Python docs: asyncio-task, sqlite3, profile. SQLite queryplanner. Links appear in the app.
