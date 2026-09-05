# VN YieldCurveLab V3.4 Implementation Plan

Goal: Upgrade V3.3.1 into V3.4 Evidence Expansion & Semantic Integrity while preserving Dual Engine + Late Fusion architecture.

Tasks:
1. Add failing static/runtime-reference tests for new V3.4 contracts: evidence ranks/decomposition, tenor 1D/1W/1M/3M, explicit windows, gap driver, liquidity market-rate vs relative-gap state, transmission matrix incl. divergence and Bond-leading cases, alignment quality, last-valid transmission snapshot, liquidity ranges, early observation, active contract metadata, research triggers.
2. Implement Bond evidence outputs without changing accepted snapshot logic.
3. Implement temporal window dates and 60-session context.
4. Implement Liquidity semantic decomposition and range statistics on event ledger.
5. Replace Transmission message tree with complete directional taxonomy; add alignment quality and last-valid snapshot storage.
6. Add research-trigger outputs derived descriptively from engine states; never causal.
7. Redesign Overview as AI evidence surface retaining Dual Engine visual zones and calm-warning semantics.
8. Preserve panels 2/3; add only evidence needed for auditability.
9. Run regression/static/property tests and package Pine/TXT/README/QA/test evidence.

Global constraints:
- No VNINDEX.
- No forecast probability or combined score.
- Bond and Liquidity states remain independent until Transmission.
- IB lag 0-5 calendar days accepted as-of; carry-forward is not a new event.
- No causal attribution.
- Preserve current source requests and closed-snapshot integrity.
- Pine compiler/runtime still requires TradingView validation by user.
