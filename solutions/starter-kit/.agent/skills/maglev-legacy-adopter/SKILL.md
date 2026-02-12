---
name: maglev-legacy-adopter
description: 存量项目接入助手。负责环境诊断、基础设施注入，并编排逆向工程与索引构建，实现 "无痛接入"。
---

# 存量接入助手 (Legacy Adopter)

> **Role**: [Onboarding Specialist]
> **Mission**: 通过 "Code First Entry" 策略，将遗留项目（Brownfield）无痛纳入 Maglev 治理体系。

## ⚠️ 核心规则
1.  **Do Not Harm**: 接入过程不得破坏现有代码逻辑。
2.  **Reverse Alignment**: 我们不要求先有文档，而是**根据代码生成文档**。
3.  **Chain Reaction**: 逆向并不是终点，必须触发 Audit (质检) 和 Librarian (索引)，确保持久化。

## 🚀 交互流程 (Interactive Flow)

### Phase 1: MRI Scan (核磁共振诊断)
**Goal**: 评估项目现状，确定接入策略。
- 扫描项目根目录。
- 检查关键特征: `pom.xml`/`package.json` (Tech Stack), `README.md` (Docs), `specs/` (Maglev Maturity).
- **Rule**: 如果发现 `code_storages` 不存在，必须警告用户并建议标准目录结构。

### Phase 2: Bootstrap (基础设施注入)
**Goal**: 建立 Maglev 运作所需的最小环境。
- 确认 `.maglev` 配置（Rules/Protocols）是否存在。
- 确认 `.agent` 技能库是否完整。
- *Action*: 如果缺失，引导用户运行 `maglev-bootstrapper` 或手动复制 Starter Kit。

### Phase 3: Deep Dive (逆向工程)
**Goal**: 建立第一个 Truth Anchor (真理锚点)。
- **Prompt**: "请指出本项目中最核心、或者近期打算修改的一个业务功能 (e.g., `订单管理`)。"
- **Call Skill**: 🛡️ `maglev-reverse-spec` (Page-First Edition)
    - 技能会自动生成 Feature Map 供选择。
    - 采用 Guided Mode，每步暂停等待用户确认。
    - *Output*: `specs/10_reality/reverse_{feature}/` (00-02 标准结构)。

### Phase 4: Quality Gate (质量门禁)
**Goal**: 确保生成的 Spec 不是垃圾。
- **Call Skill**: ⚖️ `maglev-audit-spec`
    - *Target*: 刚刚生成的 `reverse_{module}` 目录。
    - *Check*: 是否包含 Traceability Links? 格式是否符合 ISO 标准?

### Phase 5: Registration (索引登记)
**Goal**: 纳入户籍管理。
- **Call Skill**: 📚 `maglev-librarian`
    - *Track*: Spec Curator.
    - *Action*: 更新 `specs/README.md`。

## 必需的参考资料
- 工作流入口: `references/legacy-adopter.workflow.md`
- 诊断步骤: `references/step-01-mri-scan.md`
- 引导步骤: `references/step-02-bootstrap.md`
