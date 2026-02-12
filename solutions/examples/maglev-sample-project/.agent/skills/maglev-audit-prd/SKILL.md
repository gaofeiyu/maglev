---
name: maglev-audit-prd
description: 01_requirements.md 的严格产品质量审计 (Maglev 标准 v2.0)
version: 1.0.0
---

# Maglev PRD 审计技能 (Audit PRD Skill)

**角色**: "严格的产品经理" (价值守门人)
**目标**: `01_requirements.md` (单文件)

## 目的
在进入技术设计之前，根据 Maglev 质量标准严格审计需求文档 (PRD)。此技能确保工程资源不会浪费在模棱两可、不可测试或低价值的需求上。

## 能力范围
1.  **SMART 分析**: 验证功能需求是否具体 (Specific)、可测量 (Measurable) 等。
2.  **AC 完备性**: 检查每个用户故事是否有明确的验收标准 (Acceptance Criteria)。
3.  **优先级扫描**: 确保 P0/P1/P2 的平衡分布 (如果全是 P0 则发出警告)。
4.  **格式合规性**: 验证 `AS A...` 语法和 Markdown 结构。

## 用法
```bash
/maglev-audit-prd file="specs/feat-login/01_requirements.md"
```

## 工作流
1.  **摄入**: 读取目标文件。
2.  **扫描**: 运行 `audit-prd.workflow.md`。
    *   步骤 A: 结构与格式
    *   步骤 B: 故事与 AC 质量
    *   步骤 C: 需求与逻辑
3.  **报告**: 输出包含具体行动项的 `## 🛡️ Maglev 产品审计报告`。
