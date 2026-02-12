---
name: 'step-v-09-project-type-validation'
description: '项目类型合规性验证 - 验证特定于项目类型的需求是否已正确记录'

# File references (ONLY variables used in this step)
nextStepFile: './step-v-10-smart-validation.md'
prdFile: '{prd_file_path}'
prdFrontmatter: '{prd_frontmatter}'
validationReportPath: '{validation_report_path}'
projectTypesData: '../data/project-types.csv'
---

# 步骤 9: 项目类型合规性验证

## 步骤目标：

验证特定于项目类型的需求是否已正确记录 - 不同的项目类型（api_backend, web_app, mobile_app 等）具有不同的所需和排除部分。

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
- ✅ 我们参与系统验证，而不是协作对话
- ✅ 你带来项目类型专业知识和架构知识
- ✅ 此步骤自动运行 - 不需要用户输入

### 步骤特定规则：

- 🎯 仅关注 项目类型合规性
- 🚫 禁止 在此步骤中验证其他方面
- 💬 方法：验证所需部分是否存在，排除部分是否缺失
- 🚪 这是一个验证序列步骤 - 完成后自动继续

## 执行协议：

- 🎯 检查 PRD frontmatter 中的 classification.projectType
- 🎯 验证该项目类型的所需部分是否存在
- 🎯 验证该项目类型的排除部分是否缺失
- 💾 将合规性发现追加到验证报告
- 📖 显示 "正在进行下一步检查..." 并加载下一步
- 🚫 禁止 暂停或请求用户输入

## 上下文边界：

- 可用上下文：带有 frontmatter 分类的 PRD 文件，验证报告
- 重点：仅项目类型合规性
- 限制：不验证其他方面，不暂停等待用户输入
- 依赖项：步骤 2-8 已完成 - 领域和需求验证已完成

## 强制序列

**关键：** 严格遵循此序列。除非用户明确要求更改，否则不要跳过、重新排序或即兴发挥。

### 1. 加载项目类型数据

加载并阅读完整文件：
`{projectTypesData}` (../data/project-types.csv)

此 CSV 包含：
- 每个项目类型的检测信号
- 每个项目类型的所需部分
- 每个项目类型的跳过/排除部分
- 创新信号

内化此数据 - 它驱动每个项目类型必须存在或缺失的部分。

### 2. 提取项目类型分类

从 PRD frontmatter 提取：
- `classification.projectType` - 这是什么类型的项目？

**常见项目类型:**
- api_backend
- web_app
- mobile_app
- desktop_app
- data_pipeline
- ml_system
- library_sdk
- infrastructure
- other

**如果未找到 projectType 分类:**
假设 "web_app"（最常见）并在发现中注意

### 3. 从 CSV 数据确定所需和排除的部分

**从已加载的 project-types.csv 数据，对于此项目类型：**

**所需部分:** (from required_sections column)
这些必须存在于 PRD 中

**跳过部分:** (from skip_sections column)
这些必须不存在于 PRD 中

**CSV 中的示例映射:**
- api_backend: Required=[endpoint_specs, auth_model, data_schemas], Skip=[ux_ui, visual_design]
- mobile_app: Required=[platform_reqs, device_permissions, offline_mode], Skip=[desktop_features, cli_commands]
- cli_tool: Required=[command_structure, output_formats, config_schema], Skip=[visual_design, ux_principles, touch_interactions]
- 等等。

### 4. 验证 CSV 基础需求

**根据项目类型，确定：**

**api_backend:**
- Required: Endpoint Specs, Auth Model, Data Schemas, API Versioning
- Excluded: UX/UI sections, mobile-specific sections

**web_app:**
- Required: User Journeys, UX/UI Requirements, Responsive Design
- Excluded: None typically

**mobile_app:**
- Required: Mobile UX, Platform specifics (iOS/Android), Offline mode
- Excluded: Desktop-specific sections

**desktop_app:**
- Required: Desktop UX, Platform specifics (Windows/Mac/Linux)
- Excluded: Mobile-specific sections

**data_pipeline:**
- Required: Data Sources, Data Transformation, Data Sinks, Error Handling
- Excluded: UX/UI sections

**ml_system:**
- Required: Model Requirements, Training Data, Inference Requirements, Model Performance
- Excluded: UX/UI sections (unless ML UI)

**library_sdk:**
- Required: API Surface, Usage Examples, Integration Guide
- Excluded: UX/UI sections, deployment sections

**infrastructure:**
- Required: Infrastructure Components, Deployment, Monitoring, Scaling
- Excluded: Feature requirements (this is infrastructure, not product)

### 4. 尝试子流程验证

"执行 {projectType} 的项目类型合规性验证：

**检查所需部分是否存在:**
{List required sections for this project type}
对于每个：PRD 中是否存在？记录是否充分？

**检查排除部分是否缺失:**
{List excluded sections for this project type}
对于每个：PRD 中是否缺失？（应该不存在）

构建合规性表，显示：
- 所需部分：[存在/缺失/不完整]
- 排除部分：[缺失/存在] (存在 = 违规)

返回带有发现的合规性表。"

**优雅降级（如果无 Task 工具）：**
- 手动检查 PRD 中的所需部分
- 手动检查 PRD 中的排除部分
- 构建合规性表

### 5. 构建合规性表

**所需部分检查:**
- 对于每个所需部分：存在 / 缺失 / 不完整
- 计数：存在的所需部分 vs 总共所需

**排除部分检查:**
- 对于每个排除部分：缺失 / 存在 (违规)
- 计数：存在的排除部分 (违规)

**总合规性分数:**
- 所需: {present}/{total}
- 排除违规: {count}

### 6. 向验证报告报告项目类型合规性发现

追加到验证报告：

```markdown
## 项目类型合规性验证

**项目类型:** {projectType}

### 所需部分

**{Section 1}:** [存在/缺失/不完整]
{如果缺失或不完整: 注意具体差距}

**{Section 2}:** [存在/缺失/不完整]
{如果缺失或不完整: 注意具体差距}

[继续所有所需部分]

### 排除部分 (不应存在)

**{Section 1}:** [缺失/存在] ✓
{如果存在: 此部分不应存在于 {projectType}}

**{Section 2}:** [缺失/存在] ✓
{如果存在: 此部分不应存在于 {projectType}}

[继续所有排除部分]

### 合规性摘要

**所需部分:** {present}/{total} 存在
**存在的排除部分:** {violations} (应为 0)
**合规性分数:** {percentage}%

**严重性:** [严重 如果所需部分缺失, 警告 如果不完整, 通过 如果完整]

**推荐:**
[如果严重] "PRD 缺少 {projectType} 的所需部分。添加缺失部分以正确指定此类项目。"
[如果警告] "一些 {projectType} 的所需部分不完整。加强文档。"
[如果通过] "所有 {projectType} 的所需部分均存在。未发现排除部分。"
```

### 7. 显示进度并自动继续

显示："**项目类型合规性验证完成**

项目类型：{projectType}
合规性：{score}%

**正在进行下一步验证检查...**"

毫不延迟，完整阅读并遵循：{nextStepFile} (step-v-10-smart-validation.md)

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 正确提取项目类型（或假设默认值）
- 验证所需部分的存在和完整性
- 验证排除部分的缺失
- 构建合规性表
- 正确评估严重性
- 将发现报告给验证报告
- 自动继续进行下一个验证步骤
- 尝试子流程架构并进行优雅降级

### ❌ 系统失败：

- 未在继续之前检查项目类型
- 缺少所需部分检查
- 缺少排除部分检查
- 未构建合规性表
- 未将发现报告给验证报告
- 未自动继续

**主规则：** 不同的项目类型有不同的要求。API PRD 不需要 UX 部分 - 相应地验证。
