---
description: maglev-plan-unit-tests-backend Step 2 - Identify Test Targets
---

# Step 2: Identify Test Targets (识别测试目标)

## 目标
将 Spec 分析结果转化为具体的测试方法签名。

## 执行逻辑

### 2.1 测试命名规范
```
test{Method}_{Scenario}
```
- `{Method}`: 被测方法名
- `{Scenario}`: Success / EmptyResult / InvalidInput / Exception

### 2.2 按层级生成测试目标

**Controller 层**:
| API | 测试方法 | 场景 |
|-----|----------|------|
| GET /api/orders | testGetOrders_Success | 正常返回列表 |
| GET /api/orders | testGetOrders_EmptyList | 无数据返回空列表 |
| GET /api/orders | testGetOrders_InvalidPage | 分页参数非法 |
| POST /api/orders | testCreateOrder_Success | 正常创建 |
| POST /api/orders | testCreateOrder_InvalidInput | 缺少必填字段 |

**Service 层**:
| 业务规则 | 测试方法 | 场景 |
|----------|----------|------|
| 金额校验 | testCalculateTotalAmount_Normal | 正常计算 |
| 金额校验 | testCalculateTotalAmount_WithDiscount | 有折扣 |
| 金额校验 | testCalculateTotalAmount_NegativePrice | 负价格抛异常 |
| 库存检查 | testCheckStock_Sufficient | 库存充足 |
| 库存检查 | testCheckStock_Insufficient | 库存不足抛异常 |

**Repository 层**:
| Query | 测试方法 | 场景 |
|-------|----------|------|
| findByUserId | testFindByUserId_Found | 找到数据 |
| findByUserId | testFindByUserId_NotFound | 无数据 |

### 2.3 输出格式
```yaml
test_targets:
  controller:
    - class: OrderControllerTest
      methods:
        - name: testGetOrders_Success
          scenario: 正常返回列表
          priority: HIGH
        - name: testGetOrders_EmptyList
          scenario: 无数据返回空列表
          priority: MEDIUM
  service:
    - class: OrderServiceTest
      methods:
        - name: testCalculateTotalAmount_Normal
          scenario: 正常计算
          priority: HIGH
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 2 Complete]

测试目标已识别。

📊 统计:
- Controller Tests: 8 个
- Service Tests: 12 个
- Repository Tests: 4 个
- Total: 24 个测试方法

🔴 HIGH Priority: 10 个
🟡 MEDIUM Priority: 10 个
🟢 LOW Priority: 4 个

是否继续设计 Mock 策略？[Y/n]
```
