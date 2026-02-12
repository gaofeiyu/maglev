---
name: maglev-spec-draft
description: (Atomic Skill) 负责读取标准化上下文，根据多态策略 (Frontend/Backend) 生成统一的 Spec 草稿 (`draft_unified.md`)。
---

# Maglev Spec Draft (起草者)

> **Motto**: "我是多态的建筑师。给我意图，还你蓝图。"

## 核心职责
作为 Spec 生成流水线的 **第二环**，本技能负责智力创造：
1.  **Polymorphism (多态适配)**: 根据输入类型动态调整设计章节 (`02_design.md`) 的内容结构。
    *   *Frontend*: 生成 Interaction Table (组件-交互-动作)。
    *   *Backend*: 生成 API Definition (Swagger) 和 Schema (SQL)。
2.  **Logic Synthesis (逻辑合成)**: 结合 `input_facts.md` (现状) 和 `intent` (目标)，推导具体的变更点。
3.  **Drafting (起草)**: 生成包含完整 00-03 章节的单一草稿文件。

## 输入 (Inputs)
*   **JSON Context**: `ingest_context.json` (来自 Ingest)
*   **Facts**: `input_facts.md` (来自 Ingest)
*   **Project Type**: (可选) 用户指定的前/后端类型。

## 输出 (Outputs)
*   **`draft_unified.md`**: 一个包含 Markdown 内容的临时文件。
*   *注意*: 此文件尚未物理拆分，仅用于中间流转。

## 必需的参考资料
*   工作流: `references/draft.workflow.md`
*   Step 1 (Context): `references/step-01-load-context.md`
*   Step 2 (Design): `references/step-02-polymorphic-design.md`
*   **Standards**:
    *   `solutions/templates/standards/protocol_spec_context.md`
    *   `solutions/templates/standards/template_00_index.md`
    *   `solutions/templates/standards/template_01_requirements.md`
    *   `solutions/templates/standards/template_02_design.md`
    *   `solutions/templates/standards/template_03_plan.md`
