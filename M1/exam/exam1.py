"""Shopping cart management module."""


class ShoppingCart:
    """A shopping cart for managing customer items."""

    def __init__(self, customer_name, items=None):
        self.customer_name = customer_name
        self.items = [] if items is None else items

    def add_item(self, price):
        """Add an item to the cart."""
        try:
            if price <= 0:
                raise ValueError("Item price must be a positive number")
            self.items.append(price)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")       

    def remove_item(self, price):
        """Remove an item from the cart."""
        try:
            if price not in self.items:
                raise ValueError("Item not found in cart")
            self.items.remove(price)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")       

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = 0
        for price in self.items:
            total += price
        return round(total, 2)

    def apply_discount(self):
        """Apply a discount to the total price."""
        total = self.calculate_total()
        if total < 3000:
            return total
        else:
            discount = total * 0.1
            total -= discount
        return round(total)

    def display_cart(self):
        """Display the contents of the cart."""
        print(f"Customer: {self.customer_name}")
        print(f"Items in cart: {len(self.items)}")
        for price in self.items:
            print(f"- ${price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print(f"Final amount after discount: ${self.apply_discount()}")

    def clear_cart(self):
        """Clear all items from the cart."""
        self.items.clear()
        print("Cart has been cleared.")


cart = ShoppingCart('Tarek')
cart.add_item(1000.67)
cart.add_item(2000)
cart.remove_item(1000)
cart.add_item(3000)
cart.display_cart()


cart2 = ShoppingCart('Monjurul')
cart2.add_item(500)
cart2.add_item(0)
cart2.display_cart()
cart2.clear_cart()
