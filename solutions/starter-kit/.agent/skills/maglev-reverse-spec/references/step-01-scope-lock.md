# Step 1: Scope Lock (范围锁定)

## 目标
防止 AI 读取整个庞大的 Legacy 仓库导致上下文溢出。只锁定与当前“逆向目标”直接相关的文件。

## 动作
1.  **Request Entry Point**: 询问用户“从哪里开始？”（e.g., Controller, Service）。
2.  **Breadth-First Search (BFS)**: 读取入口文件的 imports，询问是否展开。
3.  **Test Start Discovery (关键步骤)**:
    *   **Physics Layer (White Box)**: 自动寻找 `code_storages` 内同级或 `src/test` 下的伴生测试文件 (e.g., `Foo.java` -> `FooTest.java`).
    *   **Guard Layer (Black Box)**: 启发式扫描 `tests/` 目录。
        *   **Acceptance**: 扫描 `tests/acceptance/*.{feature,robot,xlsx,csv}`。
        *   **E2E**: 扫描 `tests/e2e/*.{py,js,ts,go}`。
        *   **Heuristics**: 搜索文件名或内容包含入口类名 (Case Insensitive)。
4.  **Lock Scope**: 生成包含 Code + Tests 的完整文件列表。

## 交互示例
AI: "收到请求。请告诉我分析的入口文件路径。"
User: "code_storages/legacy_service/src/main/java/com/example/PaymentController.java"
AI: "正在分析依赖..."
AI: "发现了以下关联文件：
- **Code**: `PaymentService.java`
- **Unit Test**: `PaymentControllerTest.java` (Found in `src/test/java/...`)
- **E2E Test**: `tests/refund_scenario.robot` (Found by heuristic search)
是否将它们全部纳入分析范围？"
User: "是的。"
AI: "Scope Locked."

## 输出
更新 Frontmatter:
```yaml
scopeLocked:
  - path/to/FileA
  - path/to/FileB
```
