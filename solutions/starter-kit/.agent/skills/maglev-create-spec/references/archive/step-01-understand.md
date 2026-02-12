---
name: 'step-01-understand'
description: '分析当前状态与用户想要构建之间的需求差异'

workflow_path: '{project-root}/_bmad/bmm/workflows/bmad-quick-flow/create-tech-spec'
nextStepFile: './step-02-investigate.md'
skipToStepFile: './step-03-generate.md'
templateFile: '{workflow_path}/tech-spec-template.md'
wipFile: '{implementation_artifacts}/tech-spec-wip.md'
---

# 步骤 1: 分析需求差异

**进度：第 1 步，共 4 步** - 下一步：深度调查

## 规则:

- 必须不 跳过步骤。
- 必须不 优化顺序。
- 必须 遵循确切说明。
- 必须不 查看未来的步骤。
- ✅ 你必须始终使用配置的 `{communication_language}` 以你的 Agent 沟通风格输出语言

## 上下文:

- 来自 `workflow.md` 的变量在内存中可用。
- 重点：定义技术需求差异和范围。
- 调查：仅执行 表面级代码扫描 以验证差异。将对实施后果的深入研究保留给步骤 2。
- 目标：在当前状态和目标状态之间建立可验证的差异。

## 指令序列

### 0. 检查正在进行的工作

a) **在做任何其他事情之前，检查 `{wipFile}` 是否存在：**

b) **如果 WIP 文件存在：**

1. 读取 frontmatter 并提取：`title`, `slug`, `stepsCompleted`
2. 计算进度：`lastStep = max(stepsCompleted)`
3. 向用户展示：

```
嘿 {user_name}! 发现一个正在进行的技术规范：

**{title}** - 第 {lastStep} 步，共 4 步完成

这是你要继续的吗？

[Y] 是，从我离开的地方继续
[N] 否，归档它并开始新的
```

4. **停止并等待用户选择。**

a) **菜单处理：**

- **[Y] 继续现有的：**
  - 根据 `stepsCompleted` 直接跳转到适当的步骤：
    - `[1]` → 加载 `{nextStepFile}` (步骤 2)
    - `[1, 2]` → 加载 `{skipToStepFile}` (步骤 3)
    - `[1, 2, 3]` → 加载 `./step-04-review.md` (步骤 4)
- **[N] 归档并重新开始：**
  - 将 `{wipFile}` 重命名为 `{implementation_artifacts}/tech-spec-{slug}-archived-{date}.md`

### 1. 问候与输入摄入 (Greeting & Ingest)

a) **向用户问好并识别输入模式：**
   "嘿 {user_name}! 我们今天构建什么？请告诉我你的输入类型：
   1. **Idea**: 一句话意图 (e.g., '添加 VIP 字段')
   2. **Docs**: 已有 PRD 或会议记录 (请提供路径)
   3. **Legacy**: 存量项目改造 (请指出关键代码目录)"

b) **摄入逻辑 (Ingestion Logic)**:
   *   **Type 1 (Idea)**: 记录 Intent，作为后续 Q&A 的种子。
   *   **Type 2 (Docs)**: 
       *   **Action**: 立即使用 `read_file` 读取用户提供的文档。
       *   **Extract**: 从文档中提取 Goal, Context, Constraints。
   *   **Type 3 (Legacy)**:
       *   **Action**: 立即使用 `list_dir` 和 `view_file_outline` 扫描指定代码目录。
       *   **Extract**: 提取现有的 Data Schema 和 API Signature 作为“现状”。

c) **确认理解**:
   无论哪种输入，最后都要汇总确认：
   "已摄入: [Doc Name / Code Path]
   识别意图: {...}"

### 2. 快速定向扫描 (Context Scan)

### 2. 快速定向扫描

a) **在提出详细问题之前，进行快速扫描以了解情况：**

b) **检查现有的上下文文档：**

- 检查 `{output_folder}` 和 `{planning_artifacts}` 是否有规划文档（PRD、架构、epics、研究）
- 检查 `**/project-context.md` - 如果存在，浏览模式和惯例
- 检查是否存在与用户请求相关的任何现有故事或规范

c) **如果用户提到特定的代码/功能，进行快速扫描：**

- 搜索他们提到的相关文件/类/函数
- 浏览结构（不要深入研究 - 那是步骤 2）
- 注意：技术栈、明显的模式、文件位置

d) **建立心理模型：**

- 此功能的可能环境是什么？
- 根据你的发现，可能的范围是什么？
- 根据代码，你现在有什么问题？

**此扫描应少于 30 秒。足够提出聪明的问题即可。**

### 3. 提出知情问题

a) **现在提出澄清问题 - 但要根据你的发现使它们 知情：**

而不是像 "范围是什么？" 这样的通用问题，提出具体问题，如：
- "`AuthService` 在控制器中处理验证 — 新字段应该遵循该模式还是将其移动到专用的验证器？"
- "`NavigationSidebar` 组件使用本地状态进行 '折叠' 切换 — 我们应该坚持这一点还是将其移动到全局存储？"
- "epics 文档提到 X - 这与之相关吗？"

**适应 {user_skill_level}。** 技术用户想要技术问题。非技术用户需要翻译。

b) **如果没有发现现有代码：**

- 询问预期的架构、模式、约束
- 询问他们想模仿哪些类似系统

### 4. 捕获核心理解

a) **从对话中，提取并确认：**

- **标题 (Title)**: 此工作的清晰、简洁的名称
- **Slug**: 标题的 URL 安全版本（小写、连字符、无空格）
- **问题陈述 (Problem Statement)**: 我们正在解决什么问题？
- **解决方案 (Solution)**: 高级方法（1-2 句话）
- **范围内 (In Scope)**: 包括什么
- **范围外 (Out of Scope)**: 明确 不包括什么

b) **在继续之前要求用户确认捕获的理解。**

### 5. 初始化 WIP 文件

a) **创建 tech-spec WIP 文件：**

1. 从 `{templateFile}` 复制模板
2. 写入 `{wipFile}`
3. 使用捕获的值更新 frontmatter：
   ```yaml
   ---
   title: '{title}'
   slug: '{slug}'
   created: '{date}'
   status: 'in-progress'
   stepsCompleted: [1]
   tech_stack: []
   files_to_modify: []
   code_patterns: []
   test_patterns: []
   ---
   ```
4. 用问题陈述、解决方案和范围填写概述部分
5. 用在知情发现期间收集的任何技术偏好或约束填写开发上下文部分。
6. 写入文件

b) **向用户报告：**

"已创建：`{wipFile}`

**已捕获：**

- 标题: {title}
- 问题: {problem_statement_summary}
- 范围: {scope_summary}"

### 6. 展示检查点菜单

a) **显示菜单：**

显示： "**选择：** [A] 高级诱导 [P] 派对模式 [C] 继续深度调查 (第 2 步，共 4 步)"

b) **停止并等待用户选择。**

#### 菜单处理逻辑：

- 如果 A: 完整阅读并遵循：`{advanced_elicitation}` 使用当前 tech-spec 内容，处理增强见解，询问用户 "接受改进？(y/n)"，如果是更新 WIP 文件然后重新显示菜单，如果否保持原始然后重新显示菜单
- 如果 P: 完整阅读并遵循：`{party_mode_exec}` 使用当前 tech-spec 内容，处理协作见解，询问用户 "接受更改？(y/n)"，如果是更新 WIP 文件然后重新显示菜单，如果否保持原始然后重新显示菜单
- 如果 C: 验证 `{wipFile}` 具有 `stepsCompleted: [1]`，然完整阅读并遵循：`{nextStepFile}`
- 如果 其他评论或查询：有帮助地回应然后重新显示菜单

#### 执行规则：

- 始终 在展示菜单后停止并等待用户输入
- 仅 当用户选择 'C' 时才进行下一步
- 在 A 或 P 执行后，返回此菜单

---

## 必需输出：

- 必须 使用捕获的元数据初始化 WIP 文件。

## 验证清单：

- [ ] 在任何问候之前 首先 执行 WIP 检查。
- [ ] 创建 `{wipFile}`，具有正确的 frontmatter、概述、开发上下文和 `stepsCompleted: [1]`。
- [ ] 用户选择 [C] 继续。
