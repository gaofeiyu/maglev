---
name: 'step-03-generate-cases'
description: '生成具体测试用例'
workflow_path: '{project-root}/.agent/skills/maglev-create-test-cases/references/create-test-cases.workflow.md'
nextStepFile: './step-04-review-finalize.md'
wipFile: '{project-root}/specs/20_evolution/active/test_cases/test-plan-wip.md'
---

# 步骤 3: 生成测试用例

**目标**: 编写具体的 Markdown 测试用例表。

## 指令序列

### 1. 加载 WIP
读取 `{wipFile}`。

### 2. 生成用例
### 2. 生成用例 (Reasoning Enhanced)

**Phase 1: 用户旅程模拟 (Persona CoT)**
"作为 [Persona, e.g., 运营人员]，在 [Context, e.g., 网络不佳] 的情况下，我想要 [Action]，我期待 [Result]..."
- 关注: **UI 交互细节** (Toast, Loading, Disabled State), **隐性规则** (自动过滤, 默认值).

**Phase 2: 对抗性生成 (Adversarial Critique)**
自我提问:
- "如果数据是空的怎么办？"
- "如果两个用户同时操作怎么办？"
- "如果必填项根据某个开关动态变化怎么办？"
-> 生成对应的 **Negative Path** 和 **Boundary** 用例。

**Phase 3: 生成列表**
遍历所有 AC 并结合上述推理：
1. **Happy Path**: 正常流程 + UI 反馈。
2. **Negative Path**: 错误输入，异常状态 + 友好的错误提示。
3. **Boundary**: 边界值。
4. **UI States**: Loading, Empty, Error (Frontend).
5. **Interactions**: Click, Input, Scroll (Frontend).
6. **Security**: 权限校验。

**Format Constraint**: 必须使用 Markdown Table。
(ID, Priority, Title, Pre-condition, Steps, Expected Result).

### 3. 更新 WIP
填充 "2. 测试用例列表" 章节。
更新 `stepsCompleted: [1, 2, 3]`。

### 4. 报告
"已生成 {count} 个测试用例。"
展示菜单:
"[C] 审查与定稿 (Step 4)"
