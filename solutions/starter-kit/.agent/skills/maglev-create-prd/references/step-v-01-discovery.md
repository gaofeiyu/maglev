---
name: 'step-v-01-discovery'
description: '文档发现与确认 - 处理新上下文验证，确认 PRD 路径，发现输入文档'

# File references (ONLY variables used in this step)
nextStepFile: './step-v-02-format-detection.md'
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'

prdPurpose: '../data/prd-purpose.md'
---

# 步骤 1: 文档发现与确认

## 步骤目标：

通过确认 PRD 路径、从 frontmatter 发现并加载输入文档以及初始化验证报告来处理新上下文验证。

## 强制执行规则 (请先阅读):

### 通用规则：

- 🛑 绝不 在没有用户输入的情况下生成内容
- 📖 关键：在采取任何行动之前，请阅读完整的步骤文件
- 🔄 关键：当使用 'C' 加载下一步时，确保已阅读整个文件
- 📋 你是一个协调员，而不是内容生成器
- ✅ 你必须始终使用配置的 `{communication_language}` 以你的 Agent 沟通风格输出语言

### 角色强化：

- ✅ 你是验证架构师和质量保证专家
- ✅ 如果你已经被赋予了沟通或人物模式，在扮演这个新角色时继续使用它们
- ✅ 我们参与协作对话，而不是命令-响应
- ✅ 你带来系统验证专业知识和分析严谨性
- ✅ 用户带来领域专业知识和特定 PRD 上下文

### 步骤特定规则：

- 🎯 仅关注 发现 PRD 和输入文档，尚未验证
- 🚫 禁止 在此步骤中执行任何验证检查
- 💬 方法：带有清晰向用户报告的系统发现
- 🚪 这是设置步骤 - 准备好一切以进行验证

## 执行协议：

- 🎯 发现并确认要验证的 PRD
- 💾 加载 PRD 和来自 frontmatter 的所有输入文档
- 📖 在 PRD 旁边初始化验证报告
- 🚫 禁止 在用户确认设置之前加载下一步

## 上下文边界：

- 可用上下文：PRD 路径（用户指定或发现），工作流配置
- 重点：仅文档发现和设置
- 限制：不执行验证，不跳过发现
- 依赖项：从 PRD workflow.md 初始化加载配置

## 强制序列

**关键：** 严格遵循此序列。除非用户明确要求更改，否则不要跳过、重新排序或即兴发挥。

### 1. 加载 PRD 目的和标准

加载并阅读完整文件：
`{prdPurpose}`

此文件包含 BMAD PRD 哲学、标准和指导所有验证检查的验证标准。内化这种理解 - 它定义了什么构成了伟大的 BMAD PRD。

### 2. 发现要验证的 PRD

**如果作为调用参数提供了 PRD 路径：**
- 使用提供的路径

**如果未提供 PRD 路径：**
"**PRD 验证工作流**

你想验证哪个 PRD？

请提供你想验证的 PRD 文件的路径。"

**等待用户提供 PRD 路径。**

### 3. 验证 PRD 是否存在并加载

一旦提供 PRD 路径：

- 检查指定路径是否存在 PRD 文件
- 如果未找到："我无法在该路径找到 PRD。请检查路径并重试。"
- 如果找到：加载完整的 PRD 文件，包括 frontmatter

### 4. 提取 Frontmatter 和输入文档

从加载的 PRD frontmatter 中提取：

- `inputDocuments: []` 数组（如果存在）
- 任何其他相关元数据（分类、日期等）

**如果不存在 inputDocuments 数组：**
注意这一点并继续进行仅 PRD 验证

### 5. 加载输入文档

对于 `inputDocuments` 中列出的每个文档：

- 尝试加载文档
- 跟踪成功加载的文档
- 注意任何加载失败的文档

**构建已加载输入文档的列表：**
- 产品简介（如果存在）
- 研究文档（如果存在）
- 其他参考资料（如果存在）

### 6. 询问其他参考文档

"**我已经从你的 PRD frontmatter 加载了以下文档：**

{list loaded documents with file names}

**是否有你想在此验证中包含的其他参考文档？**

这些可能包括：
- 其他研究或上下文文档
- frontmatter 中未跟踪的项目文档
- 标准或合规性文档
- 竞争分析或基准

请提供任何其他文档的路径，或输入 'none' 以继续。"

**加载用户提供的任何其他文档。**

### 7. 初始化验证报告

在以下位置创建验证报告：`{validationReportPath}`

**使用 frontmatter 初始化：**
```yaml
---
validationTarget: '{prd_path}'
validationDate: '{current_date}'
inputDocuments: [list of all loaded documents]
validationStepsCompleted: []
validationStatus: IN_PROGRESS
---
```

**初始内容：**
```markdown
# PRD 验证报告

**正在验证的 PRD:** {prd_path}
**验证日期:** {current_date}

## 输入文档

{list all documents loaded for validation}

## 验证发现

[发现将随着验证进展追加]
```

### 8. 展示发现摘要

"**设置完成！**

**要验证的 PRD:** {prd_path}

**已加载输入文档:**
- PRD: {prd_name} ✓
- 产品简介: {count} {if count > 0}✓{else}(未找到){/if}
- 研究: {count} {if count > 0}✓{else}(未找到){/if}
- 其他参考: {count} {if count > 0}✓{else}(无){/if}

**验证报告:** {validationReportPath}

**准备开始验证。**"

### 9. 展示菜单选项

显示： **选择一个选项：** [A] 高级诱导 [P] 派对模式 [C] 继续到格式检测

#### 执行规则：

- 始终 在展示菜单后停止并等待用户输入
- 仅 当用户选择 'C' 时才进行下一步
- 用户可以提问或添加更多文档 - 始终响应并重新显示菜单

#### 菜单处理逻辑：

- 如果 A: 完整阅读并遵循：{advancedElicitationTask}，完成后重新显示菜单

- 如果 C: 完整阅读并遵循：{nextStepFile} 开始格式检测
- 如果 用户提供其他文档: 加载它，更新报告，重新显示摘要
- 如果 其他: 帮助用户，然后重新显示菜单

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 发现并确认 PRD 路径
- PRD 文件存在并成功加载
- 加载来自 frontmatter 的所有输入文档
- 加载其他参考文档（如果有）
- 在 PRD 旁边初始化验证报告
- 清楚地告知用户设置状态
- 正确展示菜单并处理用户输入

### ❌ 系统失败：

- 使用不存在的 PRD 文件继续
- 未加载来自 frontmatter 的输入文档
- 在错误位置创建验证报告
- 在未确认设置的情况下继续
- 未优雅处理缺失的输入文档

**主规则：** 验证前完成发现和设置。此步骤确保一切就绪以进行系统验证检查。
