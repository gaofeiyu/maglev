---
description: maglev-create-test-cases Step 5 - Output
---

# Step 5: Output (输出)

## 目标
将生成的测试计划持久化到标准位置。

## 输出路径
```
specs/{feature}/03_test_plan.md
# 或
specs/{feature}/03_test_plan_frontend.md (如果是前端 Spec)
```

## 执行逻辑

### 5.1 文件生成
根据 Step 1-4 的结果，生成完整的 `03_test_plan.md`。

### 5.2 索引更新
调用 `maglev-librarian` 更新 `specs/README.md`，将新的测试计划注册在册。

### 5.3 与 cross-validate 协同
生成的 `03_test_plan.md` 可被 `maglev-cross-validate` 读取，进行 Spec ↔ Tests 一致性验证。

## 最终输出模板
```
[Step 5 Complete]

✅ 测试计划已输出！

📄 输出路径: specs/{feature}/03_test_plan.md

📊 测试统计:
- Unit Tests: 15 个
- Integration Tests: 8 个
- E2E Tests: 3 个
- AC 覆盖率: 100%

📚 索引已更新: specs/README.md

下一步建议:
1. 使用 IDE 生成测试代码框架
2. 实现测试逻辑
3. 运行 maglev-cross-validate 验证一致性
```
