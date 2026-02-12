---
name: 'wrapper-03-crystallize'
description: '调用 maglev-spec-crystallize 技能'
sub_workflow: '../maglev-spec-crystallize/references/crystallize.workflow.md'
---

# Phase 3: Crystallize (固化)

## 指令

1.  **加载子技能**:
    读取并执行 `{sub_workflow}` 中的所有步骤。
    *   请完整执行 `split-files` 和 `finalize`。

2.  **任务完成**:
    向用户报告整个 Coordinator 流程已结束。所有资源已清理，产物已交付。
