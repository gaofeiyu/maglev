---
description: maglev-reverse-spec Step 06 - Verify Output
---

# Step 06: Verify Output (产出验证)

## 目标
作为 Quality Gate (质量门禁)，并在任务结束前验证 Spec 文件簇的完整性和归档状态。

## 验证逻辑

### 1. 全局路径确认
根据上下文中的 `slug`，构建预期路径：
`Target: specs/10_reality/reverse_{slug}/`

### 2. 核心文件检查 (Existence Check)
检查以下文件是否存在：
- [ ] `00_index.md` (索引)
- [ ] `01_requirements.md` (核心需求)
- [ ] `02_design.md` (设计)

### 3. 归档检查 (Critical Archival Check)
检查 Facts 是否已成功归档（修复之前的丢失 Bug）：
- [ ] `context/input_facts.md`

## 最终报告

### Pass (通过)
如果所有文件存在：
```
[SUCCESS - Quality Gate Passed]
🎉 逆向工程圆满完成！

📍 产出位置: specs/10_reality/reverse_{slug}/
✅ 核心文件: 完整 (Indexes, Req, Design)
✅ 上下文归档: 完整 (input_facts.md)

您可以随时开始下一个功能逆向。
```

### Fail (失败)
如果有文件缺失：
```
[WARNING - Archival Incomplete]
⚠️ 检测到部分文件丢失！

缺失项:
- {Missing File Name}

建议: 请检查 maglev-spec-crystallize 是否执行成功。
```
