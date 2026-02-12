# Step 2: Strata Analysis (地层分析)

## 目标
深入代码细节，提取“显式逻辑”并推断“隐式意图”。

## 动作
## 动作
1.  **Read Files**: 逐个读取 Locked Scope 中的文件。
2.  **Trace Path**: 跟踪关键方法的调用链。
3.  **Test Forensics (测试考古)**:
    *   **Unit Tests**: 读取 `*Test.java` / `*.spec.ts`。
        *   从 `assert` 语句反推业务规则 (e.g., `assertEquals(10, calc(5, 2))` -> "Multiplier is 2").
        *   从 `mock` 数据推断外部依赖结构。
    *   **E2E Tests**: 读取 `.feature` 或 `.robot` 文件。
        *   提取 Given-When-Then 场景，直接作为 User Story 的输入。
4.  **Identify Artifacts**:
    *   **Logic**: `if-else`, loops, validation rules.
    *   **Data**: Class fields, DB schema hints.
    *   **Events**: Kafka messages, HTTP calls.
5.  **Note Taking**: 在 Context 中生成一份临时的 "Logic Map"。

## 关键指令
"请阅读 [SourceFile] 及其关联的 [TestFile]，执行：
1. **Source Analysis**: 提取核心分支逻辑。
2. **Test Analysis**: 列出所有 Test Case 覆盖的业务场景 (Spec by Example)。
3. **Synthesis**: 用测试用例验证代码逻辑，输出确认后的业务规则。"

## 输出
Logic Map (Internal draft, not shown to user yet).
