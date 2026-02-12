---
description: maglev-plan-unit-tests-frontend Workflow
---

# Frontend Unit Test Planning Workflow

## 流程概览

```mermaid
graph TD
    Start[开始规划] --> S1[Step 1: Analyze Spec]
    S1 --> C1{确认继续?}
    C1 -->|Y| S2[Step 2: Identify Targets]
    C1 -->|n| Exit[退出]
    S2 --> C2{继续设计 Mock?}
    C2 -->|Y| S3[Step 3: Mock Strategy]
    C2 -->|n| S4
    S3 --> S4[Step 4: Generate Skeleton]
    S4 --> End[输出测试代码]
```

## Checkpoint 规则
1.  Step 1 后：展示 Spec 分析结果
2.  Step 2 后：展示测试目标清单
3.  Step 3 后：展示 Mock 策略
4.  Step 4 后：输出测试骨架代码

## 输入方式
- **指定 Spec**: `/maglev-plan-unit-tests-frontend specs/.../02_frontend.md`
- **指定组件**: `/maglev-plan-unit-tests-frontend src/views/OrderList.vue`
