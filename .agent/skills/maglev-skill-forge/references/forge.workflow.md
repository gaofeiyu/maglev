---
name: forge
description: Maglev Skill 制造工厂
output_folder: .agent/skills
step_design: references/step-01-design.md
step_scaffold: references/step-02-scaffold.md
---

# Skill Forge Workflow

**Goal**: 制造 Skill。

## 流程 (Process)

### 1. Design (设计)
- 访谈用户，确定 Skill 的三要素：
    - **Trigger**: 这个技能在什么场景下被触发？(When to use)
    - **Workflow**: 需要哪些步骤？(Steps)
    - **Context**: 作用域是哪里？(Project vs StarterKit)

### 2. Scaffold (脚手架)
- 基于设计，自动生成文件。
- **Inputs**:
    - `{{skill_name}}`
    - `{{description}}`
    - `{{steps}}` (List)
- **Outputs**:
    - `SKILL.md`
    - `references/*.md`

### 3. Verify (验证)
- 检查生成的文件是否完整。
