---
description: maglev-code-review Step 1 - Load Context
---

# Step 1: Load Context (加载上下文)

## 目标
加载待审查的代码变更和关联的 Spec 文件，建立审查基线。

## 执行逻辑

### 1.1 识别代码变更
根据输入方式，获取代码内容：

**单文件模式**:
```bash
# 读取整个文件
cat src/OrderController.java
```

**Git Diff 模式**:
```bash
# 获取变更行
git diff HEAD~1 -- src/OrderController.java
```

### 1.2 关联 Spec 匹配
尝试自动匹配关联的 Spec：

**匹配策略**:
1. 检查文件头部注释中的 Spec 引用
2. 根据文件名/路径推断 (e.g., `OrderController` → `reverse_order_management`)
3. 检查 `specs/README.md` 索引

**匹配结果**:
```yaml
spec_context:
  path: specs/10_reality/reverse_order_management/02_design.md
  apis:
    - GET /api/orders
    - POST /api/orders
    - DELETE /api/orders/{id}
  entities:
    - Order
    - OrderItem
```

### 1.3 提取审查范围
从代码变更中识别：
- 修改的方法/函数
- 涉及的 API 端点
- 涉及的数据模型

```yaml
review_scope:
  file: src/OrderController.java
  methods_changed:
    - getOrders (L25-L40)
    - createOrder (L45-L70)
    - deleteOrder (L75-L90)
  apis_touched:
    - GET /api/orders
    - POST /api/orders
    - DELETE /api/orders/{id}
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 1 Complete]

上下文已加载。

📁 代码变更:
- 文件: src/OrderController.java
- 变更行: +45 / -12
- 方法: getOrders, createOrder, deleteOrder

📋 关联 Spec:
- 路径: specs/10_reality/reverse_order_management/02_design.md
- APIs: GET /api/orders, POST /api/orders, DELETE /api/orders/{id}
- Entities: Order, OrderItem

是否继续检查合规性？[Y/n]
```

## 失败处理
- **未找到 Spec**: 提示用户手动指定 `--spec` 参数
- **Spec 过时**: 警告 Spec 版本可能与代码不同步
