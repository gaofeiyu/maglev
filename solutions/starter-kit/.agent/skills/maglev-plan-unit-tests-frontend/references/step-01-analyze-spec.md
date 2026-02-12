---
description: maglev-plan-unit-tests-frontend Step 1 - Analyze Spec
---

# Step 1: Analyze Spec (分析规格)

## 目标
读取 Tech Spec，提取可测试的前端目标。

## 执行逻辑

### 1.1 读取 Spec 文件
优先级：
1. `02_frontend.md` (主设计文档)
2. 组件文件直接分析

### 1.2 提取测试目标

**Components (组件)**:
```yaml
components:
  - name: OrderList
    type: Page Component
    props: []
    events: []
    dependencies: [OrderItem, OrderFilter]
  - name: OrderItem
    type: List Item
    props: [order: Order]
    events: [onDelete, onEdit]
```

**Hooks/Composables (逻辑)**:
```yaml
hooks:
  - name: useOrderList
    returns: [orders, loading, error, fetchOrders]
    dependencies: [orderStore]
  - name: useOrderForm
    returns: [form, validate, submit]
```

**Store/State (状态)**:
```yaml
store:
  - name: orderStore
    state: [orders, currentOrder, loading]
    actions: [fetchOrders, createOrder, updateOrder, deleteOrder]
    getters: [orderCount, pendingOrders]
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 1 Complete]

Spec 分析完成。

📋 提取结果:
- Components: 5 个
  - OrderList (Page)
  - OrderItem (List Item)
  - OrderFilter (Filter)
  - OrderForm (Form)
  - OrderDetail (Detail)
- Hooks: 2 个
  - useOrderList
  - useOrderForm
- Store: 1 个
  - orderStore (4 actions, 2 getters)

是否继续识别测试目标？[Y/n]
```
