---
description: maglev-code-review Step 2 - Compliance Check
---

# Step 2: Compliance Check (合规性检查)

## 目标
检查代码是否符合 Spec 定义的契约和行为。

## 检查维度

### 2.1 API 契约检查
**对比项**:
| Spec 定义 | 代码实现 | 检查点 |
|-----------|----------|--------|
| HTTP Method | `@GetMapping` | 方法是否匹配 |
| Path | `@RequestMapping("/api/orders")` | 路径是否匹配 |
| Request Params | `@RequestParam` | 参数名、类型是否匹配 |
| Request Body | `@RequestBody` | DTO 结构是否匹配 |
| Response Type | 返回类型 | 返回结构是否匹配 |

**示例检查**:
```yaml
api_compliance:
  - api: GET /api/orders
    spec_params: [page: int, size: int]
    code_params: [page: Integer, size: Integer]
    status: ✅ PASS
  - api: POST /api/orders
    spec_body: OrderCreateDTO {name, quantity}
    code_body: OrderCreateDTO {name, quantity, description}
    status: ⚠️ WARN (额外字段)
```

### 2.2 数据模型检查
**对比项**:
| Spec 定义 | 代码实现 | 检查点 |
|-----------|----------|--------|
| Entity 名称 | Class 名称 | 是否一致 |
| 字段名 | Field 名称 | 是否一致 |
| 字段类型 | Field 类型 | 是否匹配 |
| 关系 (1:N, N:M) | JPA 注解 | 是否正确 |

**示例检查**:
```yaml
model_compliance:
  - entity: Order
    fields:
      - name: status
        spec_type: Enum<PENDING, COMPLETED, CANCELLED>
        code_type: String
        status: ❌ FAIL (类型不匹配)
      - name: totalAmount
        spec_type: Decimal
        code_type: BigDecimal
        status: ✅ PASS
```

### 2.3 业务逻辑检查
**对比项**:
- Spec 描述的条件分支是否在代码中体现
- Spec 定义的校验规则是否实现

**示例检查**:
```yaml
logic_compliance:
  - rule: "订单金额不能为负数"
    spec_ref: 02_design.md#L45
    code_impl: "if (amount < 0) throw IllegalArgumentException"
    status: ✅ PASS
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 2 Complete]

合规性检查完成。

📊 结果:
- API 契约: 3/3 符合 ✅
- 数据模型: 2/3 符合 ⚠️
- 业务逻辑: 2/2 符合 ✅

❌ 问题 (1 个):
- [Model] Order.status: Spec 定义为 Enum，实际为 String

是否继续检查代码质量？[Y/n]
```
