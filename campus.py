class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodDeliveryApp:
    def __init__(self):
        self.menu = {
            1: FoodItem("Pizza", 12.99),
            2: FoodItem("Burger", 6.99),
            3: FoodItem("Pasta", 8.50),
            4: FoodItem("Salad", 5.99),
            5: FoodItem("Ice Cream", 3.99)
        }
        self.cart = []

    def display_menu(self):
        print("Menu:")
        for item_num, food_item in self.menu.items():
            print(f"{item_num}. {food_item.name} - ${food_item.price}")

    def add_to_cart(self, item_number):
        if item_number in self.menu:
            self.cart.append(self.menu[item_number])
            print(f"{self.menu[item_number].name} added to cart.")
        else:
            print("Invalid item number!")

    def view_cart(self):
        total_price = sum(item.price for item in self.cart)
        if self.cart:
            print("Cart:")
            for item in self.cart:
                print(f"- {item.name}: ${item.price}")
            print(f"Total: ${total_price}")
        else:
            print("Your cart is empty.")

    def place_order(self):
        if self.cart:
            total_price = sum(item.price for item in self.cart)
            print(f"Total amount to be paid: ${total_price}")
            print("Thank you for ordering!")
            self.cart = []
        else:
            print("Your cart is empty. Please add items before placing the order.")

# Sample usage
app = FoodDeliveryApp()

while True:
    print("\n1. Display Menu")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Place Order")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        app.display_menu()
    elif choice == '2':
        item_number = int(input("Enter the item number to add to cart: "))
        app.add_to_cart(item_number)
    elif choice == '3':
        app.view_cart()
    elif choice == '4':
        app.place_order()
    elif choice == '5':
        print("Thank you for using the Food Delivery App.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
