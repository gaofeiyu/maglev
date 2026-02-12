---
name: 'step-04-review-finalize'
description: '审查与定稿'
workflow_path: '{project-root}/.agent/skills/maglev-create-test-cases/references/create-test-cases.workflow.md'
wipFile: '{project-root}/specs/20_evolution/active/test_cases/test-plan-wip.md'
---

# 步骤 4: 审查与定稿

**目标**: 确保测试计划无遗漏并归档。

## 指令序列

### 1. 完整展示
读取 `{wipFile}` 并向用户展示全文（或摘要）。

### 2. 展示菜单
"[C] 确认定稿 (Finalize)"
"[R] 对抗性审查 (Simulate Attacks)"
"[E] 编辑"

#### 逻辑:
- [R]: 模拟攻击者视角，寻找逻辑漏洞，若发现则自动补充 TC。
- [C]: 进入定稿流程。

### 3. 定稿 (Finalize)
1. 将 `{wipFile}` 重命名为 `{project-root}/specs/20_evolution/active/test_cases/test-plan-{slug}.md`。
2. 更新 Frontmatter `status: active`。
3. 宣布完成。
