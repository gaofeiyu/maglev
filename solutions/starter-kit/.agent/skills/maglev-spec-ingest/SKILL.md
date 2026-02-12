---
name: maglev-spec-ingest
description: (Atomic Skill) 负责摄入异构输入 (Idea/Doc/Legacy)，执行降噪处理，并生成标准化的 'Context JSON' 和 'Fact Snapshot'。
---

# Maglev Spec Ingest (摄入者)

> **Motto**: "我不生产信息，我只是信息的搬运工和清洗工。"

## 核心职责
作为 Spec 生成流水线的 **第一环**，本技能负责：
1.  **Input Normalization**: 将 "一句话意图"、"PRD文档" 或 "存量代码目录" 统一转化为结构化上下文。
2.  **Noise Reduction (降噪)**: 针对存量代码，仅提取骨架 (Skeleton) 和 模式 (Schema)，过滤具体实现细节。
3.  **Fact Extraction (取证)**: 生成 `input_facts.md`，作为后续验证的 "真理基准"。

## 输入 (Inputs)
用户需提供以下信息 (通过对话引导)：
*   **Intent**: 想要做什么？
*   **Source**: 输入源是什么？(Idea / Doc Path / Legacy Dir)

## 输出 (Outputs)
本技能不直接生成 Spec，而是生成中间产物：
1.  **`ingest_context.json`**: 供 `spec-draft` 消费的机器可读上下文。
2.  **`input_facts.md`**: 供 `spec-crystallize` 存档的人类可读基准。

## 必需的参考资料
*   工作流: `references/ingest.workflow.md`
*   Step 1 (Identify): `references/step-01-identify-source.md`
*   Step 2 (Map): `references/step-02-map-skeleton.md`
*   Step 3 (Zoom): `references/step-03-zoom-extract.md`

## 工具依赖 (Tool Dependencies)
*   **Antigravity Optimized**: 本技能深度依赖 `view_file_outline` 工具进行存量代码降噪。在非 Google Agent 环境下可能需要人工调整 Prompt 以模拟此能力。
