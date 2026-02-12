---
name: maglev-validate-spec-context
description: Maglev Spec 上下文校验器 (Protocol Enforcer)。
---

# Skill: Validate Spec Context (The Gatekeeper)

## 目标
充当 Ingest 和 Draft 之间的质量门禁。强制执行 `protocol_spec_context.md`。

## 职责
1.  **Schema Check**: 验证 JSON 结构是否符合标准。
2.  **Integrity Check**: 验证 JSON 中引用的物理文件 (Facts) 是否存在。
3.  **Fail Fast**: 一旦违规，立即抛错并终止流程。

## 输入
*   `ingest_context.json`: 待校验的上下文文件。
*   `protocol_spec_context.md`: 校验所依据的标准协议。

## 输出
*   **Success**: 无输出 (Silent Pass)。
*   **Failure**: 错误报告 (Error Report)。

## 必需的参考资料
*   工作流: `references/validate.workflow.md`
*   Step 1: `references/step-01-validate-schema.md`
