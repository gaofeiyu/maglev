---
name: maglev-spec-crystallize
description: (Atomic Skill) 负责将 Unified Draft 拆分为物理文件簇 (00-03)，并将 Input Facts 存档为 Context。
---

# Maglev Spec Crystallize (固化者)

> **Motto**: "我不做设计，我只负责刻碑。"

## 核心职责
作为 Spec 生成流水线的 **最后一环**，本技能负责物理交付：
1.  **File Splitting (物理拆分)**: 解析 `draft_unified.md` 的章节标记 (Headers)，将其分割写入 `specs/20_evolution/active/{slug}/` 下的 `00-03` 文件。
2.  **Context Persistence (基准存档)**: 将 `input_facts.md` 复制到 `context/` 子目录，建立验证基准。
3.  **Side Effects (副作用)**: 清理临时文件，更新项目索引。

## 输入 (Inputs)
*   **Draft**: `draft_unified.md` (包含完整内容的草稿)
*   **Facts**: `input_facts.md` (需要存档的事实)
*   **Slug**: 目标文件夹名称 (e.g., `user-vip-level`)

## 输出 (Outputs)
*   **Spec Cluster**:
    *   `00_index.md`
    *   `01_requirements.md`
    *   `02_design.md`
    *   `03_plan.md`
    *   `context/input_facts.md`

## 必需的参考资料
*   工作流: `references/crystallize.workflow.md`
*   Step 1 (Split): `references/step-01-split-files.md`
*   Step 2 (Finalize): `references/step-02-finalize.md`
