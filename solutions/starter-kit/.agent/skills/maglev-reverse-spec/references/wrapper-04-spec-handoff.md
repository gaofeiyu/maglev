---
description: maglev-reverse-spec Step 4 - Handoff to Standard Draft Skill
---

# Step 4: Spec Handoff (规格交接)

## 目标
将逆向工程获取的碎片信息 (Facts)，转化为标准输入格式，并调用 `maglev-spec-draft` 技能生成符合 Maglev v2.0 标准的 Spec。

## 1. 整理 Facts
你需要将之前步骤 (Step 2, 3) 收集到的 Page Context 和 Backend Context 整理为 `input_facts.md`。

**Path**: `{project-root}/.maglev/temp/input_facts.md`

**Content Template**:
```markdown
# Reverse Engineered Facts

## User Intent & Hypotheses
Reverse Engineer feature: {Selection Name}
{Content from intent_context.md/Hypotheses}

## Unresolved Quests (Action Items)
{Content from intent_context.md/Quests}

## Frontend Facts
{Summary of content from Step 2 Page Analysis}

## Backend Facts
{Summary of content from Step 3 Stack Trace}

## Router/Structure
{Summary of Router Analysis}
```

## 2. 准备 Context
生成 `ingest_context.json` 以模拟 Ingest 技能的产出。

**Path**: `{project-root}/.maglev/temp/ingest_context.json`

```json
{
  "meta": {
    "intent": "Reverse Engineer {Selection}",
    "slug": "reverse_{selection_slug}",
    "type": "reverse-engineering"
  },
  "project": {
    "hasUI": {HasUI_Boolean} 
  }
}
```
> **注意**: `hasUI` 字段至关重要，它将触发 `maglev-spec-draft` 的 "Backend Bias Fix" 逻辑。

## 3. 调用 Draft 技能
调用子工作流 `maglev-spec-draft/references/step-02-polymorphic-design.md`。

> "现在，请作为架构师，基于上述 Facts 生成 Unified Draft。
>
> **Critical Instruction for Reverse Spec**:
> 由于逆向工程细节极多，为了避免丢分，**必须**使用 Smart Chunking 将设计拆分为：
> - `02_design_frontend.md` (详细记录组件/交互)
> - `02_design_backend.md` (详细记录接口/模型)
> - `02_design_core.md` (仅包含架构图和数据库ER图)"

## 4. 完成
Draft 完成后，进入 Standard Crystallize 流程 (Step 5)。
