---
description: maglev-create-test-cases Step 4 - Coverage Check
---

# Step 4: Coverage Check (覆盖率检查)

## 目标
检查生成的测试用例是否覆盖了所有 Acceptance Criteria。

## 执行逻辑

### 4.1 构建覆盖矩阵
```yaml
coverage_matrix:
  - ac_id: AC-001
    description: 显示订单表格
    test_cases: [TC-U-001, TC-I-001]
    status: ✅ Covered
  - ac_id: AC-007
    description: 超时重试
    test_cases: []
    status: ❌ Uncovered
```

### 4.2 计算覆盖率
```python
covered = len([ac for ac in matrix if ac.test_cases])
total = len(matrix)
coverage_rate = covered / total * 100
```

### 4.3 识别遗漏原因
| 遗漏类型 | 说明 | 处理建议 |
|----------|------|----------|
| 边缘场景 | AC 描述了异常情况 | 补充 Unit Test |
| 复杂交互 | 涉及多系统 | 补充 Integration Test |
| UI 相关 | 涉及界面状态 | 补充 E2E Test |

## Checkpoint 输出模板
```
[CHECKPOINT - Step 4 Complete]

覆盖率检查完成。

📊 覆盖率: 11/12 (92%)

✅ 已覆盖:
- AC-001, AC-002, AC-003, AC-004, AC-005
- AC-006, AC-008, AC-009, AC-010, AC-011, AC-012

❌ 未覆盖:
- AC-007: 超时重试 (建议补充 Unit Test)

是否补充缺失用例？[Y/n/skip]
- Y: 自动生成补充用例
- n: 退出
- skip: 跳过，继续输出
```

## 自动补充逻辑
如果用户选择 `Y`，针对每个未覆盖的 AC：
1. 分析 AC 类型 (边缘/复杂/UI)
2. 生成对应层级的测试用例
3. 追加到 Step 3 的输出中
