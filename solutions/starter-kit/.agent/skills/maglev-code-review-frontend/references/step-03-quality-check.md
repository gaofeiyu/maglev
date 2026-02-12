---
description: maglev-code-review-frontend Step 3 - Quality Check
---

# Step 3: Quality Check (质量检查)

## 目标
检查前端代码质量和最佳实践。

## 检查维度

### 3.1 组件复用
| 检查项 | 标准 |
|--------|------|
| 重复代码 | 相似逻辑是否可抽取为公共组件/Hook |
| 组件职责 | 单一职责，不超过 200 行 |
| 组件拆分 | 复杂组件是否合理拆分子组件 |

### 3.2 响应式设计 (Vue/React)
| 检查项 | 标准 |
|--------|------|
| Vue | 正确使用 `ref`/`reactive`，避免直接修改 props |
| React | 正确使用 `useState`/`useReducer`，避免直接修改 state |
| 副作用 | `useEffect`/`watch` 依赖项完整 |

### 3.3 性能
| 检查项 | 风险 |
|--------|------|
| 缺少 key | 列表渲染无唯一 key |
| 不必要的 re-render | 未使用 memo/useMemo/computed |
| 大列表 | 未虚拟化 (> 100 项) |
| 异步加载 | 大组件未懒加载 |
| 图片优化 | 未使用懒加载/响应式图片 |

### 3.4 样式规范
| 检查项 | 标准 |
|--------|------|
| CSS 命名 | BEM / CSS Modules / Scoped |
| 主题变量 | 使用设计系统 Token，非硬编码颜色 |
| 响应式 | 正确使用断点，移动优先 |
| 单位 | 统一使用 rem/em，非 px (除非边框) |

### 3.5 安全性
| 检查项 | 风险 |
|--------|------|
| XSS | `v-html`/`dangerouslySetInnerHTML` 渲染用户输入 |
| 敏感数据 | Token/密码存储在 localStorage |
| CORS | 硬编码 API 地址 |

### 3.6 可访问性 (a11y)
| 检查项 | 标准 |
|--------|------|
| 语义化 | 使用语义化标签 (nav, main, article) |
| ARIA | 交互元素有 aria-label |
| 键盘导航 | 可键盘操作 |
| 颜色对比 | 文字与背景对比度足够 |

## Checkpoint 输出模板
```
[CHECKPOINT - Step 3 Complete]

质量检查完成。

📊 结果:
- 组件复用: ✅ 良好
- 响应式设计: ✅ 良好
- 性能: ⚠️ 2 个问题
- 样式规范: ✅ 良好
- 安全性: 🔴 1 个问题
- 可访问性: ⚠️ 1 个问题

🔴 Critical:
- [Security] v-html 渲染用户输入 (OrderList.vue:L45)

⚠️ Warning:
- [Performance] 列表项缺少 key (OrderList.vue:L55)
- [Performance] 未使用虚拟列表 (订单 > 100 条)
- [a11y] 删除按钮缺少 aria-label

是否生成 Review 意见？[Y/n]
```
