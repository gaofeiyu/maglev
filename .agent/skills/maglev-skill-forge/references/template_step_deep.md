---
name: {{step_name}}
description: {{step_description}}
next_step: {{next_step_path}}
---

# Step {{step_number}}: {{step_title}} (Deep Mode)

## 目标 (Goal)
{{goal}}

## ⚠️ 核心法则 (Mandatory Rules)
1.  **Facilitator Role**: 你是引导者，不是执行者。多问 "Why"，少直接 "Generate"。
2.  **No Hallucination**: 禁止在用户未输入核心信息前自动生成内容。
3.  **Gatekeeper**: 必须满足 [完成标准] 才能进入下一步。

## 引导话术 (Dialogue Script)
> **Opening**: "{{opening_question}}"

### 关键问题 (Key Questions)
请依次（或根据上下文）询问以下问题，确保挖掘深度：
1.  **Q1**: ...
2.  **Q2**: ...
3.  **Q3**: ... (Challenge the user: "Is this really true?")

## 动作序列 (Actions)
1.  **Inquire**: 执行上述引导对话。
2.  **Synthesize**: 总结用户输入，形成大纲。
3.  **Confirm**: "Is this what you meant?" [Y/n]
4.  **Write**: 仅在获得确认后，写入文件。

## 下一步 (Next Step)
*   **Trigger**: 用户输入 "Continue" 或 "确认"。
*   **Check**: 确认 `{{output_artifact}}` 已生成且不为空。
