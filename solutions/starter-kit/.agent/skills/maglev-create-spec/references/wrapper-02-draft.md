---
name: 'wrapper-02-draft'
description: '调用 maglev-spec-draft 技能'
sub_workflow: '../maglev-spec-draft/references/draft.workflow.md'
nextStepFile: './wrapper-03-crystallize.md'
draft_file: '{project-root}/.maglev/temp/draft_unified.md'
---

# Phase 2: Draft (起草)

## 指令

1.  **加载子技能**:
    读取并执行 `{sub_workflow}` 中的所有步骤。
    *   请完整执行 `load-context` 和 `polymorphic-design`。

2.  **Human-in-the-Loop (人工审查)**:
    在 Draft 生成后，向用户展示文件路径：`{draft_file}`。

    **询问用户**:
    "Unified Draft 已生成！请使用编辑器打开查看。
    您想：
    1. **直接因化 (Proceed)**: 我将为您拆分文件。
    2. **手动修改 (Edit)**: 您修改 Draft 后，我再拆分。
    3. **重新生成 (Retry)**: 重新运行 Draft 步骤。"

3.  **前进**:
    如果用户选择 1 或 2，加载 `{nextStepFile}` 进入 Phase 3。
