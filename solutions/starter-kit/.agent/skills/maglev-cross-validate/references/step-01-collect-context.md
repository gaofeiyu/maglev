---
description: maglev-cross-validate Step 1 - Collect Context
---

# Step 1: Collect Context (收集上下文)

## 目标
调用现有审计技能 + 内置扫描器，收集所有待验证的上下文信息。

## 执行逻辑

### 1.1 调用 maglev-audit-prd
**目的**: 获取 PRD 层面的结构化信息
**产出**:
```yaml
prd_context:
  user_stories:
    - id: US-001
      title: 查看订单列表
      acceptance_criteria:
        - AC-001: 显示订单表格
        - AC-002: 支持分页
  total_stories: 5
  total_acs: 12
```

### 1.2 调用 maglev-audit-spec
**目的**: 获取 Tech Spec 层面的结构化信息
**产出**:
```yaml
spec_context:
  apis:
    - path: GET /api/orders
      linked_to: US-001
    - path: DELETE /api/orders/{id}
      linked_to: US-002
  entities:
    - name: Order
    - name: OrderItem
  total_apis: 4
  total_entities: 2
```

### 1.3 Code Scanner (内置)
**目的**: 扫描代码目录，识别已实现的 API 和方法
**扫描规则**:
- Java: `*Controller.java` → 提取 `@RequestMapping`
- Python: `routers/*.py` → 提取 `@app.get/post`
- Node: `routes/*.js` → 提取 `router.get/post`

**产出**:
```yaml
code_context:
  backend:
    controllers:
      - file: OrderController.java
        apis_implemented: [GET /api/orders]
    services:
      - file: OrderService.java
  frontend:
    components:
      - file: OrderList.vue
      - file: OrderItem.tsx
    stores:
      - file: orderStore.ts
```

### 1.4 Test Scanner (内置)
**目的**: 扫描测试目录，识别已覆盖的场景
**扫描规则**:
- **Backend**: `*Test.java`, `test_*.py`
- **Frontend**: `*.spec.ts`, `*.test.tsx`, `__tests__/**/*.js`

**产出**:
```yaml
test_context:
  backend:
    - file: OrderControllerTest.java
  frontend:
    - file: OrderList.spec.ts
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 1 Complete]

上下文收集完成。

📊 统计:
- PRD: 5 User Stories, 12 ACs
- Spec: 4 APIs, 2 Entities
- Code: 3 Controllers, 5 Services
- Tests: 8 Test Files, 15 Test Methods

是否继续交叉比对？[Y/n]
```
