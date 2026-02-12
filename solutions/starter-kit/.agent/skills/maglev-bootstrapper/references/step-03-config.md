---
name: step-03-config
description: 协议配置
---

# Step 3: Protocol Configuration (协议配置)

## 目标
实例化规则文件，完成最后的一公里配置。

## 动作
1.  **Generate Core Rules**:
    *   Read `.maglev/rules/core_rules.md`.
    *   Replace `{{PROJECT_NAME}}` with actual folder name.
    *   Write to `.maglev/config/core_rules.md`.
2.  **Setup User Config**:
    *   Check if `.maglev/user.yaml` exists. If not, copy `user.example.yaml`.
3.  **Setup Repository Map**:
    *   Create `specs/10_reality/repository_map.md`.
    *   If Adoption Mode, register the legacy `src` path in the map.

## 完成 (Finalize)
告知用户：
"🚀 Maglev 初始化完成！
1. 核心法则已注入。
2. 技能库已就绪。
请尝试输入: `创建第一个 Spec`。"
