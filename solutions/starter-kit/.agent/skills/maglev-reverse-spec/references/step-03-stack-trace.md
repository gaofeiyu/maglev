---
description: maglev-reverse-spec Step 3 - Stack Trace
---

# Step 3: Stack Trace (全栈追踪)

## 目标
从 Step 2 识别的 API 入口，追踪后端调用链：`Controller -> Service -> Repository -> Entity`。

## 执行逻辑

### 3.1 Controller 定位
根据 API 路径 (e.g., `/api/orders`)，在后端代码中查找对应的 Handler。

### 3.2 Service & Repository 追踪
递归追踪 Service 层和 Repository 层的调用。

### 3.3 数据实体识别 (Critical)
必须识别核心数据模型 (Entity)，以重建 Data Model。

### 3.4 输出格式 (Strict YAML)
**注意**: 所有描述性文字（purpose, fields explanation）必须使用中文。

```yaml
stack_trace:
  api: GET /api/orders
  controller:
    file: OrderController.java
    method: getOrders()
    lines: 25-40
  service:
    file: OrderServiceImpl.java
    method: listOrders()
  repository:
    file: OrderRepository.java
    method: findAll()
  entities:
    - name: Order
      fields: [id, userId, status]
      relation: "One to Many with OrderItem"
```

## Checkpoint 输出模板 (中文)
```
[CHECKPOINT - Step 3 Complete]

✅ 后端追踪完成: GET /api/orders

🔗 调用链:
Controller: OrderController.java
    ↓
Service: OrderServiceImpl.java
    ↓
Repository: OrderRepository.findAll()

📊 数据模型:
- Order [id, userId, status...]

是否进入意图推测 (Intent) ? [Y/n]
```

## 复杂情况处理
- **External**: 外部调用标记为 `[外部依赖]`。
- **Async**: 消息队列标记为 `[异步事件]`。
