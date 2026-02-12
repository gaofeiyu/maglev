---
name: 'step-02-extract-facts'
description: '执行降噪逻辑并生成标准化产物'
output_json: '{project-root}/.maglev/temp/ingest_context.json'
output_facts: '{project-root}/.maglev/temp/input_facts.md'
---

# 步骤 2: 提取事实 (Extract Facts)

## 目标
执行 "Map -> Skeleton -> Schema" 降噪逻辑，生成最终产物。

## 执行逻辑 (根据 Type)

### Type 1: Idea (纯意图)
*   **Action**: 无需扫描文件。
*   **Generate JSON**:
    ```json
    { "intent": "{user_text}", "constraints": [], "refs": {} }
    ```
*   **Generate Facts**:
    写入 `input_facts.md`:
    ```markdown
    # Input Facts: Idea
    *   **Intent**: {user_text}
    ```

### Type 2: Docs (文档)
*   **Action**: 使用 `read_file` 读取目标文档。
*   **Extract**: 提取 Core Goal, Constraints。
*   **Generate JSON**: `{ "intent": "...", "constraints": ["..."], "refs": { "doc": "{path}" } }`
*   **Generate Facts**:
    写入 `input_facts.md`:
    ```markdown
    # Input Facts: Doc Ingestion
    *   **Source**: {path}
    *   **Summary**: {summary_of_doc}
    ```

### Type 3: Legacy (存量代码)
> **⚠️ Compatibility Note (兼容性提示)**:
> 本步骤使用了 Antigravity 原生工具 `view_file_outline` 以实现极速降噪（只读骨架不读全文）。
> 如果您在使用 Cursor/Windsurf 等其他 Agent，请忽略此工具指令，改用 `read_file` 并提示 AI "仅提取函数签名，不要读取具体实现"。

*   **Action 1 (Map)**: `list_dir` 目标目录。过滤掉 `test`, `mock`。
*   **Action 2 (Skeleton)**: 对关键文件执行 `view_file_outline`。提取 Signatures。
*   **Action 3 (Schema)**: 对 Entity/DTO 文件执行 `read_file` 或 `grep` (针对 SQL)。
*   **Generate JSON**: 
    ```json
    { 
      "intent": "Refactor/Extend Legacy", 
      "refs": { 
          "signatures": ["..."], 
          "schema": ["..."] 
      } 
    }
    ```
*   **Generate Facts**:
    写入 `input_facts.md`:
    ```markdown
    # Input Facts: Legacy Analysis
    *   **Target**: {dir}
    
    ## 1. Interface Skeleton
    {signatures_summary}
    
    ## 2. Data Schema
    {schema_summary}
    ```

## 结束
报告：
"Ingest 完成。
已生成 Context: `{output_json}`
已生成 Facts: `{output_facts}`"
