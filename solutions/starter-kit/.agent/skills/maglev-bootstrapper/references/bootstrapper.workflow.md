---
name: bootstrapper
description: 执行 Maglev 初始化
output_folder: .
step_analyze: references/step-01-analyze.md
step_inject: references/step-02-inject.md
step_config: references/step-03-config.md
---

# Bootstrapper Workflow

**Goal**: 环境准备就绪 (Ready to Spec)。

## 流程 (Process)

### 1. Analyze (Step 01)
- 扫描根目录。
- 决策: `mode = GREENFIELD` (Empty) or `mode = ADOPTION` (Existing Files).

### 2. Inject (Step 02)
- 根据 `mode` 复制文件结构。
- **Source**: `solutions/starter-kit/` (如果在 Maglev 源码仓库中) 或从外部模板源。

### 3. Config (Step 03)
- 生成 `core_rules.md` (Context Injection).
- 设置 `repository_map.md`.

## 初始化
1. 阅读 `references/step-01-analyze.md`。
