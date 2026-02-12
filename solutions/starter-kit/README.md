# Maglev Starter Kit

> **The "Iron Trinity" Bootstrap Pack**
> 专为 AI Agent 协作设计的工程骨架。

## 🗺️ Maglev Atlas (项目导航)
> **Magic Command**: Run `/maglev-map-maker` to generate `docs/ATLAS.md`.

### 🏔️ 真实地形 (Reality)
*(Please run `/maglev-map-maker` to generate the Atlas)*

---

## 🧩 核心概念: Skills vs Workflows

Maglev 的能力通过两种形式提供，理解它们的区别能显著提升使用效率：

*   **Skills (技能)**: Maglev 的"原子能力"。它们存在于 `.agent/skills`，包含复杂的 Prompt 和执行逻辑 (如 `maglev-create-prd`)。虽然可以直接调用，但名字较长，适合作为后台引擎。
*   **Workflows (工作流)**: 技能的"快捷方式"。它们存在于 `.agent/workflows`，通常配置为 IDE 的 Slash Commands (如 `/create-prd`)。

> **最佳实践**: 推荐优先使用 Workflows (Slash Commands) 进行日常交互，它们封装了最佳的 Prompt 调用方式。

## 🎮 交互指南 (Interaction Guide)

以下列出的指令本质上是调用了后台对应的 Maglev Skills。

| 场景 | 指令 | 用途 |
| :--- | :--- | :--- |
| **导航** | `/map` | 生成/更新项目地图 (Atlas) |
| **启动** | `/maglev-init` | 初始化项目 (交互式注册仓库) |
| | `/standup` | 每日站会，加载上下文 |
| | `/tutor` | 启动教程模式 |
| **创造** | `/create-prd` | 生成 PRD |
| | `/create-spec` | 生成技术方案 (Spec) |
| | `/quick-dev` | 快速开发功能 |
| | `/create-tests` | 生成测试用例 |
| **发现** | `/design-ux` | UX 设计师访谈 |
| | `/research` | 深度调研 |
| **治理** | `/audit-prd` | 审计 PRD |
| | `/audit-spec` | 审计 Spec |
| | `/validate-all` | 全域交叉验证 |
| | `/code-review-backend` | 后端代码审查 (New) |
| | `/code-review-frontend` | 前端代码审查 (New) |
| **扩展** | `/new-skill` | 创建新技能 |
| | `/legacy-adopter` | 存量项目接入 (New) |

> **Tip**: 输入 `/` 即可触发 IDE 的指令补全。所有指令均支持**中文交互**。

📖 **完整地图**: [docs/ATLAS.md](docs/ATLAS.md)

---

## 📦 组件清单 (Inventory)
- **`.agent/skills/`**: 26+ 智能体技能 (Tutor, Map Maker, etc.)。
- **`.maglev/`**: 核心协议与规则。
- **`specs/`**: 10_reality (架构) 和 20_evolution (管线)。

## 🚀 快速开始 (Usage)

1. 将本目录所有文件复制到新项目的根目录。
2. 打开 **`maglev_init_guide.md`** 文件。
3. 唤起您的 AI 助手 (无论是 Cursor, Trae 还是 Windsurf)，投喂以下指令：
    > **"请阅读当前文档，理解 Maglev 的核心要素 (Rules, Skills, Workflows)。**
    > **然后，请协助我将当前工作区 Bootstrapping 为符合标准的目标状态。"**
4. 跟随 AI 的确认，配置 IDE Context 规则。
4. 运行 `/maglev-init` 初始化 AI 上下文。

---

## 📚 附录：完整技能池 (Appendix: Full Skill Inventory)

> Maglev 技能池包含 **20+ 个即插即用的 AI 技能**，供高级用户查阅。

### 📝 Spec 生产 (Spec Production)
| 技能 | 说明 |
|------|------|
| `maglev-quick-spec` | 协调器：端到端 Spec 生成 |
| `maglev-spec-ingest` | 原子技能：意图摄入与降噪 |
| `maglev-spec-draft` | 原子技能：Spec 草稿生成 |
| `maglev-spec-crystallize` | 原子技能：Spec 拆分与归档 |
| `maglev-create-prd` | PRD 生成 (BMAD Style) |
| `maglev-reverse-spec` | 逆向工程：代码 → Spec |
| `maglev-design-ux` | **New!** 体验设计 (Persona/Journey/State) |
| `maglev-research` | **New!** 深度调研 (Citation) |

### 🔍 质量保障 (Quality Assurance)
| 技能 | 说明 |
|------|------|
| `maglev-audit-prd` | PRD 质量审计 |
| `maglev-audit-spec` | Spec 工程一致性审计 |
| `maglev-cross-validate` | 全域交叉验证 (PRD↔Spec↔Code↔Tests) |
| `maglev-validate-spec-context` | Spec 上下文校验 |

### 🧪 测试规划 (Test Planning)
| 技能 | 说明 |
|------|------|
| `maglev-create-test-cases` | 测试用例生成 (Unit/Int/E2E 分层) |
| `maglev-plan-unit-tests-backend` | 后端单测规划 (Java/Python/Go/Node) |
| `maglev-plan-unit-tests-frontend` | 前端单测规划 (Vue/React) |

### 👀 代码审查 (Code Review)
| 技能 | 说明 |
|------|------|
| `maglev-code-review-backend` | 后端代码审查 |
| `maglev-code-review-frontend` | 前端代码审查 |

### 🏗️ 项目管理 (Project Management)
| 技能 | 说明 |
|------|------|
| `maglev-bootstrapper` | 项目初始化 (Greenfield/Brownfield) |
| `maglev-legacy-adopter` | 存量项目接入助手 |
| `maglev-librarian` | 项目索引管理 |
| `maglev-quick-dev` | 快速开发 (Self-Review Mode) |

### 🎓 辅助工具 (Utilities)
| 技能 | 说明 |
|------|------|
| `maglev-tutor` | 交互式教程 |
| `maglev-skill-forge` | 技能孵化器 |
| `atomizer` | 意图雾化器 |
| `maglev-map-maker` | **New!** 自动地图生成 (Atlas) |
| `maglev-standup` | **New!** 每日站会 |
| `mermaid_expert` | Mermaid 图表专家 |
