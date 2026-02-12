---
name: 'step-v-13-report-complete'
description: '验证报告完成 - 完成报告，总结发现，向用户展示，提供后续步骤'

# File references (ONLY variables used in this step)
validationReportPath: '{validation_report_path}'
prdFile: '{prd_file_path}'
---

# 步骤 13: 验证报告完成

## 步骤目标：

完成验证报告，总结步骤 1-12 的所有发现，以对话方式向用户展示总结，并提供可操作的后续步骤。

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
- ✅ 我们参与协作对话，而不是命令-响应
- ✅ 你带来综合和总结专业知识
- ✅ 这是最后一步 - 需要用户交互

### 步骤特定规则：

- 🎯 仅关注 总结发现和展示选项
- 🚫 禁止 执行额外验证
- 💬 方法：带有明确后续步骤的对话式总结
- 🚪 这是最后一步 - 此后没有下一步

## 执行协议：

- 🎯 加载完整的验证报告
- 🎯 总结步骤 1-12 的所有发现
- 🎯 使用最终状态更新报告 frontmatter
- 💬 以对话方式向用户展示总结
- 💬 提供下一步操作的菜单选项
- 🚫 禁止 在没有用户选择的情况下继续

## 上下文边界：

- 可用上下文：包含所有验证步骤发现的完整验证报告
- 重点：仅总结和展示（无需新验证）
- 限制：不添加新发现，仅综合现有的
- 依赖项：步骤 1-12 已完成 - 所有验证检查已完成

## 强制序列

**关键：** 严格遵循此序列。除非用户明确要求更改，否则不要跳过、重新排序或即兴发挥。

### 1. 加载完整验证报告

从 {validationReportPath} 读取整个验证报告

提取所有发现：
- 格式检测 (步骤 2)
- 平价分析 (步骤 2B, 假如适用)
- 信息密度 (步骤 3)
- 产品简介覆盖 (步骤 4)
- 可测量性 (步骤 5)
- 可追溯性 (步骤 6)
- 实施泄漏 (步骤 7)
- 领域合规性 (步骤 8)
- 项目类型合规性 (步骤 9)
- SMART 需求 (步骤 10)
- 整体质量 (步骤 11)
- 完整性 (步骤 12)

### 2. 使用最终状态更新报告 Frontmatter

更新验证报告 frontmatter:

```yaml
---
validationTarget: '{prd_path}'
validationDate: '{current_date}'
inputDocuments: [list of documents]
validationStepsCompleted: ['step-v-01-discovery', 'step-v-02-format-detection', 'step-v-03-density-validation', 'step-v-04-brief-coverage-validation', 'step-v-05-measurability-validation', 'step-v-06-traceability-validation', 'step-v-07-implementation-leakage-validation', 'step-v-08-domain-compliance-validation', 'step-v-09-project-type-validation', 'step-v-10-smart-validation', 'step-v-11-holistic-quality-validation', 'step-v-12-completeness-validation']
validationStatus: COMPLETE
holisticQualityRating: '{rating from step 11}'
overallStatus: '{Pass/Warning/Critical based on all findings}'
---
```

### 3. 创建发现摘要

**总体状态:**
- 从所有验证发现中确定
- **通过:** 所有关键检查通过，次要警告可接受
- **警告:** 发现一些问题，但 PRD 可用
- **严重:** 存在阻碍 PRD 适用的重大问题

**快速结果表:**
- 格式: [classification]
- 信息密度: [severity]
- 可测量性: [severity]
- 可追溯性: [severity]
- 实施泄漏: [severity]
- 领域合规性: [status]
- 项目类型合规性: [compliance score]
- SMART 质量: [percentage]
- 整体质量: [rating/5]
- 完整性: [percentage]

**关键问题:** 列出所有验证步骤中的关键问题
**警告:** 列出所有验证步骤中的警告
**优势:** 列出所有验证步骤中的积极方面

**整体质量评级:** 来自步骤 11
**前 3 个改进:** 来自步骤 11

**推荐:** 基于总体状态

### 4. 以对话方式向用户展示总结

显示:

"**✓ PRD 验证完成**

**总体状态:** {Pass/Warning/Critical}

**快速结果:**
{Present quick results table with key findings}

**关键问题:** {count or "无"}
{If any, list briefly}

**警告:** {count or "无"}
{If any, list briefly}

**优势:**
{List key strengths}

**整体质量:** {rating}/5 - {label}

**前 3 个改进:**
1. {Improvement 1}
2. {Improvement 2}
3. {Improvement 3}

**推荐:**
{Based on overall status:
- Pass: "PRD 状况良好。解决次要改进以使其变得更好。"
- Warning: "PRD 可用但存在应解决的问题。审查警告并在需要时进行改进。"
- Critical: "PRD 存在在使用前应修复的重大问题。关注上面的关键问题。"}

**你接下来想做什么？**"

### 5. 展示菜单选项

显示:

**[R] 审查详细发现** - 逐节浏览验证报告
**[E] 使用编辑工作流** - 使用验证报告和编辑工作流进行系统改进
**[F] 修复简单项目** - 立即修复简单问题（反模式、泄漏、缺失标题）
**[X] 退出** - 退出并建议后续步骤。

#### 执行规则：

- 始终 在展示菜单后停止并等待用户输入
- 仅 根据用户选择继续

#### 菜单处理逻辑：

- **如果 R (审查详细发现):**
  - 逐节浏览验证报告
  - 展示每个验证步骤的发现
  - 允许用户提问
  - 审查后返回菜单

- **如果 E (使用编辑工作流):**
  - 解释："编辑工作流 (steps-e/) 可以使用此验证报告来系统地解决问题。编辑模式将指导你发现要编辑的内容、审查 PRD 并应用有针对性的改进。"
  - 提供："你想现在启动编辑模式吗？它将帮助你系统地修复验证发现。"
  - 如果是：完整阅读并遵循：steps-e/step-e-01-discovery.md
  - 如果否：返回菜单

- **如果 F (修复简单项目):**
  - 提供立即修复：
    - 模板变量（用适当内容填充）
    - 对话式填充（删除冗长短语）
    - 实施泄漏（从 FR/NFR 中删除技术名称）
    - 缺失的部分标题（添加 ## 标题）
  - 询问："你想让我进行哪些简单修复？"
  - 如果用户指定修复，进行修复并更新验证报告
  - 返回菜单

- **如果 X (退出):**
  - 显示："**验证报告已保存:** {validationReportPath}"
  - 显示："**摘要:** {overall status} - {recommendation}"
  - PRD 验证完成。完整阅读并遵循：`_bmad/core/tasks/bmad-help.md` 参数为 `Validate PRD`。

- **如果 其他:** 帮助用户，然后重新显示菜单

---

## 🚨 系统成功/失败指标

### ✅ 成功：

- 成功加载完整的验证报告
- 总结步骤 1-12 的所有发现
- 使用最终状态更新报告 frontmatter
- 正确确定总体状态（通过/警告/严重）
- 展示快速结果表
- 列出关键问题、警告和优势
- 包含整体质量评级
- 展示前 3 个改进
- 提供清晰的推荐
- 展示带有清晰解释的菜单选项
- 用户可以审查发现、获得帮助或退出

### ❌ 系统失败：

- 未加载完整的验证报告
- 缺少发现总结
- 未更新报告 frontmatter
- 未确定总体状态
- 缺少菜单选项
- 模糊的后续步骤

**主规则：** 用户需要清晰的总结和可操作的后续步骤。编辑工作流最适合复杂问题；简单问题可立即修复。
