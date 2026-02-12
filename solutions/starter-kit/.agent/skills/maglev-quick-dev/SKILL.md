---
name: maglev-quick-dev
description: 当运行 Maglev quick-dev 工作流以通过自检和对抗性审查步骤快速实施小的变更时使用。
---

# 快速开发 (Quick Dev)

## 概述
运行 quick-dev 工作流以快速实施小的变更。严格遵循步骤文件，并在指示时运行对抗性审查。

## 何时使用
- 用户要求运行 quick-dev
- 你需要使用 Maglev 快速流程步骤进行快速、范围界定的实施

## 何时不使用
- 用户需要完整的规划工作流而不是快速开发
- 你不在 Maglev 项目上下文中

## 参与规则
- 在行动前阅读完整的步骤文件；绝不略读。
- 正如要求时使用 advanced-elicitation。
- 在指示时运行对抗性审查任务。
- 不要跳过步骤；严格遵循顺序。

## 必需的参考资料
所有引用的资源都复制到 `references/` 中以供独立技能使用。

- 工作流入口：`references/quick-dev.workflow.md`
- 步骤：`references/step-01-mode-detection.md` 到 `references/step-06-resolve-findings.md`
- 协议：`references/advanced-elicitation.workflow.xml`
- 审查任务：`references/review-adversarial-general.xml`

## 快速参考
- 步骤 01: 模式检测 (mode detection)
- 步骤 02: 上下文收集 (context gathering)
- 步骤 03: 执行 (execute)
- 步骤 04: 自检 (self-check)
- 步骤 05: 对抗性审查 (adversarial review)
- 步骤 06: 解决发现 (resolve findings)

## 示例
用户：“快速通过此修复程序进行开发。”
你：“我将运行 quick-dev 并通过自检和对抗性审查来实施更改。我应该从哪个文件开始？”

## 常见错误
- 跳过对抗性审查
- 忽略必要的诱导步骤
- 在未完成先前步骤的情况下跳跃
