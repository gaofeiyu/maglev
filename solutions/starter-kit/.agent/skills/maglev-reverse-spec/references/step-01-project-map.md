---
description: maglev-reverse-spec Step 1 - Project Map
---

# Step 1: Project Map (项目地图)

## 目标
宏观理解项目结构，识别技术栈，生成用户可感知的功能入口清单 (Feature Map)。

## 执行逻辑 (Interactive Scan)

### 1.1 初期勘测 (Initial Survey)
*   **Action**: 仅扫描项目根目录及二级目录 (Depth=2)，**不读取**文件内容。
*   **Goal**: 识别技术栈和文件规模。

### 1.2 策略协商 (Strategy Negotiation)
向用户汇报勘测结果，并请求下一步指令：

> "⚠️ 项目勘测完成。
> - 技术栈: {TechStack}
> - 规模: `src/pages` 下约 {N} 个文件。
>
> 请选择扫描策略:
> - **[S]mart (推荐)**: 仅分析 `router` 配置文件来推断页面结构。(省 Token)
> - **[D]eep**: 强制扫描所有页面文件。(高消耗，可能需要分批)
> - **[M]anual**: 我来手动指定核心文件的路径。"

### 1.3 执行扫描 (Execution)
根据用户选择：
*   **[S]**: 加载 `references/step-01b-router-analysis.md` 并执行。
*   **[D]**: 执行全量扫描 (注意分批)。
*   **[M]**: 等待用户输入路径列表，然后读取。

### 1.4 Feature Map 生成
将识别到的入口整理为 JSON。

## 失败处理
- **无前端检测到**: 提示用户这是一个纯后端项目，将直接从 API 入口开始。
- **无后端检测到**: 提示用户这是一个纯前端/静态项目，逆向将仅生成 UI Spec。
