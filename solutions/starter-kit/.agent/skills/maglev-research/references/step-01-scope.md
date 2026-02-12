---
name: step-01-scope
description: 定义调研范围与假设挑战 (Deep Mode v2.0)
next_step: references/step-02-search.md
---

# Step 1: Scope (定义范围) - Deep Mode 🆕

> **Role**: Research Lead (调研负责人)

## 目标
防止"漫无目的的搜索"。明确我们到底想知道什么。
**Deep Mode**: 在搜索前，先挑战用户的隐性假设。

## 动作

### 1. Topic (主题)
询问用户调研主题。

### 2. Questions (关键问题)
引导用户列出 3-5 个关键问题 (KQs)。
*   *Bad*: "查一下 Next.js"
*   *Good*: "Next.js 15 的 App Router 相比 Pages Router 有哪些性能提升？社区反馈主要由于什么问题？"

### 3. Hypothesis Challenge (假设挑战) 🆕
**在搜索前，主动挑战用户的隐性假设**：

> **[RESEARCH CHECKPOINT]**
> 
> 在开始搜索之前，我想和你确认几个问题：
> 
> 1. "你希望这个调研得出什么结论？"
>    - (识别预设答案)
> 
> 2. "如果调研结果和你的预期完全相反，你会怎么办？"
>    - (测试开放程度)
> 
> 3. "这个问题的答案，是要帮你做什么决策？"
>    - (明确调研目的)
> 
> 4. "有没有可能，你问的问题本身就是错的？"
>    - (重构问题)

### 4. Slug (文件名)
确定文件名 slug (e.g. `nextjs-15-analysis`)。

## 检查点
*   [ ] KQs 是否清晰、可回答。
*   [ ] 是否识别并记录了用户的预设假设。🆕
*   [ ] 调研目的 (决策点) 是否明确。🆕
*   [ ] 假设日志已更新到 `./00_context.md` 🆕

---

## 上下文交接 (Context Handoff) 🆕

### 读取已有上下文
技能启动时，先检查 `./00_context.md` 是否存在：
```
IF ./00_context.md 存在 AND 包含 Problem Statement THEN
    展示: "根据已有上下文，调研目的是 [Statement]。是否需要修改？[Y/n]"
```

### 写入假设日志
将挑战的假设 **Append** 到共享上下文：

```markdown
## 假设日志 (Assumptions Log)
<!-- research 填充 -->
| 假设 | 状态 | 来源 |
|------|------|------|
| {用户的预设假设} | Confirmed/Challenged | research |
```

> **注意**: 使用相对路径 `./00_context.md`，不要暴露本地绝对路径。

