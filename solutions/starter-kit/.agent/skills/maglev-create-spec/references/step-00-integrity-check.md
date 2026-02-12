---
description: maglev-create-spec Step 00 - Integrity Check
---

# Step 00: Integrity Check (启动自检)

## 目标
确保 Spec 生成所需的运行环境和依赖技能均已就绪。

## 自检列表

### 1. 环境准备
*   **Action**: 检查工作区根目录下的 `.maglev/temp` 目录。
*   **Logic**: 如果不存在，自动创建它。

### 2. 依赖技能检查
检查以下关键依赖是否存在：
1.  `maglev-spec-ingest` (用于信息摄入)
    *   Path: `../maglev-spec-ingest/references/ingest.workflow.md`
2.  `maglev-spec-draft` (用于生成 Spec)
    *   Path: `../maglev-spec-draft/references/step-02-polymorphic-design.md`
3.  `maglev-spec-crystallize` (用于归档)
    *   Path: `../maglev-spec-crystallize/references/crystallize.workflow.md`

### 3. 状态重置
*   **Action**: 清理 `.maglev/temp` 目录下的旧数据 (`draft_unified.md`, `input_facts.md`, `ingest_context.json`)。
*   **Reason**: 防止上一次任务的残留数据污染本次 Spec 生成。

## Checkpoint
如果上述检查全部通过，输出：
```
[CHECKPOINT - System Ready]
✅ 环境完整性检查通过。
- Temp Dir: OK
- Dependencies: OK
- Clean Slate: OK
```
否则，报错并中止。
