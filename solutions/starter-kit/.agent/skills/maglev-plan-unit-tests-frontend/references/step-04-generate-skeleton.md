---
description: maglev-plan-unit-tests-frontend Step 4 - Generate Test Skeleton
---

# Step 4: Generate Test Skeleton (生成测试骨架)

## 目标
输出可执行的前端测试代码框架。

## 输出路径
根据项目结构自动确定：
- Vue: `src/components/__tests__/{Component}.spec.ts`
- React: `src/components/{Component}/{Component}.test.tsx`

## Vue 组件测试模板 (Vitest)

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount, VueWrapper } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import OrderList from '../OrderList.vue'
import { useOrderStore } from '@/stores/order'

describe('OrderList', () => {
  let wrapper: VueWrapper

  beforeEach(() => {
    vi.clearAllMocks()
  })

  // ===== Rendering =====

  describe('rendering', () => {
    it('renders order list correctly', () => {
      wrapper = mount(OrderList, {
        global: {
          plugins: [
            createTestingPinia({
              initialState: {
                order: { orders: [{ id: 1, name: 'Test' }] }
              }
            })
          ]
        }
      })

      expect(wrapper.findAll('[data-testid="order-item"]')).toHaveLength(1)
    })

    it('shows empty state when no orders', () => {
      // TODO: Implement
    })

    it('shows loading spinner when loading', () => {
      // TODO: Implement
    })
  })

  // ===== Interactions =====

  describe('interactions', () => {
    it('calls fetchOrders on mount', async () => {
      wrapper = mount(OrderList, {
        global: {
          plugins: [createTestingPinia({ stubActions: false })]
        }
      })

      const store = useOrderStore()
      expect(store.fetchOrders).toHaveBeenCalled()
    })

    it('emits delete event when delete button clicked', async () => {
      // TODO: Implement
    })
  })
})
```

## Vue Hook 测试模板 (Vitest)

```typescript
import { describe, it, expect, vi } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useOrderList } from '../useOrderList'
import { useOrderStore } from '@/stores/order'

describe('useOrderList', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('returns orders from store', () => {
    const store = useOrderStore()
    store.orders = [{ id: 1, name: 'Test' }]

    const { orders } = useOrderList()

    expect(orders.value).toHaveLength(1)
  })

  it('handles loading state', () => {
    // TODO: Implement
  })
})
```

## Vue Store 测试模板 (Vitest)

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useOrderStore } from '../order'
import * as api from '@/api/order'

vi.mock('@/api/order')

describe('orderStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
    vi.clearAllMocks()
  })

  describe('actions', () => {
    it('fetchOrders updates state', async () => {
      vi.mocked(api.getOrders).mockResolvedValue([{ id: 1 }])

      const store = useOrderStore()
      await store.fetchOrders()

      expect(store.orders).toHaveLength(1)
    })

    it('createOrder adds to list', async () => {
      // TODO: Implement
    })
  })

  describe('getters', () => {
    it('orderCount returns correct count', () => {
      const store = useOrderStore()
      store.orders = [{ id: 1 }, { id: 2 }]

      expect(store.orderCount).toBe(2)
    })
  })
})
```

## 最终输出模板
```
[Step 4 Complete]

✅ 测试骨架已生成！

📁 输出文件:
- src/views/__tests__/OrderList.spec.ts
- src/composables/__tests__/useOrderList.spec.ts
- src/stores/__tests__/order.spec.ts

📊 统计:
- 测试文件: 3 个
- 测试用例: 31 个
- 已填充示例: 6 个
- 待实现 (TODO): 25 个

下一步:
1. 填充 TODO 部分的测试逻辑
2. 运行 `npm run test:unit` 验证
3. 使用 maglev-cross-validate 检查覆盖率
```
