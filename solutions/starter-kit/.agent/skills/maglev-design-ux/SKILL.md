---
name: maglev-design-ux
description: (Experience Layer) 负责将 Spec 转化为显性的 UX 设计方案。通过深度移情访谈理解真实用户，产出 Persona、User Journey 和 UI 状态图。
version: 2.0 (Deep Mode)
---

# Maglev Design UX (移情设计伙伴)

> **Role**: Empathetic Design Partner (移情设计伙伴)
> **Motto**: "Don't make me think. But first, let me understand WHO is thinking."

## 核心职责
本技能负责在编码之前，对 **用户体验 (User Experience)** 进行显性化设计。
它弥补了从 Spec 到 Code 之间的 "Design Gap"，防止 UI 变成 "工程师审美"。

**Deep Mode 增强** 🆕:
- 拒绝 "一般用户" 这种模糊定义
- 强制进行情绪曲线 (Before/During/After) 分析
- 主动挑战用户假设

## 适用场景
- **Complex UI**: 需要设计复杂的交互流程时。
- **User Facing**: C端产品或对体验有高要求的B端功能。
- **Ambiguity**: Spec 对 UI 描述模糊，需要具体化时。

## 技能产出
*   **Design Spec**: `specs/20_evolution/active/{slug}/02_ui_design.md`
    *   **Persona**: 深度用户画像 (非抽象标签)。🆕
    *   **User Journey Map (Mermaid)**: 带有情绪曲线的用户旅程图。
    *   **State Diagram (Mermaid)**: 关键组件的 UI 状态流转图。

## 工作流 (The Design Flow)
1.  **Empathy (同理心)**: 谁在用？为什么用？(Deep Interview) 🆕
2.  **Journey (旅程)**: 怎么用？爽点痛点在哪里？(Journey Map)
3.  **Visual (视觉逻辑)**: 长什么样？状态怎么变？(State Diagram)
4.  **Handoff (交付)**: 生成 Design Spec。

## 必需的参考资料
*   工作流: `references/design-ux.workflow.md`
*   Step 1 (Empathy - Deep): `references/step-01-empathy.md` 🆕
*   Step 2 (Journey): `references/step-02-journey.md`
*   Step 3 (Visual): `references/step-03-visual.md`
*   Step 4 (Handoff): `references/step-04-handoff.md`
