---
name: step-02-search
description: 执行搜索与交叉验证
next_step: references/step-03-report.md
---

# Step 2: Search (搜索与验证)

## 目标
获取高质量信息，并区分"事实"与"软文/观点"。

## 动作
1.  **Exeucte**: 针对每个 KQ 执行 `search_web`。
2.  **Verify**:
    *   对于数据/参数：寻找官方文档或权威 Benchmark。
    *   对于评价：寻找 Hacker News, Reddit 等第三方讨论。
3.  **Record**: 在内存中建立 `Fact Table`：
    *   Fact: ...
    *   Source URL: ...
    *   Confidence: High/Medium/Low

## 规则
*   **No Hallucination**: 不确定的信息必须标记为 "待确认" 或再次搜索。
*   **Diversity**: 尽量寻找 2 个以上的独立数据源。
