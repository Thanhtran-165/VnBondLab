# Agent Handoff — đưa VN YieldCurveLab v3.4.0 lên GitHub

## Mục tiêu

Đưa **nguyên trạng release V3.4.0** này vào repository. Đây là package runtime-baseline; không tự ý refactor logic Pine, đổi threshold, thêm nguồn dữ liệu hoặc đổi wording semantic trong cùng commit import.

## Canonical source

`src/VN_YieldCurveLab_v3_4_0.pine`

Build marker phải giữ:

`20260905-V340-EVIDENCE-SEMANTIC`

## Cấu trúc đề xuất trong repo

```text
README.md
CHANGELOG.md
VERSION
src/
  VN_YieldCurveLab_v3_4_0.pine
docs/
  QA_STATUS.md
  AI_BENCHMARK.md
  runtime/
    RUNTIME_EVIDENCE.md
    VN10Y_2026-09-05_17-00-47.png
  design/
    V3_4_IMPLEMENTATION_PLAN.md
tests/
  test_v34_contract.py
  test_v34_semantics.py
  verify_release.py
  fixtures/
    VN_YieldCurveLab_v3_3_1_baseline.pine
SHA256SUMS.txt
```

## Trước commit

Chạy:

```bash
python tests/test_v34_contract.py src/VN_YieldCurveLab_v3_4_0.pine
python tests/test_v34_semantics.py
python tests/verify_release.py
sha256sum -c SHA256SUMS.txt
```

Nếu repo đã có cấu trúc khác, có thể map file vào cấu trúc hiện có nhưng phải giữ canonical source và tài liệu QA/runtime evidence.

## Commit gợi ý

`feat: add VN YieldCurveLab v3.4.0 runtime baseline`

## Tag gợi ý

`v3.4.0`

## Không làm trong commit import

- Không đổi Pine logic.
- Không đổi contract IB lag 0–5 ngày.
- Không thêm VNINDEX.
- Không thêm combined score.
- Không thêm prediction/causal claims.
- Không xóa runtime evidence hoặc QA limitations.
- Không tự thêm LICENSE nếu repo owner chưa chọn license.

Nếu muốn refactor sau import, tạo issue/branch riêng và giữ V3.4.0 làm baseline so sánh runtime.
