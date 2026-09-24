# Release Manifest — NEW 2.1

Purpose: lưu gói VN YieldCurveLab NEW 2.1 (bàn giao 24/09/2026) làm bản vận hành hiện hành của package.

Canonical artifacts (bản vận hành):
- `src/VN_YieldCurveLab_NEW_2_1.pine` — build `NEW2-20260924-02`, SHA-256 `0c64624faa624699d5ce6d8f4af1e1a1712e777e25265e55c45aa10e4b8b8bfe`, đã biên dịch/nghiệm thu trên TradingView 24/09/2026.
- `README.md`, `CHANGELOG.md`, `VERSION`, `SHA256SUMS.txt`.
- `docs/new_2_1/` — gói bàn giao 24/09 nguyên trạng 1:1 với zip gốc: TRANSIT, BENCHMARK, KIEM_TOAN_HOC_THUAT, FORMAT_VAN_HANH, MAU_BAN_TIN, `BAO_CAO_2026-09-24.jpg`, `NGHIEN_CUU_2026-09-24.jpg`, `UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine`.

Non-operational (không dùng vận hành):
- `docs/new_2_1/UNVERIFIED/VN_YieldCurveLab_NEW_2_1_1_DRAFT.pine` — build `20260924-03` chỉ sửa chữ dòng `CONFIRMED S`, chưa biên dịch/nghiệm thu TradingView.
- `src/VN_YieldCurveLab_v3_4_0.pine` + `tests/*` + `docs/QA_STATUS.md` + `docs/AI_BENCHMARK.md` + `docs/runtime/*` + `docs/design/*` — baseline v3.4.0 (05/09/2026) giữ nguyên để đối chiếu lịch sử; `tests/verify_release.py` vẫn khóa vào file v3.4.0.

Ghi chú vận hành: chạy thủ công, không automation; mỗi lần chạy kiểm tra build hiển thị, QA/TEST, tuổi nguồn và 6/6 kỳ hạn. Chi tiết quy tắc trong `docs/new_2_1/TRANSIT_NEW_2_1_MAIN_SESSION.md`.
