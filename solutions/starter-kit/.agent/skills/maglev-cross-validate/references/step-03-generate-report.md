---
description: maglev-cross-validate Step 3 - Generate Report
---

# Step 3: Generate Report (生成报告)

## 目标
将 Step 2 的比对结果输出为结构化的验证报告。

## 输出路径
```
specs/{feature}/validation_report.md
```

## 报告模板

```markdown
---
title: "{Feature Name} - 交叉验证报告"
generated_at: {timestamp}
generator: maglev-cross-validate v1.0
---

# 交叉验证报告

## 执行摘要

| 维度 | 得分 | 状态 |
|------|------|------|
| PRD ↔ Spec | {score}% | {emoji} |
| Spec ↔ Code (Back) | {score}% | {emoji} |
| Spec ↔ Code (Front) | {score}% | {emoji} |
| Spec ↔ Tests | {score}% | {emoji} |
| Code ↔ Tests | {score}% | {emoji} |
| **综合** | **{overall}%** | {emoji} |

### 状态图例
- 🟢 ≥ 90%: 健康
- 🟡 70-89%: 需要关注
- 🔴 < 70%: 需要立即修复

---

## 发现问题

### 🔴 Critical (必须修复)
> 这些问题会导致功能缺失或行为不一致。

- [ ] {issue_1}
- [ ] {issue_2}

### 🟡 Warning (建议修复)
> 这些问题可能导致维护困难或测试覆盖不足。

- [ ] {issue_3}
- [ ] {issue_4}

### 🟢 Info (参考信息)
> 这些是优化建议，不影响功能正确性。

- [ ] {issue_5}

---

## 详细分析

### PRD ↔ Spec 追溯
| User Story | 关联 API/UI | 状态 |
|------------|-------------|------|
| US-001 | GET /api/orders, OrderList | ✅ |
| US-002 | DELETE /api/orders/{id} | ✅ |
| US-005 | - | ❌ 未关联 |

### Spec ↔ Code (Backend)
| API 定义 | Controller 实现 | 状态 |
|----------|-----------------|------|
| GET /api/orders | OrderController.getOrders | ✅ |
| DELETE /api/orders/{id} | - | ❌ 未实现 |

### Spec ↔ Code (Frontend)
| 组件定义 | 组件文件 | 状态 |
|----------|----------|------|
| OrderList | OrderList.vue | ✅ |
| OrderDetail | - | ❌ 缺失 |

### Ghost Code (代码有，Spec 无)
| 代码位置 | API/方法 | 建议 |
|----------|----------|------|
| OrderController.java:L45 | PATCH /api/orders/{id}/status | 补充 Spec 或删除代码 |
| OrderDebug.vue | - | 移除调试组件 |

### 测试覆盖
| AC | 测试用例 (Back/Front) | 状态 |
|----|-----------------------|------|
| AC-001 | testGetOrdersSuccess / renders list | ✅ |
| AC-007 | - | ❌ 未覆盖 |

---

## 建议行动

1. **立即**: 修复 Critical 问题 (缺失的 API 和组件)
2. **本周**: 补充缺失的 Front/Back 测试用例
3. **下周**: 清理 Ghost Code 或补充 Spec
```

## 最终输出模板
```
[Step 3 Complete]

✅ 验证报告已生成！

📄 报告路径: specs/{feature}/validation_report.md

📊 总结:
- 综合健康度: 76%
- Critical: 2 个 (需立即修复)
- Warning: 5 个 (建议修复)

建议使用 `maglev-quick-dev` 修复 Critical 问题后，重新运行验证。
```
