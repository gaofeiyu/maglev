---
output_folder: '{validation_report_folder}'
# Initial Step
nextStep: './check-01-structure.md'
---

# PRD 审计工作流 (安全模式)

**目标**: 对 `01_requirements.md` 执行只读审计。

**Maglev 标准**:
- **输入**: `{targetFile}` (通过参数传递)
- **输出**: 将报告写入 `{targetFile}_audit_report.md` (或类似文件)
- **非破坏性**: 此工作流 **绝不** 修改输入文件。

## 序列
1.  **结构检查** (`check-01-structure`): Frontmatter, 标题, 目标。
2.  **故事检查** (`check-02-stories`): 用户故事, AC 格式。
3.  **逻辑检查** (`check-03-requirements`): FR/NFR, SMART 分析, 优先级。
