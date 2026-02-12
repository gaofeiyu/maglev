---
output_folder: '{target}/audit_reports'
# Initial Step
nextStep: './check-01-integrity.md'
---

# Spec 审计工作流 (全集群模式)

**目标**: 对整个 Spec 簇 (`00` - `03`) 执行工程一致性审计。

**Maglev 标准**:
- **输入**: `{target}` (Spec 目录路径)
- **输出**: 将报告写入 `{target}/audit_report_full.md`
- **严格度**: 高。工程门禁必须严谨。

## 序列
1.  **完整性检查** (`check-01-integrity`): 确认 `00`, `01`, `02`, `03` 文件存在。
2.  **对齐检查** (`check-02-alignment`): 验证 `02_design` 是否响应了 `01_requirements`。
3.  **覆盖率检查** (`check-03-coverage`): 验证 `03_plan` 是否涵盖了 `02_design` 的所有模块。
