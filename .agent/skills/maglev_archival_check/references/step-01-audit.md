---
name: step-01-audit
description: 交互式审查步骤
checklist_path: references/checklist.md
---

# Step 1: 交互式归档审查

## 目标
对照 `references/checklist.md`，检查当前会话的产出是否符合 Maglev 归档标准。

## 规则
1.  **逐项核对**: 不要一次性抛出所有问题。按章节 (Section) 进行核对。
2.  **Auto-Detect**: 尽可能利用你的上下文读取能力自动判断。
    *   例如：检查 `contributors/contribution_log.md` 是否有最近的修改。
    *   如果已修改，直接标记 ✅。
    *   如果未修改，询问用户："我注意到 Contribution Log 尚未更新，是否需要我现在添加记录？"
3.  **Strict Mode**: 对于标记为 `[BLOCKER]` 或 `[CRITICAL]` 的项，必须获得明确的 Done 信号。

## 执行序列

### 1. Load Checklist
读取 `{checklist_path}` 内容。

### 2. Section Audit (循环)

**对于清单中的每个主要部分 (Headers):**

1.  **分析上下文**:
    *   查看相关文件 (`solutions/`, `docs/thinking/`, `issues/`) 的最近变动。
2.  **生成状态报告**:
    *   列出你认为 **已完成** 的项 (Evidence Based)。
    *   列出你认为 **缺失** 或 **存疑** 的项。
3.  **交互**:
    *   向用户展示该部分的审查结果。
    *   询问："这一部分是否通过？" 或提示修复。

### 3. Contribution Log Check (Critical)
*   **Action**: 读取 `contributors/contribution_log.md`。
*   **Check**: 最后一条记录是否包含本次会话的核心变更？
*   **Fix**: 如果否，提议："建议添加一条 Log: ... 你同意吗？"

### 4. Final Verdict
所有部分通过后，输出：
"✅ **归档审查通过 (Archival Check Passed)**.
所有资产已就位。Session Ready to Close."
