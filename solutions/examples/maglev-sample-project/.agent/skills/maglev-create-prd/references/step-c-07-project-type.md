---
name: 'step-07-project-type'
description: '使用 CSV 驱动的指导进行项目类型特定的发现'

# File References
nextStepFile: './step-08-scoping.md'
outputFile: '{planning_artifacts}/prd.md'

# Data Files
projectTypesCSV: '../data/project-types.csv'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'
partyModeWorkflow: 'references/party-mode.workflow.md'
---

# 步骤 7: 项目类型深度剖析

**进度：第 7 步，共 11 步** - 下一步：范围界定

## 强制执行规则 (请先阅读):

- 🛑 绝不 在没有用户输入的情况下生成内容

- 📖 关键：始终 在采取任何行动之前阅读完整的步骤文件 - 部分理解导致不完整的决定
- 🔄 关键：当使用 'C' 加载下一步时，确保在继续之前阅读并理解整个文件
- ✅ 始终 将此视为 PM 同伴之间的协作发现
- 📋 你是一个协调员，而不是内容生成器
- 💬 重点 关注特定于项目类型的要求和技术考虑因素
- 🎯 数据驱动：使用 CSV 配置来指导发现
- ✅ 你必须始终使用配置的 `{communication_language}` 以你的 Agent 沟通风格输出语言

## 执行协议：

- 🎯 在采取任何行动之前展示你的分析
- ⚠️ 在生成项目类型内容后展示 A/P/C 菜单
- 💾 仅 当用户选择 C (继续) 时保存
- 📖 更新输出文件 frontmatter，将此步骤名称添加到 stepsCompleted 列表的末尾
- 🚫 禁止 在选择 C 之前加载下一步

## 上下文边界：

- 来自先前步骤的当前文档和 frontmatter 可用
- 来自 step-02 的项目类型可用于配置加载
- 项目类型 CSV 数据将在此步骤中加载
- 专注于特定于此项目类型的技术和功能要求

## 你的任务：

使用 CSV 驱动的指导进行项目类型特定的发现，以定义技术要求。

## 项目类型发现序列：

### 1. 加载项目类型配置数据

**尝试子流程数据查找：**

"你的任务：在 {projectTypesCSV} 中查找数据

**搜索标准：**
- 查找 project_type 匹配 {{projectTypeFromStep02}} 的行

**返回格式：**
仅返回匹配的行作为 YAML 格式的对象，包含以下字段：
project_type, key_questions, required_sections, skip_sections, innovation_signals

**不要返回整个 CSV - 仅返回匹配的行。**"

**优雅降级（如果任务工具不可用）：**
- 直接加载 CSV 文件
- 手动查找匹配的行
- 提取所需字段：
  - `key_questions` (发现问题的分号分隔列表)
  - `required_sections` (要记录的部分的分号分隔列表)
  - `skip_sections` (要跳过的部分的分号分隔列表)
  - `innovation_signals` (已在 step-6 中探索)

### 2. 使用关键问题进行引导式发现

从 CSV 解析 `key_questions` 并探索每一个：

#### 基于问题的发现：

对于 CSV 中 `key_questions` 的每个问题：

- 以对话风格自然地询问用户
- 倾听他们的回答并提出澄清性跟进问题
- 将答案连接到产品价值主张

**示例流程：**
如果 key_questions = "Endpoints needed?;Authentication method?;Data formats?;Rate limits?;Versioning?;SDK needed?"

自然地问：

- "你的 API 需要暴露哪些主要端点？"
- "你将如何处理认证和授权？"
- "你将支持哪些数据格式用于请求和响应？"

### 3. 记录项目类型特定要求

根据用户对 key_questions 的回答，综合全面的要求：

#### 要求类别：

覆盖 CSV 中 `required_sections` 指示的领域：

- 综合每个所需部分的发现内容
- 记录具体要求、约束和决策
- 适当时连接到产品差异化因素

#### 跳过不相关的部分：

跳过 CSV 中 `skip_sections` 指示的领域，以避免在不相关方面浪费时间。

### 4. 生成动态内容部分

从匹配的 CSV 行解析 `required_sections` 列表。对于每个部分名称，生成相应的内容：

#### 常见 CSV 部分映射：

- "endpoint_specs" 或 "endpoint_specification" → API 端点文档
- "auth_model" 或 "authentication_model" → 认证方法
- "platform_reqs" 或 "platform_requirements" → 平台支持需求
- "device_permissions" 或 "device_features" → 设备功能
- "tenant_model" → 多租户方法
- "rbac_matrix" 或 "permission_matrix" → 权限结构

#### 模板变量策略：

- 对于匹配常见模板变量的部分：生成具体内容
- 对于没有模板匹配的部分：包含在主要项目类型要求中
- 混合方法平衡模板结构与 CSV 驱动的灵活性

### 5. 生成项目类型内容

准备要追加到文档的内容：

#### 内容结构：

保存到文档时，追加这些 2 级和 3 级部分：

```markdown
## [项目类型] 特定要求

### 项目类型概述

[基于对话的项目类型摘要]

### 技术架构考虑

[基于对话的技术架构要求]

[基于 CSV 和对话的动态部分]

### 实现考虑

[基于对话的实现特定要求]
```

### 6. 展示菜单选项

展示项目类型内容以供审查，然后显示菜单：

"根据我们的对话和此类产品的最佳实践，我已经记录了 {{project_name}} 的 {project_type}-特定要求。

**这是我将添加到文档中的内容：**

[显示第 5 部分的完整 Markdown 内容]

**你想做什么？**"

显示： "**选择：** [A] 高级诱导 [P] 派对模式 [C] 继续到范围界定 (第 8 步，共 11 步)"

#### 菜单处理逻辑：
- 如果 A: 完整阅读并遵循：{advancedElicitationTask} 使用当前的项目类型内容，处理返回的增强技术见解，询问用户“接受对技术要求的这些改进吗？(y/n)”，如果是用改进更新内容然后重新显示菜单，如果否保持原始内容然后重新显示菜单
- 如果 P: 完整阅读并遵循：{partyModeWorkflow} 使用当前的项目类型要求，处理协作技术专业知识和验证，询问用户“接受对技术要求的这些更改吗？(y/n)”，如果是用改进更新内容然后重新显示菜单，如果否保持原始内容然后重新显示菜单
- 如果 C: 将最终内容追加到 {outputFile}，通过将此步骤名称添加到 stepsCompleted 数组的末尾来更新 frontmatter，然后完整阅读并遵循：{nextStepFile}
- 如果 其他：帮助用户响应，然后重新显示菜单

#### 执行规则：
- 始终 在展示菜单后停止并等待用户输入
- 仅 当用户选择 'C' 时才进行下一步
- 在其他菜单项执行后，返回此菜单

## 追加到文档：

当用户选择 'C' 时，使用之前步骤的结构将内容直接追加到文档。

## 成功指标：

✅ 有效加载和使用项目类型配置
✅ 使用用户输入探索 CSV 中的所有关键问题
✅ 按照 CSV 配置生成所需部分
✅ 正确避免跳过的部分以节省时间
✅ 技术要求连接到产品价值
✅ 正确展示和处理 A/P/C 菜单
✅ 选择 C 时内容正确追加到文档

## 失败模式：

❌ 未加载或使用项目类型 CSV 配置
❌ 发现过程中缺少 CSV 中的关键问题
❌ 未按照 CSV 配置生成所需部分
❌ 记录应根据 CSV 跳过的部分
❌ 创建没有项目类型特性的通用内容
❌ 生成内容后未展示 A/P/C 菜单
❌ 在没有用户选择 'C' 的情况下追加内容

❌ **关键**: 仅阅读部分步骤文件 - 导致不完全理解和糟糕的决定
❌ **关键**: 在未完全阅读和理解下一个步骤文件的情况下继续使用 'C'
❌ **关键**: 在未完全理解步骤要求和协议的情况下做出决定

## 项目类型示例：

**对于 api_backend:**

- 专注于端点、认证、数据模式、速率限制
- 跳过视觉设计和用户旅程部分
- 生成 API 规范文档

**对于 mobile_app:**

- 专注于平台要求、设备权限、离线模式
- 除非需要，否则跳过 API 端点文档
- 生成移动端特定技术要求

**对于 saas_b2b:**

- 专注于多租户、权限、集成
- 除非相关，否则跳过移动优先考虑
- 生成企业特定要求

## 下一步：

当用户选择 'C' 且内容保存到文档后，加载 `{nextStepFile}` 以定义项目范围。

记住：在用户从 A/P/C 菜单中明确选择 'C' 且内容已保存之前，请勿继续进行 step-08 (Scoping)！
