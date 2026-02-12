---
type: prd_requirements
version: openspec-2.0
---

# {产品/功能名称} PRD

> 👤 **Executive Brief (决策摘要)**
> *   **背景 (Context)**: {为什么要做这个？背景是什么？}
> *   **目标 (Goal)**: {核心业务目标}
> *   **范围 (Scope)**: {包含什么 vs 不包含什么}

## Requirements (Zone 2 - 需求规格)

> **Standard**: OpenSpec (Req -> Scenario -> Gherkin)

### Requirement: {需求标题}
系统必须 (SHALL) {严格的需求声明}。

#### Scenario: {场景标题}
> **Intent**: {场景意图简述}

- **GIVEN** {前置条件 / 上下文}
- **WHEN** {触发动作 / 行为}
- **THEN** {预期结果}
- **AND** {补充检查 / 副作用}

#### Scenario: {另一个场景}
- **GIVEN** ...
- **WHEN** ...
- **THEN** ...

### Requirement: {另一个需求}
系统必须 (SHALL) ...

---

<details>
<summary>🤖 Context Trace (Zone 3 - 上下文溯源)</summary>

### Rationale
*   **Why OpenSpec?**: 采用更高精度的 BDD 格式以支持自动化测试。
*   **Source**: {访谈 / 发现阶段}

</details>
