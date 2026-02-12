---
description: maglev-plan-unit-tests-backend Step 4 - Generate Test Skeleton
---

# Step 4: Generate Test Skeleton (生成测试骨架)

## 目标
输出可执行的测试代码框架，开发者只需填充具体逻辑。

## 输出路径
根据项目结构自动确定：
- Java: `src/test/java/{package}/{TestClass}.java`
- Python: `tests/test_{module}.py`
- Go: `{package}/{file}_test.go`
- Node: `__tests__/{module}.test.ts`

## Java 模板 (JUnit 5 + Mockito)

```java
package com.example.order;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class OrderServiceTest {

    @Mock
    private OrderRepository orderRepository;
    
    @Mock
    private InventoryClient inventoryClient;
    
    @InjectMocks
    private OrderService orderService;
    
    // ===== calculateTotalAmount =====
    
    @Nested
    @DisplayName("calculateTotalAmount")
    class CalculateTotalAmountTests {
        
        @Test
        @DisplayName("正常情况 - 多商品累加")
        void testCalculateTotalAmount_Normal() {
            // Given
            // TODO: Setup test data
            
            // When
            // TODO: Call method
            
            // Then
            // TODO: Assert result
        }
        
        @Test
        @DisplayName("边缘情况 - 空订单返回零")
        void testCalculateTotalAmount_EmptyOrder() {
            // TODO: Implement
        }
    }
    
    // ===== checkStock =====
    
    @Nested
    @DisplayName("checkStock")
    class CheckStockTests {
        
        @Test
        @DisplayName("库存充足 - 返回 true")
        void testCheckStock_Sufficient() {
            // Given
            when(inventoryClient.getStock("SKU-001")).thenReturn(100);
            
            // When
            boolean result = orderService.checkStock("SKU-001", 10);
            
            // Then
            assertThat(result).isTrue();
        }
        
        @Test
        @DisplayName("库存不足 - 抛异常")
        void testCheckStock_Insufficient() {
            // Given
            when(inventoryClient.getStock("SKU-001")).thenReturn(5);
            
            // When & Then
            assertThatThrownBy(() -> orderService.checkStock("SKU-001", 10))
                .isInstanceOf(InsufficientStockException.class);
        }
    }
}
```

## Python 模板 (pytest)

```python
import pytest
from unittest.mock import Mock, patch

class TestOrderService:
    
    @pytest.fixture
    def order_service(self):
        repo = Mock()
        client = Mock()
        return OrderService(repo, client)
    
    # ===== calculate_total_amount =====
    
    def test_calculate_total_amount_normal(self, order_service):
        """正常情况 - 多商品累加"""
        # Given
        # TODO: Setup
        
        # When
        # TODO: Call
        
        # Then
        # TODO: Assert
        pass
    
    # ===== check_stock =====
    
    def test_check_stock_sufficient(self, order_service):
        """库存充足 - 返回 True"""
        order_service.inventory_client.get_stock.return_value = 100
        
        result = order_service.check_stock("SKU-001", 10)
        
        assert result is True
```

## 最终输出模板
```
[Step 4 Complete]

✅ 测试骨架已生成！

📁 输出文件:
- src/test/java/com/example/order/OrderControllerTest.java
- src/test/java/com/example/order/OrderServiceTest.java
- src/test/java/com/example/order/OrderRepositoryTest.java

📊 统计:
- 测试类: 3 个
- 测试方法: 24 个
- 已填充示例: 4 个
- 待实现 (TODO): 20 个

下一步:
1. 填充 TODO 部分的测试逻辑
2. 运行测试验证
3. 使用 maglev-cross-validate 检查覆盖率
```
