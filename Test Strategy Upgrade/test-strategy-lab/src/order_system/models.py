from dataclasses import dataclass
from typing import List
from decimal import Decimal

@dataclass
class Product:
    id: str
    name: str
    price: Decimal
    stock: int

@dataclass
class OrderItem:
    product: Product
    quantity: int
    
    def get_subtotal(self) -> Decimal:
        """Calculate subtotal for this order item"""
        # TODO: Implement subtotal calculation
        pass

@dataclass
class Order:
    order_id: str
    items: List[OrderItem]
    discount_percent: Decimal = Decimal('0')
    
    def calculate_total(self) -> Decimal:
        """Calculate order total with discount applied"""
        # TODO: Calculate sum of all item subtotals
        # TODO: Apply discount percentage
        # TODO: Return final total
        pass
