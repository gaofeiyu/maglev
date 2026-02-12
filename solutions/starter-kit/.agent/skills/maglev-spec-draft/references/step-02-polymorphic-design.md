---
name: 'step-02-polymorphic-design'
description: '读取标准模板，生成 Unified Draft'
---

# 步骤 2: 多态设计与起草 (Polymorphic Design & Drafting)

## 0. 加载上下文
*   **Context**: 读取 `{project-root}/.maglev/temp/ingest_context.json`。
*   **Facts**: 读取 `{project-root}/.maglev/temp/input_facts.md` (或 Draft 阶段已加载的 Context)。
*   **Standards**:
    *   读取 `references/templates/zone-template-00-index.md`
    *   读取 `references/templates/zone-template-01-requirements.md`
    *   读取 `references/templates/zone-template-02-design.md`
    *   读取 `references/templates/zone-template-03-plan.md` (Self-generate if missing)

## 1. 核心指令 (Core Instruction)
你需要扮演一位 **Maglev 架构师**。
根据 `input_facts` (现状) 和 `context.meta.intent` (目标)，填充上述 4 个标准模板。
将 4 个文件的内容合并输出到 `{output_draft}`。

## 2. 格式要求 (Critical Output Format)
为了让下游的 Crystallize 技能能够正确拆分文件，你必须在每个文件的开头添加特殊的 **分界标记**。

**输出格式示例**:

```markdown
<!-- FILE: 00_index.md -->
{content of 00_index based on template}

<!-- FILE: 01_requirements.md -->
{content of 01_requirements based on template}

<!-- FILE: 02_design.md -->
{content of 02_design based on template}
...
```

## 3. 填充指南 (Filling Guide)

### 🧩 Smart Chunking Strategy (智能分片) [CRITICAL]
为了避免单文件过大导致的信息丢失，当满足以下任一条件时，**必须**将文件拆分为多个物理模块：
1.  **Volume**: 预估内容超过 500 行。
2.  **Complexity**: 涉及 >2 个独立的业务领域 (Domain)。

**命名规范**:
*   `01_requirements_core.md` (核心流程)
*   `01_requirements_{module}.md` (子模块)
*   `02_design_core.md` (架构决策)
*   `02_design_frontend.md` (前端详情 - when complex) 🆕
*   `02_design_backend.md` (后端详情 - when complex) 🆕
*   `02_design_{module}.md` (垂直拆分)

---

### 🌟 三区架构 (Three-Zone Architecture) [CRITICAL]
所有文档 (01, 02) 必须遵循以下分层结构，以解决 "双视困境"：

1.  **Zone 1: Executive Brief (决策层)**
    *   **位置**: 文件顶部。
    *   **标记**: `> 👤 **Executive Brief**`
    *   **内容**: 人话摘要。一句话讲清"做什么"、"核心Trade-off" 和 "显性风险"。禁止堆砌技术细节。
    *   *Interaction*: "Imagine you are briefing the CTO in an elevator."

2.  **Zone 2: The Logic Core (执行层)**
    *   **位置**: 正文区域。
    *   **内容**: 详细的 User Stories, AC, API Definition, Diagrams。

3.  **Zone 3: The Context Dungeon (上下文层)**
    *   **位置**: 文件底部或附录。
    *   **标记**: 使用 `<details><summary>🤖 Context Trace</summary>...` 折叠。
    *   **内容**: 原始 Thinking Chain, 引用片段。

### File 00: Index
*   **Title**: 使用 `context.meta.slug` 和合适的 Emoji。
*   **Status**: 设置为 `Draft`。
*   **Navigation**: **必须动态列出所有生成的文件** (包括拆分后的模块)。
    *   Example:
        *   [Requirements (Core)](01_requirements_core.md)
        *   [Requirements (Admin)](01_requirements_admin.md)

### File 01: Requirements
*   **Zone 1**: Summary + Key Risks.
*   **Zone 2**:
    *   **OpenSpec (Requirements)**: 将 User Stories 转化为更严谨的 `Requirement` -> `Scenario` -> `Gherkin` 格式。
    *   **Quest List**: 保留并填充 `Unresolved Questions`。
    *   **Out of Scope**: 必须明确什么不做。
*   **Zone 3**: Context linkage.

### File 02: Design (Polymorphic)
*   **Zone 1**: Architecture Verdict (e.g., "Extending table X vs New Service Y").
*   **Zone 2**:
    *   **Backend**: SQL Schema & API Interface.
    *   **Frontend (Conditional)**:
        *   *If Has UI*: 必须包含 Visual Anchor (Wireframe description) + Component Tree + State Logic。
        *   *If Headless*: 明确标注 "Frontend: N/A (Headless / API Service)"。
*   **Zone 3**: Reasoning process.

### File 03: Plan
*   **Atomic Steps**: 将 Design 拆解为带 Verification 的具体步骤。
