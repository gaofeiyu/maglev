---
description: maglev-plan-unit-tests-frontend Step 2 - Identify Test Targets
---

# Step 2: Identify Test Targets (识别测试目标)

## 目标
将 Spec 分析结果转化为具体的测试用例。

## 测试分类

### 2.1 组件测试 (Component Tests)
| 测试类型 | 说明 | 示例 |
|----------|------|------|
| Rendering | 组件是否正确渲染 | renders correctly |
| Props | Props 变化是否生效 | updates when prop changes |
| Events | 事件是否正确触发 | emits event on click |
| Slots | 插槽内容是否渲染 | renders slot content |
| Conditional | 条件渲染是否正确 | shows loading state |

### 2.2 Hook 测试 (Hook/Composable Tests)
| 测试类型 | 说明 | 示例 |
|----------|------|------|
| Initial State | 初始状态是否正确 | returns empty array initially |
| State Change | 状态变化是否正确 | updates on fetch |
| Side Effects | 副作用是否触发 | calls API on mount |
| Error Handling | 错误处理是否正确 | handles error state |

### 2.3 Store 测试 (Store Tests)
| 测试类型 | 说明 | 示例 |
|----------|------|------|
| Actions | Action 是否更新状态 | fetchOrders updates state |
| Getters | Getter 计算是否正确 | orderCount returns correct count |
| Mutations | 状态变更是否正确 | adds order to list |

## 输出格式
```yaml
test_targets:
  components:
    - file: OrderList.spec.ts
      tests:
        - name: renders order list correctly
          type: Rendering
          priority: HIGH
        - name: shows empty state when no orders
          type: Conditional
          priority: MEDIUM
        - name: triggers fetch on mount
          type: Side Effects
          priority: HIGH
        - name: handles delete click
          type: Events
          priority: HIGH
  hooks:
    - file: useOrderList.spec.ts
      tests:
        - name: returns orders from store
          type: Initial State
          priority: HIGH
        - name: handles loading state
          type: State Change
          priority: MEDIUM
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 2 Complete]

测试目标已识别。

📊 统计:
- Component Tests: 15 个
- Hook Tests: 6 个
- Store Tests: 10 个
- Total: 31 个测试用例

🔴 HIGH Priority: 12 个
🟡 MEDIUM Priority: 15 个
🟢 LOW Priority: 4 个

是否继续设计 Mock 策略？[Y/n]
```
