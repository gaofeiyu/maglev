# Layered Spec Implementation Plan (显性分层实施计划)

## 1. 核心标准定义 (The Standard)
所有的 Maglev 生成文档 (PRD/Spec) 必须遵循 **"Three-Zone Architecture" (三区架构)**：

### Zone 1: The Executive Brief (决策层/人读区)
*   **Audience**: 产品经理, Tech Lead, 业务方。
*   **Content**: 
    *   **TL;DR**: 一句话讲清楚要做什么。
    *   **Decision**: 核心决策与权衡 (Trade-off)。
    *   **Risk**: 显性风险 (Security, Performance, Debt)。
*   **Format**: 纯自然语言，禁止堆砌代码细节。
*   **Marker**: `> 👤 **Executive Brief**`

### Zone 2: The Logic Core (执行层/人机共读区)
*   **Audience**: 开发人员, 测试人员, AI。
*   **Content**: 
    *   User Stories / AC。
    *   API Definition / Database Schema。
    *   Flowcharts (Mermaid)。
*   **Format**: 结构化 Markdown，图文并茂。

### Zone 3: The Context Dungeon (上下文层/机读区)
*   **Audience**: AI (for Context Restoration), 考古人员。
*   **Content**: 
    *   原始 Prompt 片段。
    *   过长的思维链 (Chain of Thought)。
    *   引用素材片段。
*   **Format**: 必须使用 `<details>` 标签折叠，或置于 `## Appendix`。
*   **Marker**: `> 🤖 **Context Dump**`

## 2. 实施步骤 (Implementation Steps)

### Step 1: Update `maglev-spec-draft`
*   **Target**: `solutions/starter-kit/.agent/skills/maglev-spec-draft/references/step-02-polymorphic-design.md`
*   **Action**: 修改 Prompt，强制要求在生成的 `01_requirements.md` 和 `02_design.md` 中应用上述分层结构。
    *   *Instruction*: "For `01_requirements.md`, you MUST start with an 'Executive Brief' section..."

### Step 2: Update `maglev-create-prd`
*   **Target**: `solutions/starter-kit/.agent/skills/maglev-create-prd/references/step-02-write-prd.md` (需确认具体文件)。
*   **Action**: 同样强制 PRD 遵循分层结构。

### Step 3: Validation
*   生成一个由 AI 编写的 Spec 样例，检查是否符合分层结果。

## 3. 模板变更示例 (Template Change)

```markdown
<!-- FILE: 01_requirements.md -->

> 👤 **Executive Brief**
> 本次迭代旨在解决 X 问题。核心决策是采用 Y 方案，以换取 Z 性能。
> ⚠️ **Risk**: 必须注意兼容老数据。

# 1. User Stories
...

<details>
<summary>🤖 Context Trace</summary>
(Original Context JSON or Thinking Process)
</details>
```
