# Maglev - AI 时代的工程化研发新范式 (AI-Native Engineering Protocol)

![License](https://img.shields.io/badge/license-MIT-blue.svg)

> **"Unlearn, to Relearn."**
> Maglev 是基于 [**Zhiyin (知音)**](https://github.com/gaofeiyu/zhiyin) 思考框架构建的 AI 原生操作系统。
> 它不仅仅是一套文档，它是一套让 AI 指挥 IDE、让工程师回归架构、让产品经理定义灵魂的 **"人机协作操作系统"**。

---

## 🔭 核心架构：Maglev 协议 (The Maglev Protocol)

Maglev 提出了 **"Project -> Organization -> Insight"** 的三层治理架构，旨在打通从单点代码生成到组织战略洞察的全链路。

*   **Layer 1: Project (执行层)**: `Spec -> Code`。通过 **Atomizer** 和 **Gatekeeper** 实现单项目的闭环交付与自愈。
*   **Layer 2: Organization (协作层)**: `Hub -> Spoke`。通过 **Global Indexing** 和 **Shareable Skills** 打通资产孤岛，实现能力复用。
*   **Layer 3: Insight (战略层)**: `Code -> Data`。通过 **Reverse Analysis** 逆向生成人才画像与风险热力图。

📖 **深入阅读**: [Maglev 协议：AI原生协作架构 (The Protocol)](solutions/guides/10_concepts/maglev_paradigm_architecture.md)

---

## 🤝 协作范式：人机共生 (Collaborative Symbiosis)

我们重新定义了 AI 时代的研发分工：
*   **Human (人类)**：负责 **定义意图** (60%) 和 **最终仲裁** (验收)。
*   **AI (智能体)**：负责 **全链路执行** (90%) 和 **自愈修正** (Debug)。
*   **Platform (平台)**：负责 **规则守门** (Gatekeeper)，拦截一切不一致。

> **价值**: 让开发者从 "搬砖工" (Coding) 升级为 "建筑师" (Defining)。

---

## 🧩 核心概念: Skills vs Workflows

Maglev 的能力通过两种形式提供，理解它们的区别能显著提升使用效率：

*   **Skills (技能)**: Maglev 的"原子能力"。它们存在于 `.agent/skills`，包含复杂的 Prompt 和执行逻辑 (如 `maglev-create-prd`)。虽然可以直接调用，但名字较长，适合作为后台引擎。
*   **Workflows (工作流)**: 技能的"快捷方式"。它们存在于 `.agent/workflows`，通常配置为 IDE 的 Slash Commands (如 `/create-prd`)。

> **最佳实践**: 推荐优先使用 Workflows (Slash Commands) 进行日常交互，它们封装了最佳的 Prompt 调用方式。

---

## 🎮 交互指南 (Interaction Guide)

Maglev 不要求你背诵 26 个技能。你只需要记住以下 **魔法指令**：

| 场景 | 指令 | 用途 | 对应技能 |
| :--- | :--- | :--- | :--- |
| **导航** | **`/map`** | **Where am I?**<br>生成/更新项目地图 (Atlas)。 | `maglev-map-maker` |
| **启动** | **`/init`** | **Bootstrap**<br>初始化项目 (交互式注册仓库)。 | `maglev-bootstrapper` |
| | **`/standup`** | **What's up?**<br>每日站会，加载上下文。 | `maglev-standup` |
| **创造** | **`/create-spec`** | **New Feature**<br>生成技术方案 (Spec)。 | `maglev-create-spec` |
| | **`/create-prd`** | **New Idea**<br>生成 PRD。 | `maglev-create-prd` |
| | **`/quick-dev`** | **Coding**<br>快速开发功能 (无需重型Spec)。 | `maglev-quick-dev` |
| **治理** | **`/audit-spec`** | **Quality Gate**<br>审计 Spec 一致性。 | `maglev-audit-spec` |
| | **`/validate-all`** | **Deep Check**<br>全域交叉验证。 | `maglev-cross-validate` |

---

## 🚀 如何落地 Maglev (Adoption Guide)

Maglev 不仅仅是一套文档，更是一套**可执行的操作系统**。根据你的项目现状，选择对应的落地路径：

### 🟢 路径 A: 绿地开荒 (Greenfield)
*适用于：全新项目，从零开始。*
- **核心逻辑**: **Zero-Code Bootstrap** (Prompt -> Init -> Issue).
- **实操手册**: [🪄 智能初始化指南 (AI-Driven Setup)](solutions/templates/maglev_init_guide.md) - **<-- 推荐！** 让 AI 替你完成所有目录创建和配置。

### 🟠 路径 B: 存量转型 (Legacy Transformation)
*适用于：已有代码库 (单库或多库)，文档缺失，希望逐步引入 AI 协作。*
- **核心逻辑**: **Workstation Mode** (Establish HQ -> Mount Legacy -> Reverse Spec)。
- **战略指南**: [🏗️ 遗留项目接入指南 (Progressive Alignment)](solutions/guides/00_start/legacy_project_adoption.md) - 定义了如何通过 "工作站" 模式非侵入式纳管业务代码。
- **实操手册**: [🚑 项目启动手册 (Track B)](solutions/guides/00_start/project_startup_manuals.md) - 教你如何搭建 "Maglev Workstation" 并挂载现有仓库。

---

## 🗂️ 仓库索引 (Repository Index)

> **Purpose**: 连接所有子模块的入口索引。这是 Maglev 的 **"Map of Maps"**。

### 核心导航 (Core Navigation)
| 模块 | 路径 | 职责 | 索引文件 |
| :--- | :--- | :--- | :--- |
| **🧠 Thinking** | [docs/thinking/](docs/thinking/) | **WHY**. 设计原理与架构决策。 | [README.md](docs/thinking/README.md) |
| **⚖️ Standards** | [standards/](standards/) | **WHAT**. 被固化的规范与检查清单。 | [README.md](standards/README.md) |
| **🛠️ Solutions** | [solutions/](solutions/) | **HOW**. 具体的解决方案与 Starter Kit。 | [README.md](solutions/README.md) |
| **📓 Docs** | [docs/](docs/) | **STATUS**. 项目日志与状态报告。 | [README.md](docs/README.md) |
| **� References** | [references/](references/) | **EXTERNAL**. 学术论文与外部文章。 | [README.md](references/README.md) |
| **🗄️ Archive** | [archive/](archive/) | **HISTORY**. 历史废弃物。 | - |

---

## 💎 核心资产导航 (Core Assets)

### 1. 理论内核 (The Core)
- **组织架构**: [铁三角核心法则 (Core Rules)](solutions/starter-kit/.maglev/rules/core_rules.md) - 定义 Value Owner, Tech Pilot, Experience Guardian 的协作宪法。
- **执行流程**: [Spec 全生命周期协议 (Lifecycle)](solutions/starter-kit/.maglev/protocols/specs_lifecycle.md) - 定义 00-99 状态流与环形迭代。
- **验证体系**: [效率矩阵 (Efficiency Matrix)](solutions/guides/10_concepts/efficiency_matrix_design.md) - 打通 Spec/Code/Bug/Case/Design/Platform 的六维虫洞。

### 2. 工具与技能 (The Tools)
- **启动套件**: [Starter Kit](solutions/starter-kit/README.md) - 包含核心规则与协议的开箱即用包。
- **技能池**: [技能目录 (Skills)](solutions/starter-kit/.agent/skills/) - 即插即用的 Prompt/SOP。
- **应急手册**: [断电协议 (Human Fallback)](solutions/guides/20_operations/human_fallback_protocol.md) - 当 AI 挂了怎么干活。

### 3. 参考知识库 (Knowledge Base)
- [references/papers/](references/) - 收录了 Flow Engineering, Agentless 等前沿论文。
- [references/articles/agentic_se_critiques.md](references/articles/agentic_se_critiques.md) - **红队反思**：AI 的暗面与风险。

---

## 🤝 贡献与反馈
本项目遵循 [standards/collaboration_conventions.md](standards/collaboration_conventions.md)。
- **贡献记录**: [contributors/contribution_log.md](contributors/contribution_log.md)
- **问题反馈**: 请提交 [Issues](issues/)。
- **Pull Requests**: 请确保阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

*Generated by Maglev Team (Human Strategic Intent + AI Execution)*
*Last Updated: 2026-02-12*
