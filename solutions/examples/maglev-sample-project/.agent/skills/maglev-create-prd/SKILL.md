---
name: maglev-create-prd
description: 当运行或恢复 BMAD create-prd 工作流以通过基于步骤的过程生成 PRD 和验证报告时使用 (Maglev Edition)。
---

# 创建 PRD

## 概览
运行 BMAD create-prd 工作流以生成 PRD（创建、编辑和验证模式）。严格遵循步骤文件，通过正确的子流程并尊重所有菜单选项。

## 何时使用
- 用户要求运行或恢复 create-prd 工作流
- 你需要使用 BMAD 步骤生成 PRD，包括验证

## 何时**不**使用
- 用户想要快速的需求摘要，而不需要 BMAD 工作流
- 你不在 BMAD 项目上下文中

## 交互规则
- 行动前阅读完整的步骤文件；切勿略读。
- 不要一次加载多个步骤文件。
- 在菜单处停下并等待用户。
- 仅在 **C** (Continue) 或明确的路由条件下继续。
- 在继续之前更新输出 frontmatter 中的 `stepsCompleted`。
- 当步骤需要时，使用 advanced-elicitation/party-mode。
- 当完成步骤需要时，使用 bmad-help 任务。

## 必需的参考资料
所有引用的资源都已复制到 `references/` 以供独立技能使用。

- 工作流入口: `references/create-prd.workflow.md`
- 模板: `references/prd-template.md`
- 验证报告: `references/validation-report-prd-workflow.md`
- 数据: `references/domain-complexity.csv`, `references/project-types.csv`, `references/prd-purpose.md`
- 创建步骤 (C): `references/step-c-01-init.md` 到 `references/step-c-12-complete.md`
- 编辑步骤 (E): `references/step-e-01-discovery.md` 到 `references/step-e-04-complete.md`
- 验证步骤 (V): `references/step-v-01-discovery.md` 到 `references/step-v-13-report-complete.md`
- 协议: `references/advanced-elicitation.workflow.xml`, `references/party-mode.workflow.md`
- 帮助任务: `references/bmad-help.md`

## 快速参考
- 创建流程: 发现 → 成功 → 旅程 → 领域 → 创新 → 项目类型 → 范围界定 → 功能 → 非功能 → 润色 → 完成
- 编辑流程: 发现 → 遗留转换 → 审查 → 编辑 → 完成
- 验证流程: 发现 → 格式 → 一致性 → 密度 → 简报覆盖 → 可测量性 → 可追溯性 → 遗漏 → 领域合规 → SMART → 整体 → 完整性 → 报告完成

## 示例
用户：“为这个产品创建一个 PRD。”
你：“我将启动 create-prd 工作流，确定正确的路线（创建/编辑/验证），并遵循步骤文件。你是想从头开始创建还是验证现有的 PRD？”

## 常见错误
- 跳过创建/编辑/验证之间的路由逻辑
- 在没有所需菜单选择的情况下推进
- 未运行所需的诱导或派对模式步骤
- 忘记更新 `stepsCompleted`
