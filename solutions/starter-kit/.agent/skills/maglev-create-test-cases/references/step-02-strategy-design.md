---
name: 'step-02-strategy-design'
description: '设计测试策略 (Pyramid)'
workflow_path: '{project-root}/.agent/skills/maglev-create-test-cases/references/create-test-cases.workflow.md'
nextStepFile: './step-03-generate-cases.md'
wipFile: '{project-root}/specs/20_evolution/active/test_cases/test-plan-wip.md'
---

# 步骤 2: 策略设计

**目标**: 确定每个测试对象的层级 (Unit vs Integration vs E2E)。

## 指令序列

### 1. 加载 WIP
读取 `{wipFile}`。

### 2. 定义策略
应用测试金字塔原则 (Backend & Frontend)：

**Backend**:
- **Logic Intensive**: Unit Test (JUnit/PyTest).
- **Data Flow / API**: Integration Test.
- **System Flow**: E2E Test.

**Frontend**:
- **Component Logic**: Unit Test (Vitest/Jest).
- **UI Interaction**: Component Test (Vue Test Utils / Standard).
- **User Journey**: E2E Test (Playwright/Cypress).

### 3. 更新 WIP
在模板的 "1. 测试策略" 章节填入表格。

### 4. 报告
展示策略摘要。
展示菜单:
"[C] 开始生成用例 (Step 3)"
"[P] 派对模式 (咨询 QA 专家)"
