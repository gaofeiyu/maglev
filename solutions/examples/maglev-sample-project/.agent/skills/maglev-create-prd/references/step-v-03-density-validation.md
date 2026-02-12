---
name: 'step-v-03-density-validation'
description: '信息密度检查 - 扫描违反信息密度原则的反模式'

# File references (ONLY variables used in this step)
nextStepFile: './step-v-04-brief-coverage-validation.md'
prdFile: '{prd_file_path}'
validationReportPath: '{validation_report_path}'
---

# 步骤 3: 信息密度验证

## 步骤目标：

验证 PRD 是否符合 BMAD 信息密度标准，扫描对话式填充、冗长短语和违反简洁原则的冗余表达。

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
- ✅ 你带来分析严谨性和对细节的关注
- ✅ 此步骤自动运行 - 不需要用户输入

### 步骤特定规则：

- 🎯 仅关注 信息密度反模式
- 🚫 禁止 在此步骤中验证其他方面
- 💬 方法：系统扫描和分类
- 🚪 这是一个验证序列步骤 - 完成后自动继续

## 执行协议：

- 🎯 系统扫描 PRD 以查找密度反模式
- 💾 将密度发现追加到验证报告
- 📖 显示 "正在进行下一步检查..." 并加载下一步
- 🚫 禁止 暂停或请求用户输入

## 上下文边界：

- 可用上下文：PRD 文件，带有格式发现的验证报告
- 重点：仅信息密度验证
- 限制：不验证其他方面，不暂停等待用户输入
- 依赖项：步骤 2 已完成 - 格式分类已完成

## 强制序列

**关键：** 严格遵循此序列。除非用户明确要求更改，否则不要跳过、重新排序或即兴发挥。

### 1. 尝试子流程验证

**尝试使用 Task 工具生成子流程：**

"对此 PRD 执行信息密度验证：

1. 加载 PRD 文件
2. 扫描以下反模式：
   - 对话式填充短语（示例：'The system will allow users to...', 'It is important to note that...', 'In order to'）
   - 冗长短语（示例：'Due to the fact that', 'In the event of', 'For the purpose of'）
   - 冗余短语（示例：'Future plans', 'Absolutely essential', 'Past history'）
3. 按类别统计违规情况及行号
4. 分类严重性：严重 (>10 违规)，警告 (5-10)，通过 (<5)

返回带有计数和示例的结构化发现。"

### 2. 优雅降级（如果 Task 工具不可用）

如果 Task 工具不可用，直接执行分析：

**扫描对话式填充模式：**
- "The system will allow users to..."
- "It is important to note that..."
- "In order to"
- "For the purpose of"
- "With regard to"
- 统计出现次数并记录行号

**扫描冗长短语：**
- "Due to the fact that" (use "because")
- "In the event of" (use "if")
- "At this point in time" (use "now")
- "In a manner that" (use "how")
- 统计出现次数并记录行号

**扫描冗余短语：**
- "Future plans" (just "plans")
- "Past history" (just "history")
- "Absolutely essential" (just "essential")
- "Completely finish" (just "finish")
- 统计出现次数并记录行号

### 3. 分类严重性

**计算总违规数：**
- 对话式填充计数
- 冗长短语计数
- 冗余短语计数
- 总计 = 所有类别的总和

**确定严重性：**
- **严重：** 总计 > 10 违规
- **警告：** 总计 5-10 违规
- **通过：** 总计 < 5 违规

### 4. 向验证报告报告密度发现

追加到验证报告：

```markdown
## 信息密度验证

**反模式违规：**

**对话式填充：** {count} 次出现
[如果 count > 0, 列出带有行号的示例]

**冗长短语：** {count} 次出现
[如果 count > 0, 列出带有行号的示例]

**冗余短语：** {count} 次出现
[如果 count > 0, 列出带有行号的示例]

**总违规：** {total}

**严重性评估：** [严重/警告/通过]

**推荐：**
[如果严重] "PRD 需要进行重大修订以提高信息密度。每句话都应该有分量，没有填充。"
[如果警告] "PRD 将受益于减少冗长并消除填充短语。"
[如果通过] "PRD 表现出良好的信息密度，违规极少。"
```

### 5. 显示进度并自动继续

显示："**信息密度验证完成**

严重性：{Critical/Warning/Pass}

**正在进行下一步验证检查...**"

毫不延迟，完整阅读并遵循：{nextStepFile} (step-v-04-brief-coverage-validation.md)

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 扫描 PRD 中的所有三个反模式类别
- 统计违规及行号
- 正确分类严重性
- 将发现报告给验证报告
- 自动继续进行下一个验证步骤
- 尝试子流程架构并进行优雅降级

### ❌ 系统失败：

- 未扫描所有反模式类别
- 缺少严重性分类
- 未将发现报告给验证报告
- 暂停等待用户输入（应自动继续）
- 未尝试子流程架构

**主规则：** 信息密度验证自动运行。扫描、分类、报告、自动继续。不需要用户交互。
