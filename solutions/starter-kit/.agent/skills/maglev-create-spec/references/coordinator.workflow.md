---
name: create-spec-coordinator
description: 协调器工作流，编排 Interview -> Ingest -> Draft -> Crystallize。(Deep Mode v2.0)
---

# Spec Coordinator Workflow (指挥官)


> **Role**: Product Architect (产品架构师)
> **Motto**: "先对齐，再动手。"

**目标**: 通过深度访谈与用户达成共识，再协调原子技能完成端到端 Spec 生成。

## 步骤序列

## 步骤序列

### Phase 00: Integrity Check (启动自检)
读取 `references/step-00-integrity-check.md`。
*   检查环境依赖和状态。
*   如果不通过，直接终止。

### Phase 0: Socratic Interview (苏格拉底式访谈) 🆕
读取 `references/step-00-socratic-interview.md`。
*   **强制性**: 除非用户明确说 "我已经想清楚了，直接开始"。
*   负责挖掘用户的隐性意图和未明假设。
*   产出: `clarified_context.md` (关键共识记录)。

### Phase 1: Ingest (摄入)
读取 `references/wrapper-01-ingest.md`。
*   负责与用户交互，确定 Intent 和 Source。
*   调用 `spec-ingest` 技能生成 Context。

### Phase 1.5: Validate (门禁)
读取 `references/wrapper-01b-validate.md`。
*   调用 `spec-validate-context` 技能。
*   如果校验失败，流程在此终止。

### Phase 2: Draft (起草)
读取 `references/wrapper-02-draft.md`。
*   调用 `spec-draft` 技能生成 Unified Draft。
*   (Checkpoint): 允许用户在这里暂停并修改 Draft。

### Phase 3: Crystallize (固化)
读取 `references/wrapper-03-crystallize.md`。
*   调用 `spec-crystallize` 技能完成拆分和存档。

### Phase 4: Verify (验证)
读取 `references/step-04-verify-output.md`。
*   验证产出的 Spec 文件和 Context 归档。
*   输出最终报告。

