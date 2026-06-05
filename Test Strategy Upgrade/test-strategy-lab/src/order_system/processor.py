from typing import List, Tuple
from .models import Order, OrderItem, Product
from .inventory import InventoryManager

class OrderProcessor:
    def __init__(self, inventory_manager: InventoryManager):
        self.inventory = inventory_manager
        self.processed_orders: List[Order] = []
    
    def validate_order(self, order: Order) -> Tuple[bool, str]:
        """
        Validate order items against inventory
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        # TODO: Check if order has items
        # TODO: Validate each item's availability
        # TODO: Return (True, "") if valid, (False, error_msg) otherwise
        pass
    
    def process_order(self, order: Order) -> Tuple[bool, str]:
        """
        Process an order: validate and update inventory
        
        Returns:
            Tuple of (success, message)
        """
        # TODO: Validate order first
        # TODO: Reduce stock for each item
        # TODO: Add to processed_orders if successful
        # TODO: Return appropriate status and message
        pass
