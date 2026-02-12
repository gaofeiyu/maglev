---
description: maglev-code-review-frontend Workflow
---

# Frontend Code Review Workflow

## 流程概览

```mermaid
graph TD
    Start[开始审查] --> S1[Step 1: Load Context]
    S1 --> C1{确认继续?}
    C1 -->|Y| S2[Step 2: Component Compliance]
    C1 -->|n| Exit[退出]
    S2 --> C2{继续质量检查?}
    C2 -->|Y| S3[Step 3: Quality Check]
    C2 -->|n| S4
    S3 --> S4[Step 4: Generate Review]
    S4 --> End[输出 Review]
```

## Checkpoint 规则
1.  Step 1 后：展示加载的组件和关联 Spec
2.  Step 2 后：展示组件合规性检查结果
3.  Step 3 后：展示质量检查结果
4.  Step 4 后：输出 Review 意见

## 输入方式
- **单文件**: `/maglev-code-review-frontend src/views/OrderList.vue`
- **Git Diff**: `/maglev-code-review-frontend --diff HEAD~1`
- **指定 Spec**: `/maglev-code-review-frontend src/views/OrderList.vue --spec specs/.../02_frontend.md`
