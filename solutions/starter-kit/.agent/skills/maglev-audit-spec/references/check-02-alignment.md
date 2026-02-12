---
name: 'check-02-alignment'
description: '审计需求与设计的对齐情况'

# References
nextStepFile: './check-03-coverage.md'
targetDir: '{target}'
---

# 审计步骤 2: 需求对齐 (Requirements Alignment)

**下一步**: 覆盖率检查

## 目标
验证 `02_design.md` 中的技术设计是否真正响应了 `01_requirements.md` 中的需求。

## 规则
- 🛑 **只读**: 不要修改文件。
- 🔗 **追溯性**: 设计元素应引用需求 ID (如 `(Ref: Story-1)` 或 `(Ref: FR-01)`)。

## 审计检查清单

### 1. 核心链路检查
- [ ] **API 设计**: 是否每个 API Endpoint 都关联了 User Story 或 FR?
- [ ] **数据模型**: Check Schema 是否支持 FR 中的字段要求 (e.g. `deleted_at` for Soft Delete)。

### 2. 遗漏分析 ("Gap Analysis")
- [ ] 扫描 `01` 中的 P0 需求。
- [ ] 在 `02` 中搜索对应关键词。如果没有提及，标记为 **潜在遗漏**。

## 输出模式
追加到 **工程审计报告**:

```markdown
## 2. 需求-设计对齐 (Alignment)
| 检查点 (Check) | 状态 (Status) | 发现 (Finding) |
| :--- | :--- | :--- |
| **P0 覆盖率** | {High/Med/Low} | {N}/Total P0 covered. |
| **API 追溯性** | {PASS/WARN} | {e.g. "POST /login untraced"} |
| **遗漏警告** | {None/List} | {List strict misses} |
```
