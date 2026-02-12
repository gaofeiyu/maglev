# 归档审查表 (Archival Checklist)

为了防止信息流失，确保每次沟通、头脑风暴或方案探讨后，相关知识都能正确沉淀，请对照下表进行审查：

## 1. 核心产出 (Solutions)
- [ ] **是否达成了新的共识或方案？**
    - 如是，是否已整理为清晰的文档存入 `solutions/`？
- [ ] **方案是否具备详细的实施步骤？**
    - 关键决策是否已记录？

## 2. 思考过程 (Thinking)
- [ ] **是否有未被采纳但有价值的思路？**
    - 如是，是否已记录在 `thinking/` 目录中？
- [ ] **是否有对现有角色的新理解或反思？**
    - 是否更新了相关的分析文档（如 `ai_role_evolution_analysis.md`）？

## 3. 历史废案 (Archive)
- [ ] **是否有旧方案被推翻？**
    - 如是，旧文件是否已移动至 `archive/`？
    - 是否在旧文件中注明了废弃原因？

## 4. 参考资料 (References)
- [ ] **沟通过程中是否提到了新的论文、工具或文章？**
    - 如是，是否已按规范归档至 `references/`？
    - 是否创建了相应的摘要文档？

## 5. 贡献记录 (Contributors) [BLOCKER]
- [ ] **必须检查：本轮会话的 Delta 是否已记录？**
    - 不要只看文件是否存在，要看 **最后几行是否包含刚才做的事** (e.g. 刚加的 Reference, 刚改的 Matrix)。
    - **Intent Check**: 必须明确记录 Human 的关键意图 (Prompt Summary)。
    - **Update**: 必须更新 `contributors/contribution_log.md`。

## 6. AI 技能 (AI Skills)
- [ ] **本次产出是否可以封装为 Skill？**
    - 如果是流程或操作指南，是否建立了对应的 Skill (in `.agent/skills/`)？
- [ ] **现有 Skill 是否需要同步更新？**
    - 核心文档变更后，Skill 的 Prompt 或引用路径是否依然有效？

## 7. 产品隔离性 (Product Isolation) [CRITICAL]
- [ ] **Starter Kit 是否包含私有路径？**
    - 检查 `solutions/starter-kit/` 下的文件，**严禁引用** `maglev/`, `contributors/` 等仅存于母体仓库的目录。
    - **Self-Correction**: Starter Kit 只能引用 `specs/`, `docs/`, `.maglev/` 这些标准目录。
- [ ] **通用性检查**:
    - Prompt 是否假设了特定的业务上下文（如 "MindBase"）？如有，请替换为 `{{PROJECT_NAME}}` 或通用描述。

## 8. 索引同步 (Index Synchronization) [CUSTODIAN]
- [ ] **Master Index 更新**: 顶层 `INDEX.md` 是否包含最新模块？
- [ ] **Sub-Index 更新**: `thinking/README.md` 等子索引是否列出了新文件？
- [ ] **Dashboard 更新**: `issues/README.md` 是否反映了最新任务状态？

---
*建议在每次 `notify_user` 结束当前任务块前，快速过一遍此表。*
