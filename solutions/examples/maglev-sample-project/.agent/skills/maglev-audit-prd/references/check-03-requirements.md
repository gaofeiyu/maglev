---
name: 'check-03-requirements'
description: '审计功能需求和优先级'

# References
# End of workflow
nextStepFile: 'END' 
targetFile: '{targetFile}'
---

# 审计步骤 3: 需求与逻辑

**下一步**: 完成

## 目标
验证功能需求 (FR) 和非功能需求 (NFR) 的质量。

## 规则
- 🛑 **只读**: 不要修改输入文件。
- ⚖️ **优先级检查**: 确保存在 P0/P1/P2 标签。

## 审计检查清单

### 1. 功能需求 (FR)
- [ ] 检查 `## 2. ...` 章节。
- [ ] **SMART 扫描**: 需求是否具体? (例如 "快" vs "< 200ms")。
- [ ] **优先级**: 表格中是否可见 `P0`, `P1` 标签?

### 2. NFR 与约束
- [ ] 检查 `## 3. ...` 章节。
- [ ] 验证标准类别的存在性 (性能, 安全)。

## Output Schema
Append to **Audit Report** and **Finalize**:

```markdown
## 3. 需求逻辑检查 (Requirements Logic)
| 检查点 (Check) | 状态 (Status) | 建议 (Suggestion) |
| :--- | :--- | :--- |
| **SMART 等级** | {High/Med/Low} | {e.g. "FR-01 is vague"} |
| **优先级分布** | {PASS/WARN} | {e.g. "All items are P0"} |
| **NFR 存在性** | {PASS/FAIL} | {Missing NFRs?} |

---
**审计完成 (Audit Complete)**. 
**最终结论 (Verdict)**: {PASS / CONDITIONAL PASS / FAIL}
```
