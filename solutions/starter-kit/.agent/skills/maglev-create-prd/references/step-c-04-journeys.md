---
name: 'step-04-journeys'
description: 'Generate User Stories and Acceptance Criteria (Standard v2.0)'

# File References
# Skipping legacy Domain/Innovation steps, jumping to Functional
nextStepFile: './step-c-09-functional.md'
# Dynamics output file from Step 01
outputFile: '{outputFile}'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'

---

# 步骤 3: 用户故事定义 (Standard v2.0)

**进度：第 3 步，共 5 核心步骤** - 下一步：功能需求

## 步骤目标：
将用户旅程转化为标准的 **User Stories** 和 **Acceptance Criteria (AC)**，并填充到 `01_requirements.md` 的 `## 1. 用户故事 (User Stories)` 章节。

## 强制执行规则:
- 🛑 绝不 在没有用户输入的情况下生成内容
- ✅ 格式必须遵循: `AS A <Role>, I WANT <Action>, SO THAT <Benefit>`
- ✅ 每个 Story 必须包含可测试的## 1. 核心指令 (Core Instruction)
你将使用 **OpenSpec 标准** (BDD Style) 来定义需求。在此阶段，严禁使用模糊的自然语言，必须转化为可执行的逻辑。**所有输出必须使用中文。**

**格式定义 (Format Definition)**:
*   **Requirement**: "系统必须(SHALL)..." (约束性声明)
*   **Scenario**: 具体的业务场景。
*   **Gherkin**: `GIVEN` (前置条件) -> `WHEN` (当) -> `THEN` (那么) -> `AND` (并且)。

## 2. 引导策略 (Conditional by Type)

*   **Type: App/Web (Has UI)**
    *   **关注点**: 交互逻辑与页面状态。
    *   **Spec 示例**:
        ```markdown
        #### Scenario: 用户登录成功
        - **GIVEN** 用户处于登录页面
        - **WHEN** 用户输入有效的凭证并提交
        - **THEN** 系统跳转至仪表盘首页
        ```

*   **Type: API/Service (Headless)**
    *   **关注点**: 数据流与接口契约。
    *   **Spec 示例**:
        ```markdown
        #### Scenario: 无效 Token 处理
        - **GIVEN** 请求头包含过期的 Token
        - **WHEN** API 收到请求
        - **THEN** 返回 401 Unauthorized 状态码
        ```

## 3. 模板加载
读取本地模板: `references/templates/zone-template-prd-openspec.md`。
请务必保留模板顶部的 Executive Brief 和底部的 Context Trace。

### 3. 编辑文档

**Action**:
使用工具 (e.g., `replace_file_content`) 将生成的 Story 内容插入到 `{outputFile}` 的 `## 1. 用户故事 (User Stories)` 章节下方。
*   Target: `## 1. 用户故事 (User Stories)` 下方的占位符或追加内容。

### 4. 展示菜单选项

展示生成的故事列表，然后显示菜单：

"[C] 继续 - 保存并移动到功能性需求 (第 4 步)"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}` (`step-c-09-functional.md`)。
- 如果 A/P: (可选) 允许高级诱导。

