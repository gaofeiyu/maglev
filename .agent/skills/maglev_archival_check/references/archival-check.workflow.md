---
name: archival-check
description: 执行归档审查清单
output_folder: .
checklist: references/checklist.md
step_audit: references/step-01-audit.md
---

# 归档审查工作流 (Archival Check Workflow)

> **Goal**: 确保每一次迭代都完美收尾 ("Finish Strong")。

## 流程 (Process)

此工作流执行单一但关键的审计步骤。

### 1. 加载配置
- 语言: Chinese (Simplified)
- 角色: Quality Assurance / Custodian

### 2. 执行审计
- 读取 `{checklist}` 作为审计标准。
- 执行 `{step_audit}` 进行交互式核查。

### 3. 收尾
- 如果发现 Blocker (如 Log 未更新)，必须阻止归档直到修复。
- 输出最终的 "Ready to Archive" 确认。
