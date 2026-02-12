---
title: '{title}'
slug: '{slug}'
type: spec
complexity_tier: '2-Feature' # Default. Options: 1-Atomic, 2-Feature, 3-Arch
maglev_status: 'draft' # draft -> review -> accepted
created: '{date}'
status: 'in-progress'
stepsCompleted: []
tech_stack: []
files_to_modify: []
---

# 统一规范草稿: {title}

> **指南**: 这是临时暂存区。定稿后，此文件将被拆分为 `00_index.md`, `01_requirements.md`, `02_design.md` 和 `03_plan.md`。

## 00. 索引与元数据 (-> 00_index.md)
*   **负责人**: {user}
*   **状态**: 规划中 (Planning)
*   **最后更新**: {date}

## 01. 需求契约 (-> 01_requirements.md)

### 1.1 核心意图 (Intent)
{intent}

### 1.2 用户故事 (User Stories)
{user_stories}

### 1.3 验收标准 (Acceptance Criteria)
{acceptance_criteria}

### 1.4 粗略边界 (Rough Boundaries)
{boundaries}

## 02. 技术蓝图 (-> 02_design.md)
> **多态设计**: 根据项目类型适配 (UI / Logic / Agent)。

### 2.1 架构视图 / 领域图
{architecture}

### 2.2 数据模型 / Schema 变更
{data_model}

### 2.3 API 接口定义
{api_interface}

### 2.4 核心逻辑 / 交互表
{core_logic}

## 03. 实施计划 (-> 03_plan.md)

### 3.1 任务清单 (Tasks)
{tasks}

### 3.2 验证计划
{verification_plan}
