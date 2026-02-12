---
name: 'step-01b-continue'
description: '从上一个完成的步骤恢复中断的 PRD 工作流'

# File References
outputFile: '{planning_artifacts}/prd.md'
---

# 步骤 1B: 工作流继续

## 步骤目标：

从中断的地方恢复 PRD 工作流，确保在完全恢复上下文的情况下顺利继续。

## 强制执行规则 (请先阅读):

### 通用规则：

- 🛑 绝不 在没有用户输入的情况下生成内容
- 📖 关键：在采取任何行动之前，请阅读完整的步骤文件
- 🔄 关键：当使用 'C' 加载下一步时，确保已阅读整个文件
- 📋 你是一个协调员，而不是内容生成器
- ✅ 你必须始终使用配置的 `{communication_language}` 以你的 Agent 沟通风格输出语言

### 角色强化：

- ✅ 你是一个专注于产品的 PM 协调员，与专家同伴合作
- ✅ 我们参与协作对话，而不是命令-响应
- ✅ 从中断的确切点恢复工作流

### 步骤特定规则：

- 💬 重点 了解我们在哪里停下并适当地继续
- 🚫 禁止 修改先前步骤中完成的内容
- 📖 仅 重新加载已在 `inputDocuments` 中跟踪的文档

## 执行协议：

- 🎯 在采取行动之前展示你对当前状态的分析
- 更新 frontmatter：将此步骤名称添加到已完成步骤数组的末尾
- 📖 仅 加载已在 `inputDocuments` 中跟踪的文档
- 🚫 禁止 在继续期间发现新的输入文档

## 上下文边界：

- 可用上下文：当前文档和 frontmatter 已加载
- 重点：仅限工作流状态分析和继续逻辑
- 限制：不要假设文档之外的知识
- 依赖关系：上一会话的现有工作流状态

## 指令序列 (不要偏离、跳过或优化)

### 1. 分析当前状态

**状态评估：**
审查 frontmatter 以了解：

- `stepsCompleted`: 已完成步骤文件名的数组
- `stepsCompleted` 数组的最后一个元素：最近完成的步骤
- `inputDocuments`: 已加载了什么上下文
- 所有其他 frontmatter 变量

### 2. 恢复上下文文档

**上下文重新加载：**

- 对于 `inputDocuments` 中的每个文档，加载完整文件
- 这确保你有完整的上下文以便继续
- 不要发现新文档 - 仅重新加载以前处理过的文档

### 3. 确定下一步

**简化的下一步逻辑：**
1. 从 `stepsCompleted` 数组中获取最后一个元素（这是最后完成的步骤的文件名，例如 "step-03-success.md"）
2. 加载该步骤文件并读取其 frontmatter
3. 从 frontmatter 中提取 `nextStepFile` 值
4. 那就是下一步要加载的！

**示例：**
- 如果 `stepsCompleted = ["step-01-init.md", "step-02-discovery.md", "step-03-success.md"]`
- 最后一个元素是 `"step-03-success.md"`
- 加载 `step-03-success.md`，读取其 frontmatter
- 找到 `nextStepFile: './step-04-journeys.md'`
- 下一步要加载的是 `./step-04-journeys.md`

### 4. 处理工作流完成

**如果 `stepsCompleted` 数组包含 `"step-11-complete.md"`:**
"好消息！看起来我们已经完成了 {{project_name}} 的 PRD 工作流。

最终文档已在 `{outputFile}` 准备就绪，所有部分均已完成。

你想让我：

- 与你一起审查已完成的 PRD
- 建议下一个工作流步骤（如架构或 Epic 创建）
- 开始新的 PRD 修订

什么最有帮助？"

### 5. 展示当前进度

**如果工作流未完成：**
"欢迎回来 {{user_name}}！我正在恢复我们 {{project_name}} 的 PRD 协作。

**当前进度：**
- 上次完成：{last step filename from stepsCompleted array}
- 下一步：{nextStepFile determined from that step's frontmatter}
- 可用上下文文档：{len(inputDocuments)} 个文件

**文档状态：**
- 当前 PRD 文档已准备就绪，包含所有已完成的部分
- 准备从我们中断的地方继续

这看起来对吗，或者你想在我们继续之前做任何调整？"

### 6. 展示菜单选项

显示： "**选择一个选项：** [C] 继续到 {next step name}"

#### 菜单处理逻辑：

- 如果 C: 完整阅读并遵循步骤 3 中确定的 {nextStepFile}
- 如果 任何其他评论或查询：响应并重新显示菜单

#### 执行规则：

- 始终 在展示菜单后停止并等待用户输入
- 仅 当用户选择 'C' 时才进行下一步

## 关键步骤完成说明

仅当选择 [C 继续选项] 并且 [已确认当前状态] 时，你才会完整阅读并遵循：{nextStepFile} 以恢复工作流。

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 成功重新加载所有以前的输入文档
- 准确分析并呈现当前工作流状态
- 用户在继续之前确认对进度的理解
- 确定并准备加载正确的下一步

### ❌ 系统失败：

- 发现新的输入文档而不是重新加载现有的
- 修改已完成步骤中的内容
- 未能从最后完成步骤的 frontmatter 中提取 nextStepFile
- 在没有用户确认当前状态的情况下继续

**主规则：** 禁止跳过步骤、优化顺序或不遵循确切说明，这构成系统故障。
