# Step 3: Reconstruction (文明还原)

## 目标
将分析得出的 Logic Map 转化为无歧义、可读性强的 Technical Specification 草稿。

## 动作
1.  **Apply Template**: 使用 `references/legacy-tech-spec-template.md`。
2.  **Drafting**: 将代码逻辑翻译为自然语言。
3.  **Ref Injection**: **CRITICAL**. 每一句断言后必须追加 `[Ref: File.java:Lxx]`。
4.  **Highlight Unknowns**: 对于看不懂的代码，放入 "Assumption" 章节。

## 规则
*   **严禁脑补**: 只有代码里写的才能写进 Logic 章节。
*   **注释也是证据**: 代码注释可以提取为 "Intent"，但要标注 `[Ref: Comment]`。
*   **可视化**: 如果逻辑复杂，必须生成 Mermaid Flowchart。

## 交互
AI: "我已经完成了分析。正在生成 Spec 草稿... (生成中)... 草稿如下，请审阅。"
