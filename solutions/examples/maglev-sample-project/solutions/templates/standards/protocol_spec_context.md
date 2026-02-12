# Maglev Spec Context Protocol (v1)

> **Type**: Data Contract (Json Schema)
> **Usage**: Ingest Skill -> [Validator] -> Draft Skill

## 1. 核心理念
此协议解耦了 "Context Provider" (Ingest) 和 "Context Consumer" (Draft)。
无论上游如何扫描代码（Listing, Reading, Grepping），最终必须生成符合此标准的 JSON，才能被下游消费。

## 2. JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["meta", "facts"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["slug", "intent", "type"],
      "properties": {
        "slug": { 
          "type": "string", 
          "description": "Unique identifier for this change (URL-safe)" 
        },
        "intent": { 
          "type": "string", 
          "description": "User's original intent description" 
        },
        "type": { 
          "type": "string", 
          "enum": ["idea", "doc", "legacy", "incremental", "fast-track"] 
        },
        "source": { "type": "string" },
        "complexity": { "type": "string", "enum": ["low", "high", "incremental"] }
      }
    },
    "facts": {
      "type": "object",
      "required": ["input_facts_path"],
      "properties": {
        "input_facts_path": { 
          "type": "string", 
          "description": "Absolute path to the generated input_facts.md" 
        },
        "base_spec_path": { 
          "type": "string", 
          "description": "Path to existing spec if incremental" 
        }
      }
    },
    "refs": {
      "type": "object",
      "description": "Explicit references to key files (optional)",
      "properties": {
        "deep_dive_targets": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  }
}
```

## 3. 字段说明

### `meta`
*   **slug**: 用于生成目录名 (e.g., `vip-icon-update`).
*   **type**: 决定 Draft 采取什么策略 (e.g., `fast-track` 可能会跳过某些复杂的架构检查).

### `facts`
*   **input_facts_path**: 上游生成的 Markdown 事实文件的**绝对路径**。Draft Skill 将读取此文件作为 LLM 的 Context。这是 "Context by Reference" (传引用) 而非传值，避免 JSON 过大。

## 4. 验证规则 (Validator Rules)
Validator Skill 将检查：
1.  JSON 格式符合 Schema。
2.  `facts.input_facts_path` 指向的文件确实**存在**。
