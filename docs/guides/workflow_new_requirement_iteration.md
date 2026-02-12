# 指南：新需求迭代工作流 (How to Iterate New Requirements)

> **Core Question**: 当我要加新功能时，该怎么做？

Maglev 的迭代机制不是“打补丁”，而是 **"Diff-Based Compilation" (基于差异的编译)**。
你的每一次迭代，本质上都是在进行一次 **Spec Update -> Re-compile** 的过程。

---

## 1. 核心机制 (The Mechanism)

### "Golden Loop" (闭环)
Maglev 维护着一个从现实 (Code) 到 理想 (Spec) 的闭环。
*   **Reverse (逆向)**: 将代码现状和自维护信息（如数据库变更）同步回 Spec。
*   **Forward (正向)**: 将新需求写入 Spec。
*   **Compile (编译)**: AI 重新生成代码，只覆盖变动部分。

---

## 2. 操作流程 (The Process)

请遵循 **"一吸，二改，三生"** 的三步走策略：

### Step 1: 吸 (Sync Context) - *选做*
**目的**: 如果你刚才手动改过代码（Hotfix）或者数据库结构变了，必须先把这些变更“吸”回 Spec，否则 AI 生成时会覆盖掉它们。
*   **Action**: 运行 `maglev-reverse-spec` (或 `/reverse`)。
*   **Check**: 确认 `specs/10_reality/` 或 `specs/20_evolution/` 下的文档已更新。

### Step 2: 改 (Edit Spec) - *必做*
**目的**: 告诉 Maglev 你想要什么新功能。
*   **Scenario A: 简单的功能修改**
    *   直接修改 `specs/01_requirements.md` (需求描述)。
    *   例如：在 "用户登录" 章节添加 "支持手机号验证码登录"。
*   **Scenario B: 复杂的架构变更**
    *   除了改 `01_requirements.md`，还要修改 `specs/02_design.md` (接口定义/数据表)。
    *   例如：新增一张 `verify_codes` 表，定义其字段。

### Step 3: 生 (Generate Code) - *必做*
**目的**: 让 AI 将 Spec 的变更落地为代码。
*   **Command**: 运行 `maglev-quick-dev` (或 `/quick-dev`)。
*   **Input**:
    > "我更新了 Spec，新增了手机号登录功能，请实现它。"
*   **Verification**:
    *   AI 会分析 Spec 的 Diff。
    *   AI 会生成代码。
    *   AI 会运行测试。

---

## 3. 常见问题 (FAQ)

**Q: 我可以直接改代码吗？**
A: **原则上禁止**。如果你直接改了代码（比如改了 `login.ts`），下次你让 AI 加功能时，AI 可能会用它的“旧记忆”（Spec）生成的代码覆盖你的修改。
*   *例外*: 紧急 Hotfix。但事后必须补做 **Step 1 (吸)**。

**Q: AI 会把整个项目重写吗？**
A: **不会**。Maglev 的 `quick-dev` 技能具备 "Incremental Build" (增量构建) 能力。它会分析 Spec 哪里变了，只修改对应的代码文件。
