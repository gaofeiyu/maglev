---
description: maglev-plan-unit-tests-backend Step 3 - Design Mock Strategy
---

# Step 3: Design Mock Strategy (设计 Mock 策略)

## 目标
确定每个测试类需要 Mock 的依赖和 Stub 行为。

## 执行逻辑

### 3.1 层级 Mock 原则

| 测试层级 | Mock 对象 | 不 Mock |
|----------|-----------|---------|
| **Controller** | Service | HTTP 请求响应 (MockMvc) |
| **Service** | Repository, 外部 Client | 业务逻辑 |
| **Repository** | - (集成测试) | 使用 H2/TestContainers |

### 3.2 Mock 策略设计

**OrderControllerTest**:
```yaml
mocks:
  - dependency: OrderService
    type: @Mock
    stubs:
      - method: getOrders(page, size)
        returns: List<OrderDTO>
      - method: createOrder(dto)
        returns: OrderDTO
```

**OrderServiceTest**:
```yaml
mocks:
  - dependency: OrderRepository
    type: @Mock
    stubs:
      - method: findByUserId(userId)
        returns: List<Order>
      - method: save(order)
        returns: Order with ID
  - dependency: InventoryClient
    type: @Mock
    stubs:
      - method: getStock(sku)
        returns: Integer (stock count)
      - method: reserveStock(sku, quantity)
        returns: Boolean
```

**OrderRepositoryTest**:
```yaml
strategy: Integration Test
database: H2 in-memory
setup: @DataJpaTest
```

### 3.3 常见 Mock 库

| 语言 | Mock 库 | 断言库 |
|------|---------|--------|
| Java | Mockito | AssertJ |
| Python | unittest.mock / pytest-mock | pytest |
| Go | testify/mock | testify/assert |
| Node | Jest mock | Jest expect |

## Checkpoint 输出模板
```
[CHECKPOINT - Step 3 Complete]

Mock 策略已设计。

📋 OrderControllerTest:
- @Mock: OrderService

📋 OrderServiceTest:
- @Mock: OrderRepository
- @Mock: InventoryClient

📋 OrderRepositoryTest:
- Strategy: H2 in-memory (@DataJpaTest)

是否生成测试骨架代码？[Y/n]
```
