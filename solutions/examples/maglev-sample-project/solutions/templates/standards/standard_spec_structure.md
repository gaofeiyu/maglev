# Maglev Spec 结构标准 (The Bookshelf Standard)

> **Status**: Draft (Co-creation Phase)
> **Purpose**: 定义 Maglev 体系下 "Spec" (作为 Reality 的容器) 的标准物理存储结构。

## 1. 核心理念 (Philosophy)

*   **Spec is a Folder, not a File**: 为了承载复杂的业务逻辑和交叉验证需求，Spec 必须是一个**文件簇 (File Cluster)**。
*   **Separation of Concerns**: 将"需求契约"、"技术实现"与"执行计划"物理分离，以便于不同角色的 AI (TestDev, Architect, PM) 独立读取和处理。

## 2. 目录层级 (Directory Hierarchy)

Maglev 的 Specs 书架应当遵循以下层级：

```text
spec/
├── 10_reality/              # 现状 (The Truth)
│   ├── _global/             # [NEW] 全局共享定义 (The Commons)
│   │   ├── system_db.md     # 全局数据模型 (ERD)
│   │   ├── system_api.md    # 全局接口注册表
│   │   └── system_ui.md     # 设计规范 (Design Tokens)
│   │
│   └── {Domain_Name}/       # 领域/模块 (e.g., User, Order)
│       ├── _domain_model.md # 领域模型 (Context Map)
│       └── {Feature_Name}/  # 具体功能单元 (The Unit)
│
├── 20_evolution/            # 演进 (Changes)
│   └── ... (同上结构)
```

## 3. 标准单元结构 (The Spec Unit)

一个标准的 Feature Spec 目录 (`{Feature_Name}/`) 必须包含以下文件：

| 文件名 | 角色 | 用途 | 验证链 (Verification Chain) |
| :--- | :--- | :--- | :--- |
| **`00_index.md`** | **The Spine (脊柱)** | 元数据、导航、状态跟踪。 | Librarian 扫描此文件生成索引。 |
| **`01_requirements.md`** | **The Contract (契约)** | 用户故事、验收标准 (AC)、边界。 | -> 生成 **Test Cases**。 |
| **`02_design.md`** | **The Blueprint (蓝图)** | 架构建模、API 定义、**UI 交互细节**。 | -> 验证 Code & UI Restore。 |
| **`03_plan.md`** | **The Roadmap (路线)** | 实施步骤、任务拆解 (Task List)。 | -> 对齐 **task.md**。 |
| **`assets/`** | **The Visuals (视觉)** | 存放 UI 截图、流程图源文件。 | -> 视觉还原度走查。 |

---

## 4. 文件详情 (File Details)

### `00_index.md`
> **管理视图**：给人和 Librarian 看的。

```markdown
# [Feature Name]
> Status: Planning | In-Progress | Verified

## Metadata
*   **Owner**: [User]
*   **Created**: [Date]
*   **Last Updated**: [Date]

## Navigation
*   [需求契约](./01_requirements.md)
*   [技术蓝图](./02_design.md)
*   [实施计划](./03_plan.md)
```

### `01_requirements.md`
> **业务视图**：给 PO 和测试看 (以及生成用例的 AI)。

```markdown
# 需求与验收契约

## 1. 核心意图 (Intent)
(一句话描述价值)

## 2. 用户故事 (User Stories)
*   As a [User]
*   I want [Feature]
*   So that [Benefit]

## 3. 验收标准 / 举例 (Acceptance Criteria)
> Format: Gherkin-style preferred (Given/When/Then)

### AC1: [Scenario Name]
*   **Given**: ...
*   **When**: ...
*   **Then**: ...
```

### `02_design.md`
> **技术视图**：只描述 **Delta (增量变化)**。

```markdown
# 技术实现蓝图

## 1. 架构视图 (Architecture)
*   **Module**: (此功能属于哪个模块)
*   **Dependency**: (依赖哪些全局组件)

## 2. 数据模型变更 (Data Model Delta)
> 不要在此重写整个 CREATE TABLE。引用 Global，只写变更。
*   **Table**: `Users`
*   **Change**: Add column `vip_level` (INT).

## 3. 接口变更 (API Delta)
*   [NEW] `POST /api/v1/user/upgrade`
```

---

## 5. 规模化原则 (Scalability Principles)

1.  **Global Defines, Local Extends**:
    *   全局表结构在 `10_reality/_global/system_db.md` 定义。
    *   功能 Spec 在 `02_design.md` 中只描述"我要修改哪个表"。
2.  **Domain Driven**:
    *   不要把所有 Spec 堆在一起。先按照 `Domain` (业务域) 分组，再按 `Feature` (功能) 拆分。
3.  **UI Components**:
    *   通用组件 (Button, Layout) 在 `_global/system_ui.md`。
---

## 6. 多态设计原则 (Polymorphic Design)

虽然目录结构 (`00-03`) 是通用的，但在不同的项目类型中，`02_design.md` 的内容侧重点完全不同。

### Variant A: UI-Centric (Web/App)
*   **Focus**: Visual & Interaction (所见即所得).
*   **`02_design.md` Content**:
    *   **Design Source**: 引用 Figma/蓝湖链接 (Source of Truth)。
    *   **Visual Snapshot**: 必须包含关键状态的截图 (存放在 `./assets/` 下)，防止远端设计稿变更导致的历史追溯丢失。
    *   **Component Tree**: 组件层级关系。
    *   **Interaction Table (交互表)**:
        | Component | Event | Action | State Change |
        | :--- | :--- | :--- | :--- |
        | `SubmitBtn` | `OnClick` | Call `API_Login` | `Loading=true` |
        | `API_Login` | `OnSuccess` | Redirect | `Route=/home` |

### Variant B: Logic-Centric (Backend/Lib)
*   **Focus**: Data & Algorithm.
*   **`02_design.md` Content**:
    *   **API Schema**: Swagger/OpenAPI 定义。
    *   **ERD**: 数据库实体关系。
    *   **Sequence Diagram**: 复杂业务的时序逻辑。
    *   **Concurrency**: 锁与事务策略。

### Variant C: Agentic (AI Ops)
*   **Focus**: Prompt & Context.
*   **`02_design.md` Content**:
    *   **Prompt Strategy**: System Prompt 结构与策略。
    *   **Workflow Graph**: 智能体工作流 (State Machine)。
    *   **Tool Interface**: 外部工具调用规范。
    *   **Context Window**: 上下文管理策略。
