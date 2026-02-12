---
name: 'step-01-scope-analysis'
description: '分析输入文档，提取测试对象'
workflow_path: '{project-root}/.agent/skills/maglev-create-test-cases/references/create-test-cases.workflow.md'
nextStepFile: './step-02-strategy-design.md'
wipFile: '{project-root}/specs/20_evolution/active/test_cases/test-plan-wip.md'
---

# 步骤 1: 范围分析

**目标**: 识别 PRD/Spec 中的所有 Functional Requirements (FR) 和 Acceptance Criteria (AC)。

## 规则
- 必须基于提供的 PRD/Spec 路径。
- 如果没有输入文件，询问用户。

## 指令序列

### 1. 检查输入
询问用户: "请提供 PRD 或 Tech Spec 的路径 (e.g. `specs/20_evolution/active/change-logs/spec.md`)。"

### 2. 分析与提取
读取该文件：
1. **提取 Title & Slug**。
2. **提取 FR List** (Functional Requirements)。
3. **提取 AC List** (Acceptance Criteria)。
4. **提取 Components** (如果是前端 Spec): 识别 UI 组件和交互点。
5. **提取 Constraints** (Constraints/Non-Functional Requirements)。

### 3. 上下文增强 (Context Augmentation)
1. **加载业务规则**: 尝试读取 `specs/00_planning/business_rules.md`。如果是空或不存在，假设通用规则或询问用户。
   > _(Goal: 理解隐性业务逻辑，如 "版本号生成"、"软删除" 等)_
2. **加载参考样本**: 读取 `.agent/skills/maglev-create-test-cases/examples/human_quality_example.md`。
   > _(Goal: 学习 Human QA 的颗粒度，特别是 UI 交互和边缘场景的描述)_

### 3. 初始化 WIP
使用模板 `test-case-template.md` 初始化 `{wipFile}`。
Frontmatter:
```yaml
---
title: '{title}'
source: '{input_file}'
status: 'in-progress'
stepsCompleted: [1]
---
```

### 4. 报告
向用户列出识别到的测试对象数量，并展示菜单：
"[C] 继续制定策略 (Step 2)"
"[A] 高级诱导"
