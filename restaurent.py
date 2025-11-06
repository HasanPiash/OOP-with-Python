from admin import Admin

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.admin = Admin()

    def show_menu(self):
        print("Restaurant Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def add_menu_item(self, item, price):
        self.menu[item] = price
        print(f"Item {item} added with price ${price}.")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Item {item} removed from the menu.")
        else:
            print("Item not found in the menu.")

    def check_customer_details(self, email):
        if email in self.admin.customers:
            customer = self.admin.customers[email]
            print(f"Customer Details:")
            print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")
        else:
            print("Customer not found.")

 
