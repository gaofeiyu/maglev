---
name: step-01-design
description: 交互式技能设计
next_step: references/step-02-scaffold.md
---

# Step 1: Skill Design (技能设计)

## 目标
通过访谈明确新 Skill 的核心要素，为脚手架生成提供元数据。

## 动作
1.  **Ask Name**: "给这个新技能取个名字 (e.g., `maglev-sql-writer`)。"
2.  **Ask Goal**: "它解决什么问题？(One line description)"
3.  **Ask Steps**: "它的大致执行步骤是什么？(e.g., 1. Connect DB, 2. Get Schema, 3. Write SQL)"
    *   *AI Hint*: 引导用户拆分为 3-5 个 Micro-Steps。
4.  **Confirm Context**: "它是项目专用的 (.agent/skills) 还是 Starter Kit 产品的一部分 (solutions/...)?"

## 交互示例
AI: "启动 Forge。First, what's the name of the new skill?"
User: "maglev-sql-bot"
AI: "Understood. What is its primary goal?"
...
AI: "Summary:
- Name: `maglev-sql-bot`
- Goal: `Auto-generate SQL based on schema`
- Steps: [`connect`, `scan`, `generate`]
- Path: `.agent/skills/`
Ready to scaffold?"

## 输出
在 Context 中生成 `skill_metadata` 对象。
