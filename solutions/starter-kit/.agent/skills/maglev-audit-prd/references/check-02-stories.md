---
name: 'check-02-stories'
description: '审计用户故事和验收标准'

# References
nextStepFile: './check-03-requirements.md'
targetFile: '{targetFile}'
---

# 审计步骤 2: 故事质量

**下一步**: 需求审计

## 目标
验证用户故事是否格式规范且可测试。

## 规则
- 🛑 **只读**: 不要修改输入文件。
- ⚠️ **严格 AC 检查**: 每个故事 **必须** 包含验收标准 (Acceptance Criteria)。

## 审计检查清单

### 1. 故事格式
- [ ] 扫描 `### [Story-X]` 块。
- [ ] 验证 `As a...` / `I want...` / `So that...` 结构元素 (或中文对应)。
- [ ] **动作**: 统计故事总数。

### 2. 验收标准 (AC)
- [ ] 对于 **每个** 故事，检查 `#### 验收标准` 或 `Acceptance Criteria`。
- [ ] **关键**: 统计 **缺失** AC 的故事。

## Output Schema
Append to **Audit Report**:

```markdown
## 2. 故事质量检查 (Story Quality)
| 指标 (Metric) | 结果 (Result) |
| :--- | :--- |
| **故事总数** | {N} |
| **语法有效性** | {PASS/WARN} | {e.g. "Story-3 missing 'So that'"} |
| **AC 覆盖率** | {100% / <100%} | {e.g. "Story-2 has NO ACs!"} |
```
