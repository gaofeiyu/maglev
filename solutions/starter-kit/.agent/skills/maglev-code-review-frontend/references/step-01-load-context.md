---
description: maglev-code-review-frontend Step 1 - Load Context
---

# Step 1: Load Context (加载上下文)

## 目标
加载待审查的前端代码变更和关联的 Spec 文件。

## 执行逻辑

### 1.1 识别代码变更
根据输入方式，获取组件内容：

**支持的文件类型**:
- Vue: `.vue`
- React: `.tsx`, `.jsx`
- Angular: `.component.ts`, `.component.html`
- Svelte: `.svelte`

### 1.2 关联 Spec 匹配
尝试自动匹配关联的 Spec：

**匹配策略**:
1. 检查组件注释中的 Spec 引用
2. 根据文件路径推断 (e.g., `views/order/` → `reverse_order_management`)
3. 检查 `specs/README.md` 索引

**需要加载的 Spec**:
- `02_frontend.md`: 组件设计、Props 定义、State 结构
- `02_api.md`: API 契约 (用于验证前端 API 调用)

### 1.3 提取审查范围
```yaml
review_scope:
  file: src/views/order/OrderList.vue
  framework: Vue 3
  components:
    - OrderList (主组件)
    - OrderItem (子组件引用)
    - OrderFilter (子组件引用)
  api_calls:
    - GET /api/orders
    - DELETE /api/orders/{id}
  store_usage:
    - orderStore.orders
    - orderStore.fetchOrders()
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 1 Complete]

上下文已加载。

📁 代码变更:
- 文件: src/views/order/OrderList.vue
- 框架: Vue 3 + Composition API
- 变更行: +65 / -20

📋 关联 Spec:
- 前端设计: specs/.../02_frontend.md
- API 契约: specs/.../02_api.md

🧩 组件涉及:
- OrderList, OrderItem, OrderFilter

📡 API 调用:
- GET /api/orders
- DELETE /api/orders/{id}

是否继续检查组件合规性？[Y/n]
```
