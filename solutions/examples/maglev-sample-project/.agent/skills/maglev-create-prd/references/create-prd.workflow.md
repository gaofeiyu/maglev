---
name: create-prd
description: PRD 三模态工作流 - 创建、验证或编辑综合性 PRD (Maglev Edition)
# Maglev: Hardcoded Config
output_folder: '{project-root}/specs/20_evolution/active'
nextStep: 'references/step-c-01-init.md'
validateWorkflow: 'references/step-v-01-discovery.md'
editWorkflow: 'references/step-e-01-discovery.md'
---

# PRD 工作流 (三模态) - Maglev Edition (v2.0 Standard)

**目标:** 通过结构化工作流创建、验证或编辑综合性 PRD。

**Maglev 标准:**
- **Output**: `specs/20_evolution/active/{slug}/01_requirements.md`
- **Language**: Chinese (Simplified)
- **Flattened Paths**: 所有步骤文件位于同一 `references/` 目录。
- **Compressed Flow**: Init -> Discovery -> Stories -> Functional -> Non-Functional -> Complete.

---

## 模式确定

### 检测工作流模式
## 工作流架构

### 核心原则
- **微文件设计**: 每个步骤都是一个独立的指令文件，是整体工作流的一部分，必须严格遵循
- **即时加载**: 内存中只有当前的步骤文件 - 在被告知之前绝不加载未来的步骤文件
- **顺序强制**: 必须按顺序完成步骤文件中的序列，不允许跳过或优化
- **状态跟踪**: 当工作流生成文档时，使用 `stepsCompleted` 数组在输出文件 frontmatter 中记录进度
- **仅追加构建**: 按照指示将内容追加到输出文件来构建文档

### 关键规则 (无例外 - SECURITY LEVEL: HIGH)
- 🛑 **绝不** 同时加载多个步骤文件
- 📖 **务必** 在执行前阅读整个步骤文件
- 🚫 **绝不** 跳过步骤或优化顺序
- 💾 **务必** 在为特定步骤编写最终输出时更新输出文件的 frontmatter
- 🎯 **务必** 遵循步骤文件中的确切说明
- ⏸️ **务必** 在菜单处停止并等待用户输入
- 📋 **绝不** 从未来的步骤创建心理待办事项列表

### 步骤处理规则
1. **完整阅读**: 在采取任何行动之前，务必阅读整个步骤文件
2. **遵循顺序**: 按顺序执行所有编号的部分，绝不偏离
3. **等待输入**: 如果出现菜单，停下来等待用户选择
4. **检查继续**: 如果步骤有一个带有“继续”选项的菜单，只有当用户选择 'C' (继续) 时才进行下一步
5. **状态保存**: 每次行动后必须更新 `stepsCompleted`

---

## 初始化序列

### 1. 配置加载
无需加载外部 Config。使用 Maglev 标准配置：
- **Language**: Chinese (Simplified)

### 2. 路由到适当的工作流

**如果 mode == create:**
"**创建模式: 从头开始创建一个新的 PRD。**"
完整阅读并遵循: `{nextStep}` (`references/step-c-01-init.md`)

**如果 mode == validate:**
"**验证模式: 根据 BMAD 标准验证现有的 PRD。**"
提示输入 PRD 路径: "你想要验证哪个 PRD？请提供 PRD.md 文件的路径。"
然后完整阅读并遵循: `{validateWorkflow}` (`references/step-v-01-discovery.md`)

**如果 mode == edit:**
"**编辑模式: 改进现有的 PRD。**"
提示输入 PRD 路径: "你想要编辑哪个 PRD？请提供 PRD.md 文件的路径。"
然后完整阅读并遵循: `{editWorkflow}` (`references/step-e-01-discovery.md`)
