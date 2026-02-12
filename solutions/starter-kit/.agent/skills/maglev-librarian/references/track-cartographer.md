# Track C: Cartographer (制图师) - Root Edition

## 目标
辅助更新根目录下的 `repository_map.md`。

## 逻辑 (Algorithm)
> 注意：这是一个轻量级的 Mapping，不是完整的 AST 分析。

1.  **Overview**: 使用 `tree -L 2 -d` (MaxDepth 2, Directories only) 获取高层结构。
2.  **Listing**: 列出关键的 Top-Level 文件 (如 `package.json`, `pom.xml`, `Dockerfile`, `README.md`, `INDEX.md`, `llms.txt`)。
3.  **Annotation**: 对于每个目录，尝试推断其职责 (e.g., `solutions/starter-kit` -> 用户启动包)。

## 输出格式
将内容写入 `repository_map.md` (或覆盖现有内容)。
使用简单的 Markdown Tree 格式。

```markdown
# Repository Map

Project Root: `/`

## Directory Structure
- `code_storages/` - Code Repositories
    - `my-core-repo/`   <-- (User defined repository name)
    - `legacy-service/` <-- (Supports multiple repos)
- `docs/` - Documentation
- `specs/` - Maglev Specifications

## Key Entry Points
- Web App: `code_storages/my-core-repo/src/index.js`
- API Server: `code_storages/legacy-service/main.go`
```
