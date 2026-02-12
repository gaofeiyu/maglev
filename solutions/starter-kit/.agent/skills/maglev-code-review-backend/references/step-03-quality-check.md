---
description: maglev-code-review Step 3 - Quality Check
---

# Step 3: Quality Check (质量检查)

## 目标
检查代码质量和最佳实践，独立于 Spec 合规性。

## 检查维度

### 3.1 命名规范
| 检查项 | 标准 |
|--------|------|
| 变量命名 | 驼峰命名，含义清晰 |
| 方法命名 | 动词开头，描述行为 |
| 常量命名 | 全大写 + 下划线 |
| 类命名 | 大驼峰，名词 |

### 3.2 错误处理
| 检查项 | 标准 |
|--------|------|
| 异常捕获 | 不使用空 catch |
| 异常类型 | 使用具体异常类型，非 Exception |
| 错误消息 | 包含上下文信息 |
| 资源关闭 | 使用 try-with-resources |

### 3.3 边界条件
| 检查项 | 标准 |
|--------|------|
| 空值检查 | 处理 null 参数 |
| 集合为空 | 处理空 List/Map |
| 数值边界 | 处理 0、负数、溢出 |
| 字符串 | 处理空字符串、超长字符串 |

### 3.4 代码复杂度
| 检查项 | 阈值 |
|--------|------|
| 方法行数 | ≤ 30 行 |
| 参数个数 | ≤ 5 个 |
| 嵌套深度 | ≤ 3 层 |
| 圈复杂度 | ≤ 10 |

### 3.5 安全性
| 检查项 | 风险 |
|--------|------|
| SQL 拼接 | SQL 注入 |
| HTML 输出 | XSS |
| 文件路径 | 路径遍历 |
| 敏感信息 | 日志泄露 |

## 检查逻辑示例
```python
def check_error_handling(method):
    issues = []
    
    # 检查空 catch
    if has_empty_catch(method):
        issues.append({
            "type": "ERROR_HANDLING",
            "severity": "WARNING",
            "message": "存在空 catch 块",
            "line": get_catch_line(method)
        })
    
    # 检查未处理的异常
    for external_call in get_external_calls(method):
        if not is_wrapped_in_try(external_call):
            issues.append({
                "type": "ERROR_HANDLING",
                "severity": "WARNING",
                "message": f"{external_call} 可能抛出异常但未处理"
            })
    
    return issues
```

## Checkpoint 输出模板
```
[CHECKPOINT - Step 3 Complete]

质量检查完成。

📊 结果:
- 命名规范: ✅ 良好
- 错误处理: ⚠️ 2 个问题
- 边界条件: ⚠️ 1 个问题
- 代码复杂度: ✅ 良好
- 安全性: ✅ 未发现风险

⚠️ 问题 (3 个):
- [ERROR_HANDLING] deleteOrder():L90 - 缺少异常捕获
- [ERROR_HANDLING] updateOrder():L110 - 空 catch 块
- [BOUNDARY] getOrders():L30 - page 参数未校验负数

是否生成 Review 意见？[Y/n]
```
