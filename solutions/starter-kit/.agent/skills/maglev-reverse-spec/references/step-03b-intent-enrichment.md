---
description: maglev-reverse-spec Step 3b - Intent Speculation & Quests
---

# Step 3b: Intent Speculation (意图推测)

## 目标
弥补逆向工程的 "Quality Gap"。不仅仅翻译代码 (What)，更要推测背后的业务意图 (Why)。

## 执行逻辑

### 1. 侦探推理 (Sherlock Strategy)
分析 Step 3 产生的 Backend Context，寻找以下线索：
*   **Magic Numbers**: 硬编码的数字 (e.g., `0.15`, `Status == 9`).
*   **Complex Logic**: 复杂的校验、分支 (e.g., "Triple nested if").
*   **Naming Hints**: 具有业务含义的命名 (e.g., `isVIP`, `anti_fraud`).

### 2. 假设生成 (Hypothesis Generation)
基于线索生成假设：
*   *"校验逻辑可能是为了防止库存超卖。"*
*   *"硬编码 0.15 可能是当年的增值税率。"*

### 3. 用户交互 (Interactive Verification)
向用户展示假设，并生成 **[Quest List]**:

> "🕵️ **Intent Analysis Complete**
>
> 我发现了一些关键逻辑，推测如下：
> 1. `checkStock()`: 包含复杂的锁机制 -> **Hypothesis**: 防止高并发超卖。
> 2. `tax_rate = 0.15`: 硬编码 -> **Quest**: 这是哪里的税率？
>
> **您的指令**:
> - **[C]onfirm**: 同意所有假设，不知道Quest答案 (保留为 TODO)。
> - **[E]dit**: 我来补充/纠正某些点。
> - **[S]kip**: 不关心，直接生成 Spec。"

## Output Structure
生成 `intent_context.md`:

```markdown
# Intent Context

## Hypotheses (Confirmed)
- Locking mechanism is for high-concurrency overselling protection.

## Unresolved Quests (To-Do)
- [ ] What does `Status == 9` mean?
- [ ] Confirm valid region for `tax_rate = 0.15`.
```
