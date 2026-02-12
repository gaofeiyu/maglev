---
name: 'step-10-nonfunctional'
description: 'Generate Non-Functional Requirements (Standard v2.0)'

# File References
# Skip legacy polish, jump to Quality Gate
nextStepFile: './step-c-11-quality-gate.md'
outputFile: '{outputFile}'

# Task References
advancedElicitationTask: 'references/advanced-elicitation.workflow.xml'

---

# 步骤 5: 非功能需求定义 (Standard v2.0)

**进度：第 5 步，共 5 核心步骤** - 下一步：完成

## 步骤目标：
定义性能、安全、可靠性等 NFR，填充 `01_requirements.md` 的 `## 3. 非功能需求 (Non-Functional Requirements)` 章节。

## 强制执行规则:
- 🛑 绝不 在没有用户输入的情况下生成内容
- ✅ 仅包含相关的 NFR (No Bloat)

## 指令序列

### 1. 发现 NFR

询问关键维度:
- Performance (e.g. Latency)
- Security (e.g. Auth)
- Scalability
- Reliability

### 2. 生成内容

**目标格式:**
```markdown
### 性能 (Performance)
- [ ] **NFR 1.1**: API latency < 200ms
```

### 3. 编辑文档

**Action**:
将内容插入到 `{outputFile}` 的 `## 3. 非功能需求` 章节。

### 4. 展示菜单

"[C] 继续 - 完成工作流"

#### 菜单处理逻辑：
- 如果 C: 完整阅读并遵循 `{nextStepFile}` (`step-c-12-complete.md`)。

