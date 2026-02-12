---
name: maglev-standup
description: 每日站会 (Context Loader)。快速加载 Maglev 核心上下文，进入创造者模式。
---

# Maglev Standup (每日站会)

## 概览 (Overview)
专为 Maglev 创造者 (Creator) 设计的上下文加载器。
它模拟了 "Daily Standup" 的过程：快速回顾目前的战场地形、最近的战术决策和当天的行动清单。

## 为什么需要它？
Maglev 项目本身非常复杂，包含元范式、多层交付物和高度抽象的逻辑。
每次会话开始时，仅靠记忆很容易遗漏上下文。Standup 强制执行一次 "Context Injection"，确保 AI 与 Creator 同频。

## 核心能力 (Capabilities)
1.  **Space Sync**: 读取 `repository_map.md`，建立物理空间感知。
2.  **Mind Sync**: 读取 `docs/thinking/README.md`，对齐最近的架构决策。
3.  **Action Sync**: 读取 `task.md`，明确当前任务进度。

## 何时使用 (When to use)
- 每天第一次打开会话时 (输入 `/maglev-standup` 或 "Start Standup")。
- 感觉 AI "失忆" 或 "跑偏" 时。

## 交互示例
User: "Standup."
AI: "Morning, Creator.
[Space] 仓库结构正常，新增了 maglev-tutor。
[Mind] 昨天我们确定了 'Meta-Skill' 范式。
[Action] 今天待办：完成 Standup Skill 开发。
Ready to build?"
