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
partyModeWorkflow: 'references/party-mode.workflow.md'
---

# 步骤 3: 用户故事定义 (Standard v2.0)

**进度：第 3 步，共 5 核心步骤** - 下一步：功能需求

## 步骤目标：
将用户旅程转化为标准的 **User Stories** 和 **Acceptance Criteria (AC)**，并填充到 `01_requirements.md` 的 `## 1. 用户故事 (User Stories)` 章节。

## 强制执行规则:
- 🛑 绝不 在没有用户输入的情况下生成内容
- ✅ 格式必须遵循: `AS A <Role>, I WANT <Action>, SO THAT <Benefit>`
- ✅ 每个 Story 必须包含可测试的 AC (Acceptance Criteria)

## 指令序列

### 1. 发现用户故事

基于产品简报和上下文，与用户协作识别关键 User Stories。

**引导策略:**
1.  **识别角色**: 谁是主要用户？(e.g., Admin, Buyer)
2.  **定义动作**: 他们想做什么？(e.g., View Dashboard)
3.  **明确价值**: 为什么要做这个？(e.g., To track sales)
4.  **定义 AC**: 怎么算做完了？(e.g., "Must show daily total")

### 2. 生成内容 (Standard Format)

当用户确认故事列表后，生成符合 Maglev 标准的 Markdown 内容。

**目标格式:**
```markdown
### [Story-X] {Title}
*   **As a**: {Role}
*   **I want**: {Action}
*   **So that**: {Benefit}

#### 验收标准 (Acceptance Criteria)
- [ ] **AC 1.1**: {Condition} -> {Result}
- [ ] **AC 1.2**: ...
```

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

