---
description: maglev-create-prd Step 00 - Integrity Check
---

# Step 00: Integrity Check (启动自检)

## 目标
确保 PRD 生成所需的运行环境和依赖文件均已就绪。

## 自检列表

### 1. 环境准备
*   **Action**: 检查工作区根目录下的 `.maglev/temp` 目录。
*   **Logic**: 如果不存在，自动创建它。

### 2. 状态重置
*   **Action**: 清理 `.maglev/temp` 目录下的以 `prd_` 开头的临时文件。
*   **Reason**: 防止上一次任务的残留数据污染本次 PRD 生成。

### 3. 输出目录检查
*   **Action**: 检查 `docs/prd/` 目录是否存在。如果不存则创建。

## Checkpoint
如果上述检查全部通过，输出：
```
[CHECKPOINT - System Ready]
✅ 环境完整性检查通过。
- Temp Dir: OK
- Output Dir: OK
- Clean Slate: OK
```
否则，报错并中止。
