---
name: step-01-sync
description: 同步上下文
---

# Step 1: Sync (全域同步)

## 目标
读取关键状态文件，向 Creator 汇报当前项目状态。

## 动作
1.  **Read Files**: 使用 `view_file` 读取以下文件 (只读头部或关键部分以节省 Token)：
    *   `repository_map.md` (前 50 行) -> 确认物理结构。
    *   `docs/thinking/README.md` (前 50 行) -> 确认决策流。
    *   `task.md` (活跃任务区域) -> 确认进度。

2.  **Report**: 基于读取内容，输出 **"Maglev Daily Brief"**:
    *   **🧩 Topology**: 简述当前核心模块 (e.g., "Skills: 5 active, Solutions: 3 guides").
    *   **🧠 Context**: 复述最近的一条决策 (e.g., "Last thought: Meta Paradigm Analysis").
    *   **⚡ Focus**: 列出当前正在进行 (`[/]`) 的任务。

3.  **Ready**:
    *   结束语: "System Online. Awaiting command."

## 示例输出
```text
# ☀️ Maglev Daily Brief

**🧩 Topology Status**
- Core: Healthy (Thinking, Solutions, Src detected).
- Newest Asset: maglev-tutor (Skill).

**🧠 Decision Context**
- Focus: "Meta-Skill" & "Contributor Onboarding".
- Recent: 2026-01-31 Deploy Maglev Tutor.

**⚡ Action Items**
- [/] Create Maglev Standup Skill
- [ ] Refactor...

**System Ready. What's next?**
```
