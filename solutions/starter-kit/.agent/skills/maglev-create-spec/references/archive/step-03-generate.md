---
name: 'step-03-generate'
description: '构建符合 Maglev 标准的结构化 Spec 草稿'

workflow_path: '{project-root}/_bmad/bmm/workflows/bmad-quick-flow/create-tech-spec'
nextStepFile: './step-04-review.md'
wipFile: '{implementation_artifacts}/tech-spec-wip.md'
---

# 步骤 3: 生成结构化草稿 (Generate Structural Draft)

**进度：第 3 步，共 4 步** - 下一步：审查与拆分定稿

## 规则:
- ✅ 你必须始终使用配置的 `{communication_language}` (中文)
- **Bookshelf Principle**: 我们不再生成单一的技术规范文件，而是生成一个 **Spec File Cluster**。当前阶段，请将所有内容写入 `{wipFile}` 作为统一草稿。

## 指令序列

### 1. 加载并分析
读取 `{wipFile}` 中的问题陈述与调查结果。

### 2. 生成 Draft Content (按章节)

请使用以下思维模型填充模板的四个核心部分：

#### A. Requirements Layer (`01_requirements`)
*   **Intent**: 用一句话概括核心价值。
*   **Stories**: 定义 User Stories。
*   **Acceptance Criteria**: **关键！** 必须使用 Given/When/Then 格式。这是后续生成 Test Case 的真理源头。

#### B. Design Layer (`02_design`) [Polymorphic]
根据项目类型选择生成策略：
*   **Web/App**: 侧重 **Sitemap**, **Component Tree**, **Interaction Table** (Component -> Event -> Action)。
*   **Backend**: 侧重 **API Schema**, **Data Model (ERD)**, **Sequence Diagram**。
*   **Agent**: 侧重 **System Prompt**, **Workflow State Machine**。

#### C. Plan Layer (`03_plan`)
*   **Tasks**: 具体的实施步骤，包含要修改的文件列表。
*   **Verification**: 如何验证每一个 Task (e.g., Unit Test, UI Check)。

### 3. 执行写入
使用从 Step 1 收集的信息和 Step 2 生成的内容，**完全填充** `{wipFile}`。
确保没有 `{placeholder}` 遗留。

### 4. 完成更新
更新 frontmatter：
```yaml
---
# ... existing ...
status: 'review'
stepsCompleted: [1, 2, 3]
---
```

## 必需输出:
*   `{wipFile}` 必须包含 00, 01, 02, 03 四个完整章节。
*   AC (验收标准) 必须是结构化的。
*   Design 章节必须包含 Mermaid 图表。
