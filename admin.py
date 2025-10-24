from customer import Customer

class Admin:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, email, address):
        if email in self.customers:
            print("Customer with this email already exists.")
        else:
            self.customers[email] = Customer(name, email, address)
            print(f"Customer {name} added successfully.")

    def view_customers(self):
        print("Registered Customers:")
        for email, customer in self.customers.items():
            print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")

    def remove_customer(self, email):
        if email in self.customers:
            del self.customers[email]
            print("Customer removed successfully.")
        else:
            print("Customer not found.")

    
    def manage_menu(self, menu):
        while True:
            print("Menu Management Options:")
            print("1. Add item")
            print("2. Remove item")
            print("3. Update item price")
            print("4. View menu")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                item = input("Enter item name: ")
                price = float(input("Enter item price: "))
                menu[item] = price
                print(f"Item {item} added successfully.")
            elif choice == "2":
                item = input("Enter item name to remove: ")
                if item in menu:
                    del menu[item]
                    print(f"Item {item} removed successfully.")
                else:
                    print("Item not found.")
            elif choice == "3":
                item = input("Enter item name to update: ")
                if item in menu:
                    price = float(input("Enter new price: "))
                    menu[item] = price
                    print(f"Price of {item} updated to ${price}.")
                else:
                    print("Item not found.")
            elif choice == "4":
                for item, price in menu.items():
                    print(f"{item}: ${price}")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

