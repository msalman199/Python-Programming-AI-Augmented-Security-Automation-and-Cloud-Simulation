from typing import Dict, Optional
from .models import Product

class InventoryManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:
        """Add a product to inventory"""
        # TODO: Add product to products dictionary
        pass
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID"""
        # TODO: Return product if exists, None otherwise
        pass
    
    def check_availability(self, product_id: str, quantity: int) -> bool:
        """Check if requested quantity is available"""
        # TODO: Verify product exists
        # TODO: Check if stock >= quantity
        pass
    
    def reduce_stock(self, product_id: str, quantity: int) -> bool:
        """Reduce stock after order placement"""
        # TODO: Verify availability first
        # TODO: Reduce stock if available
        # TODO: Return success status
        pass
