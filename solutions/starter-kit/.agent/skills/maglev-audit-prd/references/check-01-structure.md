---
name: 'check-01-structure'
description: '审计 PRD 结构和元数据'

# References
nextStepFile: './check-02-stories.md'
targetFile: '{targetFile}'
---

# 审计步骤 1: 结构完整性

**下一步**: 故事审计

## 目标
验证 `01_requirements.md` 是否符合 Maglev v2.0 文件标准。

## 规则
- 🛑 **只读**: 不要修改输入文件。
- ✅ **严格审计**: 任何缺失的必填部分均视为失败 (FAIL)。

## 审计检查清单

### 1. 元数据 (Frontmatter)
- [ ] `type: spec_requirements` 是否存在?
- [ ] `version: 2.0` 是否存在?
- [ ] `slug` 是否已定义?

### 2. 标题结构
- [ ] `> **Goal**:` 是否存在?
- [ ] `## 1. 用户故事` (或 User Stories) 是否存在?
- [ ] `## 2. 功能性需求` (或 Functional Requirements) 是否存在?
- [ ] `## 3. 非功能性需求` (或 Non-Functional Requirements) 是否存在?

## Output Schema
Start the **Audit Report** holding structure:

```markdown
# 🛡️ 审计报告 (Audit Report): {slug}

## 1. 结构完整性检查 (Structural Check)
| 检查项 (Item) | 状态 (Status) | 说明 (Note) |
| :--- | :--- | :--- |
| **元数据 (Frontmatter)** | {PASS/FAIL} | {Details} |
| **章节布局 (Layout)** | {PASS/FAIL} | {Missing sections?} |
| **目标清晰度 (Goal)** | {PASS/WARN} | {Goal snippet or "Missing"} |
```
