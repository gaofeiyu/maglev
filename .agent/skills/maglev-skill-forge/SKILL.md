---
name: maglev-skill-forge
description: Maglev Skill 孵化器 - 通过交互式工作流快速生成符合 "Workflow-Driven Step Architecture" 的新技能。
---

# Skill Forge (技能熔炉)

## 概览 (Overview)
这是一个 **Meta-Skill** (元技能)。它封装了 Maglev 标准的技能设计模式 (Workflow + Micro-Steps + Isolation)，帮助用户快速将想法转化为可执行的 AI 技能。

## 何时使用 (When to use)
- 想要创建一个新 Skill 时。
- 想要标准化现有 Skill 的结构时。
- 只有想法，不知道如何拆解为步骤时。

## 交互模式 (Interaction)
Forge 扮演 **[Architect]** 角色，引导你完成设计：
1.  **Define**: 技能叫什么？解决什么问题？
2.  **Design**: 需要哪些步骤？(e.g., Load Config -> Scan Code -> Generate Report)
3.  **Scaffold**: 自动生成所有 Markdown 文件和目录结构。

## 必需的参考资料 (References)
- 工作流入口: `references/forge.workflow.md`
- 设计步骤: `references/step-01-design.md`
- 脚手架步骤: `references/step-02-scaffold.md`
- 模板:
    - `references/template_skill.md`
    - `references/template_workflow.md`
    - `references/template_step.md`

## 快速参考
- **Pattern**: Entry -> Workflow -> Micro-Steps
- **Isolation**: 所有引用资源必须在 `references/` 下。

## 示例
User: "我想做一个自动写 SQL 的技能。"
AI: "收到。启动 Skill Forge。请问这个技能的目标目录是 Project Internal (.agent/skills) 还是 Starter Kit (solutions/...)?"
