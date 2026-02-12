# Step 4: Cross-Examination (交叉质询)

## 目标
让 Agent 切换角色为 "Detective"，对生成的 Spec 进行攻击性审查，确保其与代码严格一致。

## 动作
1.  **Persona Switch**: 切换为 [Code Detective]。
2.  **Load Review Task**: 读取 `references/review-adversarial-reverse.xml`。
3.  **Execute Review**: 逐条核对 Spec 中的 Claims 和 Code Refs。
4.  **Report Findings**: 输出 "Inconsistency Report"。
5.  **Final Polish**: 根据审查结果修正 Spec。

## 交互示例
AI (Detective): "我有异议！Spec 第 2.1 节说 'User ID must be not null'，但在 `UserController.java` 第 45 行，我依然看到了 `if (userId == null) return` 的防御代码。这说明业务上允许 null 并在 Controller 层拦截了，建议修正 Spec 描述。"

## 退出条件
所有 Inconsistency 都被解决或被用户确认为 "Acceptable Deviation"。
