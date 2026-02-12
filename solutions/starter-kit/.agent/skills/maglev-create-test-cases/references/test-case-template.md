# 测试计划: {Title}

**源文档**: {Source Link}
**覆盖率**: {Coverage Summary}

## 1. 测试策略
| 模块 | 测试类型 | 工具/方法 |
| --- | --- | --- |
| Backend Service | Unit | JUnit + Mockito |
| API | Integration | Postman / RestAssured |

## 2. 测试用例列表

### 模块 A: {Module Name}

| ID | 优先级 | 标题 | 前置条件 | 步骤 | 预期结果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-001 | P0 | 正常创建 Feature | DB Empty | 1. Call API... | 200 OK, DB Inserted |
| TC-002 | P1 | 必填校验 | - | 1. Call API with null | 400 Bad Request |
