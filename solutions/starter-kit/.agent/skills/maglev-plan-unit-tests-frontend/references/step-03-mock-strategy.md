---
description: maglev-plan-unit-tests-frontend Step 3 - Design Mock Strategy
---

# Step 3: Design Mock Strategy (设计 Mock 策略)

## 目标
确定每个测试需要 Mock 的依赖。

## Mock 原则

### 3.1 层级 Mock 策略

| 测试层级 | Mock 对象 | 不 Mock |
|----------|-----------|---------|
| **Component** | Store, Router, API | DOM 渲染 |
| **Hook** | Store, API | 响应式逻辑 |
| **Store** | API (axios/fetch) | 状态管理逻辑 |

### 3.2 常用 Mock 方式

**Vue (Vitest)**:
```typescript
// Mock Store
import { createTestingPinia } from '@pinia/testing'
const wrapper = mount(Component, {
  global: { plugins: [createTestingPinia()] }
})

// Mock Router
import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({ history: createWebHistory(), routes: [] })

// Mock API
vi.mock('@/api/order', () => ({
  getOrders: vi.fn(() => Promise.resolve([]))
}))
```

**React (Vitest)**:
```typescript
// Mock Store (Zustand)
vi.mock('@/stores/order', () => ({
  useOrderStore: vi.fn(() => ({ orders: [], fetchOrders: vi.fn() }))
}))

// Mock Router
vi.mock('react-router-dom', () => ({
  useNavigate: () => vi.fn(),
  useParams: () => ({ id: '1' })
}))

// Mock API
vi.mock('@/api/order', () => ({
  getOrders: vi.fn(() => Promise.resolve([]))
}))
```

### 3.3 Mock 策略输出

```yaml
mock_strategy:
  - test_file: OrderList.spec.ts
    mocks:
      - target: orderStore
        method: createTestingPinia
      - target: useRouter
        method: vi.mock
  - test_file: useOrderList.spec.ts
    mocks:
      - target: orderStore
        method: createTestingPinia
  - test_file: orderStore.spec.ts
    mocks:
      - target: axios
        method: vi.mock
        stubs:
          - get: Promise.resolve({ data: [] })
          - post: Promise.resolve({ data: { id: 1 } })
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 3 Complete]

Mock 策略已设计。

📋 OrderList.spec.ts:
- Mock: orderStore (createTestingPinia)
- Mock: useRouter (vi.mock)

📋 useOrderList.spec.ts:
- Mock: orderStore (createTestingPinia)

📋 orderStore.spec.ts:
- Mock: axios (vi.mock)

是否生成测试骨架代码？[Y/n]
```
