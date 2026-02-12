---
name: {{workflow_name}}
description: {{description}}
output_folder: {{output_folder}}
---

# {{workflow_name_human_readable}} Workflow

**Goal**: {{goal}}

## 流程 (Process)

{{process_description}}

## 步骤架构
- **Micro-Steps**: 严格遵循 `step-*.md`。
- **Isolation**: 内存中只加载当前步骤。

## 初始化
1. 阅读 `{{first_step}}`。
