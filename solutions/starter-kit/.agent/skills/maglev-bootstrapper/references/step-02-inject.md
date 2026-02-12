---
name: step-02-inject
description: 骨架注入
next_step: references/step-03-config.md
---

# Step 2: Structure Injection (骨架注入)

## 目标
物理创建 Maglev 标准目录结构。

## 动作
1.  **Inject Core**:
    *   Copy `.agent/` -> Root.
    *   Copy `.maglev/` -> Root.
    *   Create `specs/`, `docs/`, `issues/`, `tests/`.
2.  **Handle Mode**:
    *   **Greenfield**: Create `code_storages/` directory.
    *   **Adoption**: 
        *   Ask user: "Should I move existing `src` to `code_storages/` (Recommended) or keep it in Root (Legacy Mode)?"
        *   If Legacy Mode, note this for config step.

## 关键指令
- 使用 `mkdir -p` 创建目录。
- 确保不要覆盖用户已有的重要文件 (如 `.gitignore`)。

## 交互示例
AI: "Injecting Maglev core structures..."
AI: "Done. `specs/`, `.agent/` created."
