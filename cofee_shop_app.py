class CoffeeShop:
    def __init__(self):
        # Encapsulated fields
        self._coffee_price = 0.0
        self._sandwich_price = 0.0

    # Properties for field access
    @property
    def coffee_price(self):
        return self._coffee_price

    @property
    def sandwich_price(self):
        return self._sandwich_price

    # Update Menu
    def update_menu(self, coffee_price, sandwich_price):
        self._coffee_price = coffee_price
        self._sandwich_price = sandwich_price
        print(f"Menu updated: Coffee Price = {coffee_price}, Sandwich Price = {sandwich_price}")

    # Process Order
    def process_order(self, order):
        total = 0
        if order.wants_coffee:
            total += self.coffee_price
        if order.wants_sandwich:
            total += self.sandwich_price

        print(f"Order processed for {order.customer_name}")
        print(f"Total amount to pay: {total}")
        self.process_payment(total)

    # Process Payment
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")


class Order:
    def __init__(self, customer_name, wants_coffee, wants_sandwich):
        self.customer_name = customer_name
        self.wants_coffee = wants_coffee
        self.wants_sandwich = wants_sandwich


if __name__ == "__main__":
    # Initialize CoffeeShop and Update Menu
    coffee_shop = CoffeeShop()
    coffee_shop.update_menu(5.0, 8.5)

    # Create an order and process it
    order = Order("Rehan", wants_coffee=True, wants_sandwich=True)
    coffee_shop.process_order(order)
