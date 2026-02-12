---
name: maglev_archival_check
description: 交互式归档审查工具，作为 Quality Gate 确保每次任务结束前的知识沉淀和状态一致性。
---

# 归档审查 (Archival Check)

## 概览 (Overview)
本 Skill 数字化了 `standards/archival_checklist.md`，强制执行项目归档标准。
它不直接修改代码，而是作为 **Gatekeeper (守门人)**，引导用户或自动检查任务的完整性。

## 何时使用 (When to use)
- **任务结束时**: 用户说 "任务完成了", "归档", "Close task"。
- **状态不确定时**: 想要检查当前工作流是否遗漏了文档更新。
- **提交代码前**: 确保 Changelog 和 Contribution Log 已更新。

## 交互模式 (Interaction)
Skill 会扮演 **[Quality Assurance]** 角色，逐一核对必须的归档项：
1.  **Thinking**: 有新的想法记录吗？
2.  **Solutions**: 方案文档是否已落地？
3.  **Contributors**: `contribution_log.md` 是否更新？ (Blocker)
    - **Rule**: 必须插入到表格第一行 (最新在前)。
4.  **Skills**: 是否有新技能产生？

## 参考资料 (References)
- 工作流入口: `references/archival-check.workflow.md`
- 审查清单: `references/checklist.md`
- 审计步骤: `references/step-01-audit.md`
