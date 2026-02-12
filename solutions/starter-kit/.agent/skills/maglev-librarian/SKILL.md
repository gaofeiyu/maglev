---
name: maglev-librarian
description: 项目的“图书管理员”，负责扫描项目资产并生成/更新索引文件。
---

# Maglev Books & Librarian (图书管理员)

## 概览
`maglev-librarian` 是项目的知识管家。它不生产内容，只负责整理内容。
它通过扫描 `solutions/`, `docs/thinking/`, `code_storages/` 等目录，自动生成 README 索引，维护项目知识的“可发现性” (Discoverability)。

## 主要能力 (Tracks)
1.  **Spec Curator**: 整理 `solutions/` (Products)，生成 StarterKit-Guides-Skills 层级视图。
2.  **Thought Organizer**: 整理 `docs/thinking/`，按时间或主题聚类决策记录。
3.  **Cartographer**: 绘制 **代码仓库 (.)** 地图，更新 `repository_map.md`。

## 何时使用
- 用户要求“整理文档”、“更新索引”或“生成目录”。
- 在大型变更后，需要重新梳理项目结构时。
- 想要了解当前有哪些 Specs 处于 Active 状态时。

## 交互规则
- **Language**: 所有生成的索引文件头部描述、章节标题必须使用 **中文**。
- **Action-Oriented**: 不要只列出清单，通过 File Edit 实际更新 `README.md` 文件。
- **Metadata-Aware**: 解析文件的 YAML Frontmatter (title, status, slug) 来丰富索引信息。
- **Non-Destructive**: 更新索引时保留用户手写的 Context 区域（如果模板支持）。

## 必需的参考资料
- 工作流入口: `references/librarian.workflow.md`
- Track A (Spec): `references/track-spec-curator.md`
- Track B (Thought): `references/track-thought-organizer.md`
- Track C (Repo): `references/track-cartographer.md`
- 模板: `references/template-index-page.md`
