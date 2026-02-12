---
description: 召唤图书管理员整理项目索引 (Specs, Docs, Code)
---

# Maglev Librarian Update

此工作流用于唤醒项目的图书管理员 (Librarian)，自动扫描并更新各项资源的索引文件。

## 步骤

1. **唤醒管理员**
   使用 Skill `@maglev-librarian`。

   > **提示**: 管理员会询问您想要整理哪类资源：
   > *   **[A] Spec Curator**: 更新 `specs/README.md`
   > *   **[B] Thought Organizer**: 更新 `docs/thinking/README.md`
   > *   **[C] Cartographer**: 更新 `specs/10_reality/repository_map.md`
   > *   **[D] All**: 全部更新

2. **确认变更**
   管理员会直接修改 `.md` 文件。请在 Git 中查看 diff 并提交变更。
