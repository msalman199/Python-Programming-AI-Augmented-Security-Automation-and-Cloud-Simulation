import pytest
from decimal import Decimal
from src.order_system.models import Product, OrderItem, Order

class TestProduct:
    """Unit tests for Product model"""
    
    def test_product_creation(self):
        """Test product instantiation with valid data"""
        # TODO: Create a product instance
        # TODO: Assert all attributes are set correctly
        # TODO: Use specific assertion messages for clarity
        pass
    
    def test_product_price_type(self):
        """Test that price is stored as Decimal"""
        # TODO: Create product with Decimal price
        # TODO: Assert price type is Decimal
        # TODO: Assert price value is exact
        pass

class TestOrderItem:
    """Unit tests for OrderItem model"""
    
    @pytest.fixture
    def sample_product(self):
        """Fixture providing a sample product"""
        return Product(
            id="P001",
            name="Test Product",
            price=Decimal('29.99'),
            stock=100
        )
    
    def test_order_item_subtotal(self, sample_product):
        """Test subtotal calculation for order item"""
        # TODO: Create OrderItem with quantity 3
        # TODO: Calculate expected subtotal
        # TODO: Assert calculated subtotal matches expected
        # TODO: Use descriptive assertion message
        pass
    
    def test_order_item_subtotal_single_quantity(self, sample_product):
        """Test subtotal with quantity of 1"""
        # TODO: Create OrderItem with quantity 1
        # TODO: Assert subtotal equals product price
        pass

class TestOrder:
    """Unit tests for Order model"""
    
    @pytest.fixture
    def sample_order_items(self):
        """Fixture providing sample order items"""
        # TODO: Create 2-3 sample products
        # TODO: Create OrderItems from products
        # TODO: Return list of OrderItems
        pass
    
    def test_order_total_no_discount(self, sample_order_items):
        """Test order total calculation without discount"""
        # TODO: Create order with items, no discount
        # TODO: Calculate expected total manually
        # TODO: Assert order.calculate_total() matches expected
        pass
    
    def test_order_total_with_discount(self, sample_order_items):
        """Test order total with discount applied"""
        # TODO: Create order with 10% discount
        # TODO: Calculate expected total with discount
        # TODO: Assert calculated total is correct
        # TODO: Verify discount was applied properly
        pass
    
    def test_order_empty_items(self):
        """Test order with no items"""
        # TODO: Create order with empty items list
        # TODO: Assert total is zero
        pass
