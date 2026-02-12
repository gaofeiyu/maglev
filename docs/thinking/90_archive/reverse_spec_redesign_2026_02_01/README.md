# maglev-reverse-spec 重构设计档案

**归档日期**: 2026-02-01
**关联 Issue**: `/issue.md` (存量项目逆向问题反馈)

## 📂 文件清单
| 文件 | 用途 |
|------|------|
| `implementation_plan.md` | Page-First 全栈逆向架构设计 |
| `task.md` | 重构任务清单 (Checklist) |
| `walkthrough.md` | (执行完成后) 实施总结报告 |

## 🎯 核心变更
1.  **Page-First 策略**: 从页面入手，追踪前后端调用链。
2.  **Guided Mode**: 恢复 BMAD 式强制检查点。
3.  **Multi-Stack Adapters**: 支持 Java/Python/Go/Node/Rust 等多技术栈。
4.  **00-03 标准输出**: 逆向产物强制符合 Spec Cluster 结构。

## 🔗 关联资产
- 最终技能: `solutions/starter-kit/.agent/skills/maglev-reverse-spec/`
- 上游调用者: `maglev-legacy-adopter`
