---
description: maglev-code-review-frontend Step 4 - Generate Review
---

# Step 4: Generate Review (生成 Review)

## 目标
将 Step 2 和 Step 3 的检查结果合并，生成结构化的 Review 意见。

## 输出格式

### Review 分级
| 级别 | 含义 | 操作 |
|------|------|------|
| 🔴 **Blocking** | 必须修复才能合并 | 阻止 PR |
| 🟡 **Non-Blocking** | 建议修复 | 可合并，跟进 |
| 🟢 **Good** | 值得肯定 | 正向反馈 |

### 前端分级规则
| 问题类型 | 级别 |
|----------|------|
| XSS 风险 | 🔴 Blocking |
| Props 类型不匹配 | 🔴 Blocking |
| API 参数不一致 | 🟡 Non-Blocking |
| 缺少 key | 🟡 Non-Blocking |
| 可访问性问题 | 🟡 Non-Blocking |
| 样式不规范 | 🟡 Non-Blocking |

## Review 模板
```markdown
## Code Review: {filename}

### 📊 总评
- **合规性**: {emoji} {summary}
- **质量**: {emoji} {summary}
- **建议**: {verdict}

---

### 🔴 必须修复 (Blocking)

#### [{category}] {title}
**位置**: `{file}:{line}`
**问题**: {description}
**建议**:
```{language}
// 修改建议代码
```

---

### 🟡 建议修复 (Non-Blocking)

#### [{category}] {title}
**位置**: `{file}:{line}`
**问题**: {description}
**建议**:
```{language}
// 修改建议代码
```

---

### 🟢 Good (值得肯定)
- {positive_feedback_1}
- {positive_feedback_2}
```

## 最终输出模板
```
[Step 4 Complete]

✅ Review 意见已生成！

📊 总结:
- 🔴 Blocking: 1 个 (必须修复)
- 🟡 Non-Blocking: 4 个 (建议修复)
- 🟢 Good: 2 个 (肯定)

建议:
1. 修复 XSS 风险后重新提交
2. 其他问题可在后续迭代处理

Review 内容已复制到剪贴板，可直接粘贴到 PR。
```
