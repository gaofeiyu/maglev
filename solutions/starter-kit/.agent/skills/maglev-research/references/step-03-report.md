---
name: step-03-report
description: 生成调研报告
---

# Step 3: Report (生成报告)

## 目标
输出结构化、带引用的报告。

## 动作
1.  **Draft**: 撰写 Markdown 报告。
2.  **Save**: 保存至 `docs/research/{date}-{slug}.md`。
3.  **Review**: 提交给用户审阅。

## 模板
```markdown
# Research: {Topic}
Date: {YYYY-MM-DD}

## 1. Executive Summary (摘要)
[1-paragraph concise summary]

## 2. Key Questions & Findings (关键发现)
### Q1: {Question 1}
- **Finding**: ...
- **Evidence**: ... [1]

### Q2: {Question 2}
...

## 3. Analysis & Recommendation (建议)
[Your synthesized opinion]

## 4. References (引用)
1. [Title](URL) - {Source Name}
2. ...
```
