---
description: maglev-reverse-spec Step 2 - Page Analysis
---

# Step 2: Page Analysis (页面分析)

## 目标
深入分析用户选定的页面，理解其 UI 结构、组件层次和 API 调用关系。

## 前置条件
- Step 1 已完成，用户已选择目标功能。
- `feature_context.frontend` 已确定 (e.g., `OrderList.vue`)。

## 执行逻辑

### 2.1 组件树解析 (Component Tree)
读取页面文件，提取：
- **组件引用**: `import XxxComponent from ...`
- **模板结构**: `<template>` 中的主要 DOM 结构
- **Props / State**: `props`, `data()`, `ref()` 等

输出示例 (YAML):
```yaml
component_tree:
  root: OrderList.vue
  children:
    - name: OrderTable
      type: table
      props: [columns, data, loading]
```

### 2.2 API 调用提取 (API Calls)
扫描页面及其子组件中的 HTTP 调用：
- `axios.get/post/put/delete`
- `fetch()`
- `useFetch()` / `useQuery()`
- `useFetch()` / `useQuery()` (如果是 React Query / SWR)

输出示例 (YAML):
```yaml
api_calls:
  - method: GET
    path: /api/orders
    purpose: 获取订单列表 # 必须使用中文描述
```

### 2.3 事件流识别 (Event Flow)
识别关键用户交互：
- 按钮点击 (`@click`)
- 表单提交 (`@submit`)
- 生命周期 (`onMounted`)

输出示例 (YAML):
```yaml
event_flow:
  - trigger: 页面加载
    action: 调用 GET /api/orders
  - trigger: 点击删除按钮
    action: 调用 DELETE /api/orders/{id}
```

## Checkpoint 输出模板 (中文)
```
[CHECKPOINT - Step 2 Complete]

✅ 页面分析完成: `OrderList.vue`

📦 组件结构:
- OrderTable (数据表格)
- Pagination (分页控件)

🌐 API 调用:
- GET /api/orders -> 获取订单列表
- DELETE /api/orders/{id} -> 删除订单
```

## 纯后端项目处理
如果 Step 1 未检测到前端，跳过此步骤，直接进入 Step 3。
