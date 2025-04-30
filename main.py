from restaurant import Restaurant

def main():
    restaurant = Restaurant()
    admin = restaurant.admin

    # Admin manages menu
    admin.manage_menu(restaurant.menu)

    # Admin adds a customer
    admin.add_customer("John Doe", "john@example.com", "123 Main St")

    # Customer operations
    customer = admin.customers["john@example.com"]
    customer.view_menu(restaurant.menu)
    customer.add_funds(50)
    customer.place_order(restaurant.menu, ["Burger", "Fries"])
    customer.view_past_orders()
    customer.check_balance()

if __name__ == "__main__":
    main()
