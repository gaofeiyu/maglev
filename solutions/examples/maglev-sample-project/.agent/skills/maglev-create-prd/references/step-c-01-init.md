---
name: 'step-01-init'
description: '通过检测继续状态并设置文档来初始化 PRD 工作流'

# File References
nextStepFile: './step-c-02-discovery.md'
continueStepFile: './step-c-01b-continue.md'
# Output will be defined dynamically based on user slug
outputFile: ''

# Template Reference
prdTemplate: '{project-root}/solutions/templates/standards/template_01_requirements.md'
---

# 步骤 1: 工作流初始化 (v2.0 Standard)

**进度：第 1 步，共 5 核心步骤** - 下一步：项目发现

## 步骤目标：
初始化 PRD 工作流，获取 Slug，并创建标准的 Spec 目录结构。

## 强制执行规则 (请先阅读):

### 通用规则：
- 🛑 绝不 在没有用户输入的情况下生成内容
- 📖 关键：在采取任何行动之前，请阅读完整的步骤文件

### 角色强化：
- ✅ 你是一个专注于产品的 Maglev 架构师

## 指令序列 (不要偏离、跳过或优化)

### 1. 获取项目 Slug

首先，向用户询问此 PRD 的唯一标识符 (Slug)。
这对应目录名: `specs/20_evolution/active/{slug}/`。

**交互提示:**
"欢迎！为了开始新的 PRD，请提供一个简短的 **Slug** (项目/功能标识符)，例如 `feat-user-login` 或 `refactor-payment-api`。"

**等待用户输入 Slug**。

### 2. 初始化路径与文件

一旦获得 `{slug}`：
1.  **定义输出路径**: `{output_folder}/{slug}/01_requirements.md` (注意: `output_folder` 来自 workflow config).
2.  **创建目录**: 确保 `{output_folder}/{slug}` 存在。
3.  **检查文件**: 如果文件已存在，询问是否 `[E] 编辑` 或 `[O] 覆盖`。

### 3. 创建初始文档 (若是新文件)

**文档设置：**
- 将模板从 `{prdTemplate}` 复制到 `{outputFile}`。
- 更新 Frontmatter: 此步骤已完成。

### 4. 展示菜单选项

在设置报告后显示菜单：

"[C] 继续 - 保存并移动到项目发现 (第 2 步)"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}` (`step-c-02-discovery.md`)。


#### 菜单处理逻辑：

- 如果 C: 更新输出文件 frontmatter，将此步骤名称添加到 stepsCompleted 列表的末尾，然后完整阅读并遵循：{nextStepFile}
- 如果用户提供其他文件：加载它们，更新 inputDocuments 和 documentCounts，重新显示报告
- 如果用户提问：回答并重新显示菜单

#### 执行规则：

- 始终 在展示菜单后停止并等待用户输入
- 仅 当用户选择 'C' 时才进行下一步

## 关键步骤完成说明

仅当选择 [C 继续选项] 并且 [frontmatter 已正确更新，此步骤已添加到 stepsCompleted 和 documentCounts] 时，你才会完整阅读并遵循：`{nextStepFile}` 以开始项目发现。

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 检测到现有工作流并正确移交给 step-01b
- 使用模板和正确的 frontmatter 初始化新工作流
- 使用分片优先逻辑发现并加载输入文档
- frontmatter `inputDocuments` 中跟踪的所有已发现文件
- 清楚地告知用户棕地与绿地状态
- 正确展示菜单并处理用户输入
- 在继续之前，frontmatter 已更新，此步骤名称已添加到 stepsCompleted

### ❌ 系统失败：

- 当存在现有工作流时继续进行新初始化
- 未用发现的输入文档更新 frontmatter
- **未在 frontmatter 中存储文档计数**
- 创建没有正确模板结构的文档
- 未在整个文件之前先检查分片文件夹
- 未清楚地向用户报告发现的文档
- 在没有用户选择 'C' (继续) 的情况下继续

**主规则：** 禁止跳过步骤、优化顺序或不遵循确切说明，这构成系统故障。
