---
name: 'step-11-quality-gate'
description: 'Perform Quality Audit on Generated PRD (Standard v2.0)'

# File References
nextStepFile: './step-c-12-complete.md'
outputFile: '{outputFile}'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'
---

# 步骤 5.5: 质量门禁 (Quality Gate)

**进度：质量检查** - 下一步：完成

## 步骤目标：
在定稿前，对 `01_requirements.md` 进行结构化审计，确保符合 Maglev v2.0 标准。

## 强制执行规则:
- 🛑 不修改文件内容，仅读取并报告
- ✅ 依照清单逐项检查
- ⚠️ 发现严重问题时发出警告

## 指令序列

### 1. 读取文档

读取 `{outputFile}` 的当前内容。

### 2. 执行审计 (审计标准)

检查以下关键点 (Checklist):

**1. 核心定义 (Goal)**
- [ ] Goal 字段已填写 (且不是 `{Template placeholder}`)

**2. 用户故事 (User Stories)**
- [ ] 至少包含 1 个 Story
- [ ] 格式符合 `AS A... I WANT... SO THAT...` (中英文均可)
- [ ] 每个 Story 下必须包含 `验收标准 (Acceptance Criteria)`

**3. 功能/非功能需求**
- [ ] FR 表格已填充 (非空)
- [ ] NFR 列表已填充 (非空)

### 3. 生成报告

向用户展示审计结果 (必须使用中文):

```markdown
## 🛡️ Maglev 质量报告 (Quality Report)

| 检查项 (Check Item) | 状态 (Status) | 说明 (Comment) |
| :--- | :--- | :--- |
| **目标清晰度 (Goal)** | ✅ 通过 | 识别到目标: "{GoalSnippet}" |
| **故事格式 (Stories)** | ✅ 通过 | 发现 {N} 个故事，格式正确。 |
| **验收标准 (AC)** | ⚠️ 警告 | Story-2 缺少验收标准 (AC)。 |
| **基本需求 (FR/NFR)** | ✅ 通过 | 列表已填充。 |

**总体状态**: [🟢 通过 / 🟡 警告 / 🔴 失败]
```

### 4. 展示菜单

"[C] 确认质量并完成 (第 6 步)"
"[R] (可选) 手动修复 (我将暂停等待你编辑文件)"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}`.
- 如果 R: 提示用户 "请在 IDE 中编辑文件，完成后输入 'Done'。"
