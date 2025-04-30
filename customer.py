class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.past_orders = []

    def view_menu(self, menu):
        print("Restaurant Menu:")
        for item, price in menu.items():
            print(f"{item}: ${price}")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def add_funds(self, amount):
        self.balance += amount
        print(f"${amount} added to your balance. New balance: ${self.balance}")

    def place_order(self, menu, order_items):
        total_cost = sum(menu[item] for item in order_items if item in menu)
        if total_cost > self.balance:
            print("Insufficient balance. Please add funds.")
        else:
            self.balance -= total_cost
            self.past_orders.append(order_items)
            print(f"Order placed successfully! Total cost: ${total_cost}. Remaining balance: ${self.balance}")

    def view_past_orders(self):
        print("Past Orders:")
        for order in self.past_orders:
            print(order)
