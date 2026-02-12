---
description: maglev-cross-validate Step 2 - Cross-Reference
---

# Step 2: Cross-Reference (交叉比对)

## 目标
对 Step 1 收集的上下文进行多维度一致性检查。

## 比对维度

### Layer 1: PRD ↔ Spec (需求 ↔ 设计)
**检查项**:
- 每个 User Story 是否有对应的 API 设计？
- 每个 AC 是否可追溯到技术实现？

**匹配逻辑**:
```python
for story in prd_context.user_stories:
    linked_apis = spec_context.apis.filter(linked_to=story.id)
    if not linked_apis:
        report.add_issue("CRITICAL", f"{story.id} 无对应 API 设计")
```

**产出**:
```yaml
prd_spec_match:
  matched: 4
  unmatched: 1
  score: 80%
  issues:
    - type: CRITICAL
      message: "US-005 无对应 API 设计"
```

---

### Layer 2: Spec ↔ Code (设计 ↔ 代码)
**检查项**:
- Spec 定义的 API 是否在 Controller 中实现？
- 是否存在 Ghost Code (代码有，Spec 无)？

**匹配逻辑**:
```python
for api in spec_context.apis:
    implemented = code_context.has_api(api.path)
    if not implemented:
        report.add_issue("CRITICAL", f"{api.path} 未实现")

for controller_api in code_context.all_apis:
    if not spec_context.has_api(controller_api):
        report.add_issue("WARNING", f"{controller_api} 为 Ghost Code")
```

**产出**:
```yaml
spec_code_match:
  backend_score: 80% (API Impl)
  frontend_score: 90% (Component Impl)
  issues:
    - type: CRITICAL
      message: "Component 'OrderList' defined in 02_frontend.md not found"
```

---

### Layer 3: Spec ↔ Tests (设计 ↔ 测试)
**检查项**:
- **Backend Tests**: 是否覆盖了 AC 和 API？
- **Frontend Tests**: 是否覆盖了组件交互和 UI 状态？

**产出**:
```yaml
spec_test_match:
  backend_coverage: 70%
  frontend_coverage: 60% (3 Component Tests missing)
  issues:
    - type: WARNING
      message: "OrderList.vue 无对应 spec 文件"
```

---

### Layer 4: Code ↔ Tests (代码 ↔ 测试)
**检查项**:
- Service 方法是否有单元测试？
- Frontend 组件是否有 Spec 文件？

**产出**:
```yaml
code_test_match:
  backend_ratio: 80%
  frontend_ratio: 50%
```

---

## 健康度计算

```python
overall_score = (
    prd_spec_match.score * 0.25 +
    spec_code_match.score * 0.35 +
    spec_test_match.score * 0.25 +
    code_test_match.score * 0.15
)
```

权重说明:
- Spec ↔ Code 权重最高 (35%)，因为"设计与实现不一致"是最严重的问题。
- PRD ↔ Spec 和 Spec ↔ Tests 各 25%。
- Code ↔ Tests 权重最低 (15%)，因为部分代码可能不需要单测。

## Checkpoint 输出模板
```
[CHECKPOINT - Step 2 Complete]

交叉比对完成。

📊 健康度评分:
- PRD ↔ Spec: 80% 🟡
- Spec ↔ Code: 75% 🟡
- Spec ↔ Tests: 70% 🟡
- Code ↔ Tests: 80% 🟢
- **综合: 76%** 🟡

🔴 Critical: 2 个
🟡 Warning: 5 个
🟢 Info: 3 个

是否生成详细报告？[Y/n]
```
