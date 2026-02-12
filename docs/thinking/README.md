# 思考与决策日志 (Thinking & Decision Log)

> **背景**: 这里记录了 Maglev 构建过程中的所有决策分析、反思与复盘。相当于项目的"大脑皮层"。

## 📂 00_meta (元理论 & 哲学)
核心创造范式的理论基石，定义 Maglev "为何存在" 及其底层逻辑。

*   **[maglev_manifesto.md](../30_philosophy_maglev_equation.md)** (⭐ Consolidated)
    *   **Maglev 宣言**：从方程到协议，重新定义软件工程的终极理论。包含准确性协议与迭代闭环。
*   **[accuracy_protocol.md](../35_accuracy_and_correction_protocol.md)**
    *   **纠错协议**：定义如何通过 Iron Triangle 协作来保证准确性与纠错流程。(Detailed Reference)
*   **[bidirectional_protocol.md](../36_bidirectional_context_protocol.md)**
    *   **双向协议**：定义正向设计与逆向事实的闭环机制。(Detailed Reference)
*   **[meta_paradigm_analysis.md](./00_meta/meta_paradigm_analysis.md)**
    *   剖析 "Intent -> Red Team -> Crystallization" 这一核心创造范式，阐述 Maglev 如何通过对抗消除不确定性。
*   **[atomizer_uncertainty_principle.md](./00_meta/atomizer_uncertainty_principle.md)**
    *   论述为何必须通过“雾化”将模糊意图拆解为原子任务，以应对软件工程中不可避免的熵增。
*   **[transparency_as_feature.md](./00_meta/transparency_as_feature.md)**
    *   阐述为何 Maglev 将过程透明化作为核心特性，而非仅仅关注最终产物，强调“过程即结果”。
*   **[spec_as_universal_ir.md](./00_meta/spec_as_universal_ir.md)**
    *   定义 Spec 为自然语言与机器代码之间的通用中间表示 (IR)，可视作 AI 时代的“高级汇编语言”。
*   **[prd_vs_spec_dialectic.md](./00_meta/prd_vs_spec_dialectic.md)**
    *   辩证分析 PRD (产品视角) 与 Spec (工程视角) 的异同及转换关系，明确两者在 Maglev 中的定位。
*   **[ai_role_evolution_analysis.md](./00_meta/ai_role_evolution_analysis.md)**
    *   探讨 AI 从 Copilot 工具人到 Agent 合作伙伴的角色演进路径，以及人类职责的相应变化。

## 📂 10_critique (批判与反思)
自我红队测试记录，记录 Maglev 自身的局限性、潜在风险与反思。

*   **[defense_completeness_myth.md](./10_critique/defense_completeness_myth.md)**
    *   批判“一开始就设计完美防御”的妄念，提倡演进式防御，主张在对抗中完善系统。
*   **[fleet_vision_critique.md](./10_critique/fleet_vision_critique.md)**
    *   对 Maglev 舰队愿景的自我批判，深入分析多 Agent 协作可能带来的混乱与管理成本。
*   **[tech_generation_critique.md](./10_critique/tech_generation_critique.md)**
    *   反思技术代际更迭，警示避免盲目追逐新框架而忽视工程本质，提倡“守正出奇”。
*   **[2026-02-02-maglev_vs_bmm_critique.md](./10_critique/2026-02-02-maglev_vs_bmm_critique.md)**
    *   对比 Maglev Deep Mode 与 BMM (Business Model Master)，反思深度思考模式在工程落地中的优劣。
*   **[reflection_phase1_risks.md](./10_critique/reflection_phase1_risks.md)**
    *   复盘 Phase 1 阶段发现的执行偏差与潜在风险，为后续迭代提供改进依据。
*   **[workflow_comparison.md](./10_critique/workflow_comparison.md)**
    *   对比不同工作流模式的效率与适用场景，分析 Maglev 在特定团队结构下的适配性。
*   **[research_industry_validation.md](./10_critique/research_industry_validation.md)**
    *   调研行业内类似 AI 工程化方案(Flow Engineering, Agentless)，验证 Maglev 的独特定位与价值。

## 📂 20_architecture (架构设计)
具体的系统设计文档，描述 Maglev 的组件交互与技术决策。

*   **[atomic_spec_architecture.md](./20_architecture/atomic_spec_architecture.md)**
    *   详解原子化 Spec 的结构设计，如何实现从单体文档到碎片化知识的解耦与重组。
*   **[2026-02-02-maglev_atlas.md](./20_architecture/2026-02-02-maglev_atlas.md)**
    *   Maglev Atlas 体系的顶层设计，定义世界、地形、城市、街道四层地图隐喻，指导项目可视化。
*   **[visual_verification_strategy.md](./20_architecture/visual_verification_strategy.md)**
    *   定义基于视觉快照的验证策略，确保 UI 实现与设计稿的一致性，通过像素级对比发现缺陷。
*   **[tech_robustness_gap_analysis.md](./20_architecture/tech_robustness_gap_analysis.md)**
    *   分析当前技术栈的鲁棒性短板，提出针对性的架构补全计划，提升系统的稳定性。
*   **[skill_safety_analysis.md](./20_architecture/skill_safety_analysis.md)**
    *   评估 Skill 执行过程中的安全边界与权限控制策略，防止 AI 越权操作或破坏代码。
*   **[adoption_model_evolution.md](./20_architecture/adoption_model_evolution.md)**
    *   演进接入模型，描述从“全盘接管”转向“渐进式增强”的策略调整，降低接入阻力。

## 📂 90_archive (归档)
历史任务清单与过时的推演记录。

*   **[doc_cleanup_2026_02_02/](./doc_cleanup_2026_02_02/task.md)**: 文档重构任务清单。
*   **[deep_mode_rollout_2026_02_02/](./90_archive/deep_mode_rollout_2026_02_02/task.md)**: Deep Mode 推广实施记录。
*   **[2026-02-03] Maglev 加固与 OpenSpec 标准化**
  [链接](./2026-02-03-maglev-fortification/00_index.md)
  *"三模态安全"升级 (逆向/Spec/PRD) 与 OpenSpec 采用的整合思考记录。*

*   **[2026-02-03] 工作流暴露策略**
  [链接](./workflow_exposure_2026_02_03/implementation_plan.md)
  *关于向用户暴露工作流的策略分析。*

*   **[2026-02-03] 后端偏差修复**
  [链接](./backend_bias_fix_2026_02_03/implementation_plan.md)
  *修复生成逻辑中后端偏差的问题。*
*   **[reverse_spec_redesign_2026_02_01/](./90_archive/reverse_spec_redesign_2026_02_01/task.md)**: 逆向 Spec 重构过程记录。
*   **[skill_extension_2026_02_01/](./90_archive/skill_extension_2026_02_01/task.md)**: 技能扩展（Design/Research）实施记录。

---
*Generated by Maglev Librarian - Johnny Decimal System*
