# Maglev Methodology: 完整索引 (Full Index)

本文档将 "Maglev" 项目生成的所有 AI 协作方法论文档串联起来，形成一份完整的实施地图。
如果您是第一次接触本项目，请按以下顺序阅读。

## 0. 快速通道 (Quick Scenarios)
*按角色与其最紧迫的目标导航*

| 我是谁 (Role) | 我想做什么 (Goal) | 传送门 (Link) |
| :--- | :--- | :--- |
| **架构师 / Tech Lead** | 将 Maglev 引入现有团队 | [Track B: Workstation Mode](guides/project_startup_manuals.md#step-0-建立指挥部-setup-the-workstation) |
| **架构师 / Tech Lead** | 了解与 OpenSpec 的区别 | [Maglev vs OpenSpec](guides/maglev_vs_openspec.md) |
| **产品经理 / VO** | 定义需求 Spec | [Spec Lifecycle Protocol](starter-kit/.maglev/protocols/specs_lifecycle.md) |
| **开发者 / TP** | 接手老代码，开始修 Bug | [Reverse Engineering Guide](guides/legacy_project_adoption.md#step-2-建立逆向-agent-setup-archaeologist) |
| **所有人员** | 查阅 AI 协作守则 | [Core Rules](starter-kit/.maglev/rules/core_rules.md) |

## 1. 顶层设计 (The Big Picture)
了解我们为什么要重构 B2B 开发模式，以及核心理念是什么。
- **[thinking/ai_role_evolution_analysis.md](../thinking/ai_role_evolution_analysis.md)**: 之前的角色（PM/Dev/QA）为什么不适应 AI 时代了？
- **[thinking/workflow_comparison.md](../thinking/workflow_comparison.md)**: 为什么要从“线性接力”转向“环形迭代”？
- **[solutions/guides/maglev_vs_sdd.md](guides/maglev_vs_sdd.md)**: **Maglev vs SDD**。为什么有了 Spec-Driven Development 还需要 Maglev？（整体 vs 局部）
- **[solutions/guides/maglev_vs_openspec.md](guides/maglev_vs_openspec.md)**: **Maglev vs OpenSpec**。Maglev (OS) 与 OpenSpec (Protocol) 的深度对比与融合。

## 2. 核心架构 (The Core Framework)
Maglev 方法论的三大支柱。
1.  **组织模型 (People)**:
    - **[solutions/guides/role_personas.md](guides/role_personas.md)**: 定义了 **“铁三角” (Iron Triangle)** —— Value Owner, Tech Pilot, Experience Guardian。
    - *(附: [solutions/starter-kit/.maglev/rules/core_rules.md](starter-kit/.maglev/rules/core_rules.md) - AI 协作的核心宪法)*
2.  **执行流程 (Process)**:
    - **[solutions/starter-kit/.maglev/protocols/specs_lifecycle.md](starter-kit/.maglev/protocols/specs_lifecycle.md)**: **Spec 全生命周期协议**。Intent -> Build -> Check 的闭环执行细节。
- **[solutions/guides/project_startup_manuals.md](guides/project_startup_manuals.md)**: **项目启动手册**。包含资产结构定义与接入指南。
- **[solutions/skills/](skills/)**: **技能池目录**。按角色和技术栈分类的 AI 能力矩阵。

## 3. 落地指南 (Implementation Guides)
如何将理论应用到实际团队中？

### 3.1 怎么选人？
- **[solutions/guides/role_personas.md](guides/role_personas.md)**: **角色画像与人才选拔指南**。包含能力雷达图和面试结合题库。

### 3.2 怎么转型？
- **[solutions/guides/transition_guide.md](guides/transition_guide.md)**: **人员转型指南**。为现有 PM/Dev/QA 提供的 Stop/Start 清单和第一周行动计划。

### 3.3 怎么干活？
- **[solutions/guides/collaboration_playbook.md](guides/collaboration_playbook.md)**: **协作实战手册**。手把手的微操 SOP，包含 Git 规范和危机熔断机制。

## 4. 批判性视角 (Critical Perspective)
冷静下来，看看这套体系的弱点。
- **[solutions/evaluation/risk_analysis.md](evaluation/risk_analysis.md)**: **蓝军红队对抗分析**。主动暴露了方案的人才依赖、规模化难题及合规风险，并预判了反对者的声音。
- **[solutions/evaluation/measurement_framework.md](evaluation/measurement_framework.md)**: **量化评估与 ROI 框架**。定义了 3x 提效的成功门槛。
- **[solutions/guides/human_fallback_protocol.md](guides/human_fallback_protocol.md)**: **业务连续性计划 (BCP)**。定义了 AI 宕机时的 "降级模式" (Degraded Mode) 及消除工具参差的标准化策略。
- **[thinking/skill_safety_analysis.md](../thinking/skill_safety_analysis.md)**: **技能与安全反思**。针对 Agent 落地过程中的“上下文溢出”与“路径僵化”问题的红队分析。
- **[thinking/efficiency_matrix_design.md](../thinking/efficiency_matrix_design.md)**: **全流程提效矩阵设计**。探讨如何打通 Spec/Code/Bug/Case/Design 之间的资产虫洞。

---
> **阅读建议**:
> - **管理者/负责人**: 重点看 Part 1, Part 3.1/3.2, 和 **Part 4**。
> - **一线执行者**: 重点看 Part 2 和 Part 3.3。
