---
name: 'step-01-split-files'
description: '执行物理拆分与存档'
---

# 步骤 1: 拆分与存档 (Split & Persist)

## 目标
将 Unified Draft 转化为物理文件簇。

## 执行逻辑

### 1. 准备目录
*   从 `draft_unified.md` 的内容或 Frontmatter 中提取 `slug`。
*   创建目录: `{output_base}/{slug}/`
*   创建目录: `{output_base}/{slug}/context/`

### 2. 存档 Facts (Premise)
*   **Action**: 将 `{input_facts}` 复制到 `{output_base}/{slug}/context/input_facts.md`。
*   **意义**: 确立此 Spec 的 "输入事实基准"。

### 3. 拆分 Draft (Robust Splitting)
读取 `{input_draft}`，使用 Regex `<!-- FILE: (.*?) -->` 进行内容拆分。

**逻辑**:
1.  找到所有匹配 `<!-- FILE: {filename} -->` 的行。
2.  将该行之后、直到下一个 `<!-- FILE: ... -->` 之前的内容，写入 `{output_base}/{slug}/{filename}`。
3.  如果文件已存在，直接覆盖。

**支持的文件列表 (Expected)**:
*   `00_index.md`
*   `01_requirements.md`
*   `02_design.md`
*   `03_plan.md`
*   *(以及任何 AI 动态生成的附加文件)*

### 4. 前进
加载下一步: `./step-02-finalize.md`。
