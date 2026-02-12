# Documentation Update Plan (文档更新计划)

## 1. 核心概念阐述 (Core Concepts)
在 `solutions/starter-kit/README.md` 中增加一个清晰的章节，解释 **Skills** 与 **Workflows** 的关系。

**草稿内容**:
> ### 🧩 核心概念: Skills vs Workflows
> *   **Skills (技能)**: Maglev 的"原子能力"。它们存在于 `.agent/skills`，包含复杂的 Prompt 和执行逻辑 (如 `maglev-create-prd`)。虽然可以直接调用，但名字难记。
> *   **Workflows (工作流)**: 技能的"快捷方式"。它们存在于 `.agent/workflows`，通常以 `/` 开头。它们将复杂的技能调用封装为简单的指令 (如 `/create-prd`)。
>
> **最佳实践**: 推荐优先使用 Workflows (Slash Commands) 进行交互。

## 2. README 更新
*   在 `Interaction Guide` 上方或下方插入上述概念。
*   保持之前的 `Slash Command` 表格不变，但增加一句："这些指令本质上是调用了后台的 Maglev Skills。"

## 3. Init Guide 更新
*   检查 `maglev_init_guide.md`，确保它引导用户复制 `.agent/workflows` 目录 (之前只强调了 `.agent/skills`?)。
*   *Check*: `maglev_init_guide.md` 原文提到 "将 `.agent/` 目录完整复制到项目根目录"，这已经涵盖了 workflows。无需大改，只需在说明中提一下 Workflows 的重要性。

## 执行步骤
1.  修改 `solutions/starter-kit/README.md`。
2.  (可选) 微调 `solutions/starter-kit/maglev_init_guide.md`。
