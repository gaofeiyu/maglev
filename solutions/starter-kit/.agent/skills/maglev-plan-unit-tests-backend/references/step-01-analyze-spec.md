---
description: maglev-plan-unit-tests-backend Step 1 - Analyze Spec
---

# Step 1: Analyze Spec (分析规格)

## 目标
读取 Tech Spec，提取可测试的目标。

## 执行逻辑

### 1.1 读取 Spec 文件
优先级：
1. `02_design.md` (主设计文档)
2. `02_api.md` (API 详情)
3. `02_schema.md` (数据模型详情)

### 1.2 提取测试目标

**API Endpoints (Controller 层)**:
```yaml
apis:
  - method: GET
    path: /api/orders
    params: [page, size, status]
    response: List<OrderDTO>
  - method: POST
    path: /api/orders
    body: OrderCreateDTO
    response: OrderDTO
```

**Business Rules (Service 层)**:
```yaml
business_rules:
  - name: 订单金额校验
    description: 订单金额不能为负数
    testable: true
  - name: 库存检查
    description: 下单前检查库存是否充足
    testable: true
  - name: 状态流转
    description: 订单状态只能 PENDING → COMPLETED/CANCELLED
    testable: true
```

**Data Access (Repository 层)**:
```yaml
entities:
  - name: Order
    fields: [id, userId, status, totalAmount, createdAt]
    queries: [findByUserId, findByStatus]
  - name: OrderItem
    fields: [id, orderId, sku, quantity, price]
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 1 Complete]

Spec 分析完成。

📋 提取结果:
- APIs: 4 个 (GET, POST, PUT, DELETE)
- Business Rules: 3 个
  - 订单金额校验
  - 库存检查
  - 状态流转
- Entities: 2 个 (Order, OrderItem)
- Custom Queries: 2 个 (findByUserId, findByStatus)

是否继续识别测试目标？[Y/n]
```
