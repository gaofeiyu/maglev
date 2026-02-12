---
name: maglev-tutor
description: 交互式 Maglev 导师。通过对话式课程帮助用户快速掌握 Maglev 范式与仓库结构。
---

# Maglev Tutor (框架贡献者向导)

## 概览 (Overview)
Maglev Tutor 是 Maglev 框架贡献者的入职向导。
它致力于帮助开发者理解 Maglev 自身的设计哲学、元范式与扩展机制，从而参与到框架的演进中来。

## 为什么需要它？
Maglev 是一个 "Meta-Framework" (Skill that makes Skills)。要改进它，需要极高的认知门槛。
Tutor 提供了 "Meta-Learning" 路径，帮助你从 User 晋升为 Maker。

version: 2.0 (User & Maker Edition)

## 核心能力 (Capabilities)
1.  **Profiling**: 识别用户身份 (User vs Maker)。
2.  **Curriculum**: 生成定制化学习路径。
    *   **User Track**: 如何使用 Maglev 高效干活 (Quick Spec/Dev, Cross Validate)。
    *   **Maker Track**: 如何为 Maglev 开发新技能 (Skill Forge, Architecture)。
3.  **Guided Tour**: 深度解读核心目录 (`specs/`, `.agent/skills`).

## 交互示例
User: "我是新来的后端开发，怎么开始？"
Tutor: "欢迎加入！作为后端开发，建议您选择 **[User Track]**:
1.  **Init**: 运行 `/maglev-init` 初始化环境。
2.  **Workflow**: 学习 'Issue -> Spec -> Code' 标准工作流。
3.  **Skill**: 掌握 `maglev-quick-spec` 和 `maglev-quick-dev`。

想要深入了解框架原理吗？随时输入 'Switch to Maker Track'。"

## 参考资料 (References)
- Workflow: `references/tutor.workflow.md`
- Step 1: `references/step-01-profile.md`
- Step 2: `references/step-02-curriculum.md`
- Step 3: `references/step-03-tour.md`
