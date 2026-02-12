# Track A: Spec Curator (规格策展人) - Root Edition

## 目标
扫描 `solutions/` 目录，生成层级化的索引文件 `solutions/README.md`。

## 逻辑 (Algorithm)
1.  **Scan**: 递归遍历 `solutions/starter-kit`, `solutions/guides`, `solutions/skills`, `solutions/templates`。
2.  **Extract**: 对于每个 `.md` 文件，读取 Frontmatter：
    *   `title`
    *   `status` (draft/review/accepted/done)
    *   `complexity_tier`
    *   `slug` (if available)
3.  **Group**: 按子目录分组 (starter-kit, guides, skills...)。
4.  **Render**: 使用 Markdown 表格或列表渲染索引。

## 输出格式 (solutions/README.md)
```markdown
# Solution Index (产品交付物索引)

> **Maglev Enabler**: 这些是 Maglev 交付给用户的核心能力与资产。

## skills (智能技能)
*Smart Agents.*

| 技能名称 | 描述 |
| :--- | :--- |
| maglev-librarian | 图书管理员 |

## starter-kit (启动套件)
*Boilerplates.*

## guides (指南)
*How-to Manuals.*
```

## 指令
"请执行 Scan -> Extract -> Group -> Render 流程。直接 **Overwrite** `solutions/README.md` 文件。**必须使用中文标题和描述**。"
