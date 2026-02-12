---
name: step-02-scaffold
description: 执行脚手架生成
---

# Step 2: Scaffold Generation (脚手架生成)

## 目标
根据 Step 1 收集的元数据，物理生成文件结构。

## 动作
1.  **Read Templates**: 读取 `references/template_*.md`。
2.  **Plan Paths**:
    *   Root: `{target_path}/{skill_name}/`
    *   Refs: `{target_path}/{skill_name}/references/`
3.  **Generate Entry**:
    *   Render `template_skill.md` -> `SKILL.md`
4.  **Generate Workflow**:
    *   Render `template_workflow.md` -> `references/{name}.workflow.md`
5.  **Generate Steps**:
    *   Loop through defined steps.
    *   Render `template_step.md` -> `references/step-XX-{name}.md`
    *   Ensure `next_step` chaining.

## 关键指令 (Directives)
-使用 `mkdir` 创建目录。
- 使用 `write_to_file` 创建文件。
- **Physical Copy**: 不要引用模板路径，而是将内容复制到新文件。

## 完成 (Finalize)
告知用户：
"Skill `{skill_name}` has been forged at `{target_path}`.
You can now edit `SKILL.md` to customize it."
