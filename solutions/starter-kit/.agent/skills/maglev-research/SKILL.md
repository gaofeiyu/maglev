---
name: maglev-research
description: (Observation Layer) 执行深度的市场或技术调研。通过假设挑战避免确认偏误，生成带引用的分析报告。
version: 2.0 (Deep Mode)
---

# Maglev Research (调研负责人)

> **Role**: Research Lead (调研负责人)
> **Motto**: "Facts over Opinions. But first, challenge your assumptions."

## 核心职责
本技能负责**获取外部信息**并进行**深度综合**。
它借鉴了 BMM-02 的严谨性，强制要求对关键事实进行**多源验证**和**引用标注**。

**Deep Mode 增强** 🆕:
- 在搜索前主动挑战用户假设
- 识别并记录预设答案
- 明确调研服务的决策点

## 适用场景
- **Tech Selection**: 技术选型 (e.g. "React vs Vue 2026")。
- **Market Analysis**: 市场/竞品分析 (e.g. "AI IDE 竞品功能对比")。
- **Domain Learning**: 领域知识补全 (e.g. "了解 HIPAA 合规要求")。

## 技能产出
*   **Research Report**: `docs/research/{date}-{topic}.md`
    *   **Executive Summary**: 一页纸结论。
    *   **Fact Sheet**: 事实清单 (带 Citation)。
    *   **Analysis**: 深度分析与建议。
    *   **Assumptions Log**: 被挑战/确认的假设记录。🆕
    *   **References**: 参考文献列表。

## 工作流 (The Research Loop)
1.  **Scope**: 要查什么？(Define Questions + Challenge Assumptions) 🆕
2.  **Search**: 联网地毯式搜索。(Search Web)
3.  **Synthesize**: 事实交叉验证，排除幻觉。(Citation Check)
4.  **Report**: 生成报告。(Markdown)

## 必需的参考资料
*   工作流: `references/research.workflow.md`
*   Step 1 (Scope - Deep): `references/step-01-scope.md` 🆕
*   Step 2 (Search): `references/step-02-search.md`
*   Step 3 (Report): `references/step-03-report.md`
