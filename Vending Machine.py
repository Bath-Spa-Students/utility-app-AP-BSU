# Start program 
# dictionary of item inventory hides items unavailable in stock and tracks inventory while running
def vending():
    a = {"item": "Arwa", "rate": 1.70, "available stock": 2}
    b = {"item": "Aquafina", "rate": 2, "available stock": 4}
    c = {"item": "Lipton", "rate": 3.50, "available stock": 69}
    d = {"item": "Fiji", "rate": 6, "available stock": 3}
    e = {"item": "Evian", "rate": 5.30, "available stock": 1}
    items = [a, b, c, d, e]
    money = 0  # money in machine
    print("Welcome to the Waterfalling machine")  # first interface display upon powered on

    # Interface showing item info and updating available stock
    def show(items):
        print("\nItems available:")
        for item in items:
            if item["available stock"] > 0:
                print(f"{item['item']} - AED {item['rate']}")
        print("\n")  # separator

    # User input to choose item
    while True:
        show(items)
        user_selection = input("Select item: ")
        selected_item = next((item for item in items if user_selection.lower() == item["item"].lower()), None)

# Shows the user input to insert amount depending on item price
        if selected_item:
            rate = selected_item["rate"]
            while money < rate:
                try:
                    money += float(input(f"Insert AED {rate - money}: "))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue

# Upon successful transaction selected item will be deducted if reduced to 0 it will now be hidden to item selection
            selected_item["available stock"] -= 1
            money -= rate
            print(f"{selected_item['item']} purchased. Cash remaining: ${money}")

# Request the user to continue to order again or end program
            order_again = input("Order again? (t/f): ").lower()
            if order_again == "f":
                if money != 0:
                    print(f"Remaining amount refunded: AED{money}") # 13 float decimals are defaultly added
                    money = 0
                print("Transactions Completed (End of program)")
                break  # Exit the loop if the user type "n"
            else:
                continue # Continues the loop if user types "t" or else
vending()
