---
description: maglev-code-review-frontend Step 2 - Component Compliance
---

# Step 2: Component Compliance (组件合规性检查)

## 目标
检查前端组件是否符合 Spec 定义的接口和行为。

## 检查维度

### 2.1 Props 接口检查
**对比项**:
| Spec 定义 | 代码实现 | 检查点 |
|-----------|----------|--------|
| Prop 名称 | `defineProps()` / `props` | 是否一致 |
| Prop 类型 | TypeScript / PropType | 是否匹配 |
| Prop 必选 | `required` | 是否正确 |
| Prop 默认值 | `default` | 是否合理 |

**示例检查**:
```yaml
props_compliance:
  - prop: orderId
    spec_type: number
    code_type: String  # ❌ 类型不匹配
    status: FAIL
  - prop: showDetail
    spec_type: boolean
    code_type: boolean
    status: PASS
```

### 2.2 API 调用检查
**对比项**:
| Spec (`02_api.md`) | 代码实现 | 检查点 |
|--------------------|----------|--------|
| API 路径 | axios/fetch URL | 是否一致 |
| HTTP Method | get/post/delete | 是否匹配 |
| 请求参数 | params/body | 名称、类型是否一致 |
| 响应处理 | 解构字段 | 是否符合响应结构 |

**示例检查**:
```yaml
api_compliance:
  - api: GET /api/orders
    spec_params: [page: number, size: number]
    code_params: [pageNum: number, pageSize: number]  # ❌ 参数名不匹配
    status: FAIL
  - api: DELETE /api/orders/{id}
    spec_path: /api/orders/{id}
    code_path: /api/orders/${id}
    status: PASS
```

### 2.3 State/Store 结构检查
**对比项**:
| Spec (`02_frontend.md`) | 代码实现 | 检查点 |
|-------------------------|----------|--------|
| State 字段 | Store 定义 | 是否一致 |
| Action 方法 | Store 方法 | 是否实现 |
| Getter 计算 | Computed | 是否符合 |

### 2.4 事件处理检查
**对比项**:
- Spec 描述的用户交互是否在代码中实现
- 事件处理逻辑是否符合 Spec 描述

## Checkpoint 输出模板
```
[CHECKPOINT - Step 2 Complete]

组件合规性检查完成。

📊 结果:
- Props 接口: 3/4 符合 ⚠️
- API 调用: 1/2 符合 ⚠️
- State 结构: 符合 ✅
- 事件处理: 符合 ✅

❌ 问题 (2 个):
- [Props] orderId: Spec 定义为 number，实际为 String
- [API] GET /api/orders: 参数名 pageNum/pageSize 应为 page/size

是否继续检查代码质量？[Y/n]
```
