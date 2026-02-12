---
description: maglev-reverse-spec Workflow (Page-First Edition)
---

# Reverse Spec Workflow

本工作流定义了 Page-First 全栈逆向的完整流程。

## 流程概览

```mermaid
graph TD
    Start[Start] --> S0[Step 00: Integrity Check]
    S0 --> S1[Step 1: Project Map]
    S1 --> C1{用户选择功能}
    C1 -->|选择| S2[Step 2: Page Analysis]
    C1 -->|Smart| S1b[Step 1b: Router Analysis]
    S1b --> C1
    C1 -->|all| Loop[循环处理]
    S2 --> C2{继续追踪?}
    C2 -->|Y| S3[Step 3: Stack Trace]
    C2 -->|n| Exit[退出]
    S3 --> S3b[Step 3b: Intent Speculation]
    S3b --> C3{生成Spec?}
    C3 -->|Y| S4[Step 4: Spec Handoff Reuse]
    C3 -->|n| Exit
    S4 --> S4a[Standard Draft]
    S4a --> C4{写入?}
    C4 -->|confirm| S5[Step 5: Crystallize & Archive]
    S5 --> S6[Step 06: Verify Output]
    S6 --> C5{继续下一个?}
    C5 -->|Y| S1
    C5 -->|n| End[结束]
```

## Checkpoint 规则
1.  **每个 Step 结束后必须暂停**，展示阶段性产物。
2.  **等待用户确认** (`[Y/n]` 或 `[confirm/edit]`)。
3.  **用户可随时退出** (输入 `exit` 或 `n`)。

## 执行顺序

| Step | 名称 | 产出 | 参考文件 |
|------|------|------|----------|
| 00| **Integrity Check** | System Ready | `step-00-integrity-check.md` |
| 1 | Project Map | Feature Map (功能地图) | `step-01-project-map.md` |
| 1b| Router Analysis | Refined Map (路由分析) | `step-01b-router-analysis.md` |
| 2 | Page Analysis | Page Context (组件+API) | `step-02-page-analysis.md` |
| 3 | Stack Trace | Backend Context (调用链) | `step-03-stack-trace.md` |
| 3b| Intent Speculation | Intent Context (推测+Quest) | `step-03b-intent-enrichment.md` |
| 4 | Spec Handoff | Standard Unified Draft | `wrapper-04-spec-handoff.md` |
| 5 | **Crystallize** | **Archived Spec & Facts** | `../maglev-spec-crystallize/references/crystallize.workflow.md` (output_base: specs/10_reality) |
| 06| **Verify Output** | Quality Gate | `step-06-verify-output.md` |

## 异常处理
- **纯后端项目**: 跳过 Step 2，直接从 Step 3 开始。
- **纯前端项目**: Step 3 仅记录 API 契约，不追踪后端实现。
- **用户中断**: 随时可输入 `exit` 退出，已完成的 Spec 不受影响。
