---
description: maglev-reverse-spec Step 00 - Integrity Check
---

# Step 00: Integrity Check (启动自检)

## 目标
确保逆向工程所需的运行环境和依赖技能均已就绪。

##自检列表

### 1. 环境准备
*   **Action**: 检查工作区根目录下的 `.maglev/temp` 目录。
*   **Logic**: 如果不存在，自动创建它。

### 2. 依赖技能检查
检查以下关键依赖是否存在：
1.  `maglev-spec-draft` (用于生成 Spec)
    *   Path: `../maglev-spec-draft/references/step-02-polymorphic-design.md`
2.  `maglev-spec-crystallize` (用于归档)
    *   Path: `../maglev-spec-crystallize/references/crystallize.workflow.md`

### 3. 状态重置
*   **Action**: 清理 `.maglev/temp/input_facts.md` 和 `.maglev/temp/draft_unified.md` (如果存在)。
*   **Reason**: 防止上一次任务的残留数据污染本次逆向。

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
