# 协作准则 (Collaboration Conventions)

为了实现B端项目开发方式的重构与效率质量的飞跃，本项目遵循以下核心协作准则：

## 1. 目录用途约定
- **solutions/**: 用于存放经过深思熟虑、具备可落地性的最终方案文档。
- **thinking/**: 用于记录探索过程中的思考路径、草稿和头脑风暴内容，保留思维火花。
- **archive/**: 用于归档废弃的方案、不再适用的历史记录，确保项目历史可追溯但不干扰当前工作。
- **contributors/**: 专门用于记录项目内容的贡献来源（人/AI）。
- **standards/**: 存放项目的所有准则、约定和规范（包括本文档）。

## 2. 贡献者记录 (Contributor Logging)
为了更公平地界定人类与 AI 在项目中的价值，我们废弃了单纯的“工作量比例”，采用 **双维度评价体系**：

- **意图主导 (Intent Driver)**: 谁定义了“做什么”？谁提供了关键的决策、灵感或约束？（通常由 Human 主导）
- **执行载体 (Execution Carrier)**: 谁完成了“怎么做”？谁承担了主要的文档编写、代码生成或数据整理工作？（通常由 AI 主导）

在 `contributors/contribution_log.md` 中，应明确记录这两个维度，而非简单的百分比。
- **[必填] Human Prompt Summary**: 必须记录人类给出的关键 Prompt，以便他人复用这种“意图注入”的模式。

## 3. 产物关联性 (Artifact Linkage)
- 文档之间必须建立正确的关联（Hyperlinks）。
- AI与人类应能通过文档中的链接清晰地找到上下文脉络，避免形成信息孤岛。

## 4. 准则的存储与更新
- 本准则及后续所有达成的约定，都必须直接存储在 `standards/` 目录下。
- 准则是活的文档，应随着项目的进展不断迭代更新。

## 5. 语言规范
- **所有产出的 Artifacts (包括 Task 列表, Implementation Plan, Walkthrough, 以及项目内的文档)** 必须以 **中文** 形式呈现。

## 6. 参考资料归档策略 (Reference Archiving Strategy)
为了保持知识的系统化沉淀，`references/` 目录遵循以下归档策略：

- **子目录分类**：资料必须按类型存入相应的子目录：
    - `references/papers/`: 学术论文 (建议命名: `YYYY-Title.pdf`)
    - `references/articles/`: 博客文章、深度好文 (建议以 Markdown 记录链接、摘要和推荐理由)
    - `references/tools/`: 实用工具、库的介绍或配置文件
    - `references/prompts/`: 值得学习的外部高效 Prompt 案例
- **摘要要求**：对于链接型或长篇资料，必须创建一个同名 Markdown 文件，包含：
    - **来源链接**
    - **推荐理由**
    - **核心摘要/关键点**
- **命名规范**：文件名应清晰、具备语义，尽量包含年份或关键主题词。

## 7. 范式定义归档 (Paradigm Definitions)
- **paradigms/**: 专门用于存储新旧范式的对比分析、角色演变定义及工作流图示。任何关于“我们如何工作”的元思考，都应沉淀于此。

## 8. 归档审查机制 (Archival Review)
- 为了确保知识不流失，每次重要沟通或任务块结束前，**必须执行 [standards/archival_checklist.md](archival_checklist.md) 中的自查流程**。
- 这是一道“防呆”工序，确保所有思考、方案、引用都各归其位。

## 9. AI 技能维护 (AI Skill Maintenance)
- **沉淀即技能 (Codify as Skill)**: 任何被验证有效、可重复的流程或知识（即进入 `solutions/` 的内容），都应尝试封装为 AI Skill (in `.agent/skills/`)。这能让未来的 AI Agent 直接调用这些能力，实现“仓库自我进化”。
- **同步更新 (Sync Update)**: 当核心文档（如流程图、角色定义）发生变更时，**必须**检查并更新引用了该文档的 Skill，确保 AI 获取的 Context 是最新的。

## 10. 统一意图流 (Unified Intent Stream)
所有工作意图（Feature/Bug/Refactor）必须统一收敛至 `issues/` 目录。
- **Physical**: `issues/active/` 是单一入口。
- **Logical**: 区分 **Evolution** (演进) 与 **Correction** (修正) 双流路由。
- **Visual**: 必须维护 `issues/README.md` 作为 **"战术仪表盘 (Dashboard)"**，防止任务迷失。

## 11. 上下文感知机制 (Context Awareness)
为了提升 AI 的协作效率，建议在项目根目录配置 `.maglev/user.yaml`。
- **User Profile**: 定义当前用户的角色 (Role) 和关注点 (Focus)。
- **AI Behavior**: AI 应在会话启动时主动读取此配置，并调整其 Context 加载策略。

## 12. 知识园艺 (Knowledge Gardening)

为了防止文档膨胀 (Bloat)，我们执行严格的 **"Unlinked Draft Policy" (无链即废)**。

### 10.1 这里的 Thinking 为什么保留？
`thinking/` 目录下的文档不仅仅是过程草稿，它们是 **"Decision Records" (决策履历)**。
只有当一份 Thinking 文档具有长期的 **"Contextual Value" (解释为什么要这样做)** 时，才会被保留。
- **保留标准**: 被 `solutions/maglev_methodology_index.md` 显式索引。
- **归档标准**: 未被索引的孤儿文档，视为已固化为 Solution 或废弃，应移入 `archive/thinking/`。

### 10.2 定期修剪 (Pruning Routine)
- **触发时机**: 每周或里程碑结束时。
- **Action**: 扫描 `thinking/` 目录，将未被 Index 引用的文件移入 `archive/`。
