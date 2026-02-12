---
name: 'step-02-discovery'
description: 'Discover Goal and Context (Standard v2.0)'

# File References
# Skip Success/Domain/etc., jump to User Stories
nextStepFile: './step-c-04-journeys.md'
outputFile: '{outputFile}'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'
partyModeWorkflow: 'references/party-mode.workflow.md'
---

# 步骤 2: 项目发现 (Standard v2.0)

**进度：第 2 步，共 5 核心步骤** - 下一步：用户故事

## 步骤目标：
基于上下文定义产品的核心目标 (Goal)，填充 `01_requirements.md` 的 `> **Goal**` 部分。

## 强制执行规则:
- 🛑 绝不 在没有用户输入的情况下生成内容
- ✅ 目标必须简洁有力 (一句话)

## 指令序列

### 1. 分析上下文

阅读 `inputDocuments` (e.g. Brief)。
提炼核心目标。
*   Question: "用一句话概括，我们要在这个 Spec 中达成什么核心目标？"

### 2. 定义 Goal

当用户确认后，生成 Goal 语句。
Format: `> **Goal**: {Statement}`

### 3. 编辑文档

**Action**:
使用工具将 `> **Goal**: {Statement}` 写入 `{outputFile}`，替换模板中的占位符。

### 4. 展示菜单

"[C] 继续 - 保存并移动到用户故事 (第 3 步)"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}`.

