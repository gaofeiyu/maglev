---
name: 'step-04-review'
description: '审查 Unified Draft 并拆分为标准文件簇'

workflow_path: '{project-root}/_bmad/bmm/workflows/bmad-quick-flow/quick-spec'
wipFile: '{implementation_artifacts}/tech-spec-wip.md'
---

# 步骤 4: 审查与定稿 (Review & Crystallize)

**进度：第 4 步，共 4 步** - 最后一步

## 指令序列

### 1. 展示统一草稿 (Unified Draft)
完整展示 `{wipFile}`，并特别提醒用户关注 **Structure** (00-03 章节是否清晰)。

展示菜单: `[C] 确认定稿 (Crystallize)   [E] 继续编辑   [M] Maglev Checklist`

### 2. Maglev 13-Point Checklist
(保持原有检查项，增加结构检查)
*   **Struct**: 是否包含 `01_requirements`, `02_design` 等所有必要章节？
*   **Visual**: 如果是前端项目，`02_design` 是否包含 Interaction Table？

### 3. 定稿与拆分 (Crystallization)

**当用户选择 [C] 时，执行以下物理操作：**

1.  **创建目录**:
    使用 `run_command` 创建目录: `{output_folder}/{slug}/`

2.  **拆分文件 (Split & Write)**:
    从 `{wipFile}` 中提取对应章节的内容，分别写入以下文件 (使用 `write_to_file`):
    *   `{output_folder}/{slug}/00_index.md` (提取 `## 00. 索引与元数据` 内容)
    *   `{output_folder}/{slug}/01_requirements.md` (提取 `## 01. 需求契约` 内容)
    *   `{output_folder}/{slug}/02_design.md` (提取 `## 02. 技术蓝图` 内容)
    *   `{output_folder}/{slug}/03_plan.md` (提取 `## 03. 实施计划` 内容)
    *   *提示*: 如果有 `assets` (图片链接)，请确保它们被正确保留或提示用户。

3.  **清理现场**:
    使用 `run_command` 删除临时草稿: `rm {wipFile}`

### 4. 退出
向用户报告：
"Spec Flag 已插上！🏁
文件簇已创建于: `{output_folder}/{slug}/`
- 📄 00_index.md
- 📄 01_requirements.md
- 📄 02_design.md
- 📄 03_plan.md
"
