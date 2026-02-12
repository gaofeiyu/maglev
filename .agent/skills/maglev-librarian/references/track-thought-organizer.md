# Track B: Thought Organizer (思想整理者) - Root Edition

## 目标
整理 `thinking/` 目录，生成决策日志 `thinking/README.md`。

## 逻辑 (Algorithm)
1.  **Scan**: 遍历 `thinking/*.md` 和 `thinking/archive/*.md`。
2.  **Extract**: 
    *   Frontmatter: `date`, `status`, `authors`
    *   Content: 提取第一个 H1 作为 Title，提取前 100 字符或 `Summary` 块作为摘要。
3.  **Sort**: 按 `date` 倒序排列 (最新的在最前)。
4.  **Render**: 生成一个 Timeline 风格的列表。

## 输出格式 (thinking/README.md)
```markdown
# Thinking & Decision Log

## Active
*   **[2024-03-20] 数据库选型分析** (Status: Proposed)
    *   *Summary*: 对比了 MySQL 和 PostgreSQL...
    *   [Read More](./db-selection.md)

## Archived
*   ...
```

## 指令
"请执行 Scan -> Extract -> Sort -> Render 流程。更新 `thinking/README.md`。"
