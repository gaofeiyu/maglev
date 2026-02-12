---
name: 'step-09-functional'
description: 'Generate Functional Requirements (Standard v2.0)'

# File References
nextStepFile: './step-c-10-nonfunctional.md'
outputFile: '{outputFile}'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'

---

# 步骤 4: 功能需求定义 (Standard v2.0)

**进度：第 4 步，共 5 核心步骤** - 下一步：非功能需求

## 步骤目标：
定义产品必须具备的能力，填充 `01_requirements.md` 的 `## 2. 功能需求 (Functional Requirements)` 章节。

## 强制执行规则:
- 🛑 绝不 在没有用户输入的情况下生成内容
- ✅ 需求必须是无实现细节的 (Implementation Agnostic)
- ✅ 必须覆盖所有关键 User Stories

## 指令序列

### 1. 综合功能需求

回顾之前的 User Stories，提取并补充系统必须具备的功能点。
按模块或领域分组 (e.g., User Management, Payment Processing)。

### 2. 生成内容 (Standard Format)

**目标格式:**
```markdown
### [Feature-X] {Title}
*   **Description**: {What it does}
*   **Priority**: P0/P1/P2
*   **Dependencies**: {Optional}

#### 细项 (Requirements)
- [ ] **FR 1.1**: {Specific Requirement}
- [ ] **FR 1.2**: ...
```

### 3. 编辑文档

**Action**:
使用工具将生成的内容插入到 `{outputFile}` 的 `## 2. 功能需求 (Functional Requirements)` 章节下方。

### 4. 展示菜单选项

展示功能列表，然后显示菜单：

"[C] 继续 - 保存并移动到非功能需求 (第 5 步)"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}`。
- 如果 A/P: (可选) 高级诱导。

