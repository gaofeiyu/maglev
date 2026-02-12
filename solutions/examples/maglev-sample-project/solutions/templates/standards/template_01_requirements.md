---
type: spec_requirements
version: 2.0
---

# 需求定义 (Requirements Definition)

> **Goal**: {一句话描述核心业务目标}

## 1. 用户故事 (User Stories)
> Format: `AS A <Role>, I WANT <Action>, SO THAT <Benefit>`

### [Story-1] {Story Title}
*   **As a**: {Role}
*   **I want**: {Action}
*   **So that**: {Benefit}

#### 验收标准 (Acceptance Criteria)
> **Rule**: 必须是可测试的 (Testable)。
- [ ] **AC 1.1**: {Condition 1} -> {Expected Result 1}
- [ ] **AC 1.2**: {Condition 2} -> {Expected Result 2}

---

## 2. 功能性需求 (Functional Requirements)
> 补充 User Story 未覆盖的系统级需求 (e.g., Validation, Logic)。

| ID | 模块 | 需求描述 | 优先级 |
| :--- | :--- | :--- | :--- |
| **FR-01** | API | 输入参数必须校验非空 | P0 |
| **FR-02** | DB | 软删除逻辑 (deleted_at) | P1 |

## 3. 非功能性需求 (Non-Functional Requirements)
> 性能、安全、兼容性。

*   **Performance**: {e.g. API latency < 200ms}
*   **Security**: {e.g. RBAC required}

## 4. 边界与排除 (Out of Scope)
> 明确**不做什么**，防止 Scope Creep。
*   [ ] 不包含 {Feature X}
*   [ ] 不支持 {Platform Y}
