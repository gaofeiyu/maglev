---
name: 'step-12-complete'
description: 'Finalize PRD and Close Workflow (Standard v2.0)'

# File References
outputFile: '{outputFile}'
validationFlow: '../steps-v/step-v-01-discovery.md'
---

# 步骤 6: 工作流完成 (Standard v2.0)

**最后一步 - 完成 PRD**

## 强制执行规则:
- ✅ 这是一个最后步骤 - 不需要继续工作流
- 📋 检查 Frontmatter 状态
- 🎯 提供下一步指引

## 执行协议：

### 1. 宣布完成

通知用户:
- PRD 已生成: `{outputFile}`
- Slug: `{slug}`

### 2. 状态更新 (Frontmatter)

确保 `{outputFile}` 的 frontmatter 中的 `status` 被设置为 `Draft` 或 `Review`.

### 3. 下一步建议

Maglev 推荐的后续步骤:
1.  **Tech Design**: 运行 `maglev-design` (Pending Implementation)
2.  **Implementation**: 运行 `maglev-plan` (Pending Implementation)

目前，你可以直接开始 `02_design.md` 的编写。

**结束语:**
"PRD 已就绪。您现在可以运行 `/maglev-librarian` 来索引这个新 Spec。"

