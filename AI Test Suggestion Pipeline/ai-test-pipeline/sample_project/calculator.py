def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide two numbers with error handling."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_discount(price, discount_percent):
    """Calculate discounted price with validation."""
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid input")
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount
