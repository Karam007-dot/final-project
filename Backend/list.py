print("Welcome to Karam's Shop")

items = {
    1: ("Air Filter", 32.5),
    2: ("Spark Plug", 12.99),
    3: ("Transmission Oil", 45.0),
    4: ("Engine Oil", 28.75)
}

purchases = []   # store purchased item prices

while True:
    start = input("Do you want to buy an item? (yes or no): ").strip().lower()

    if start == "no":
        print("\nThank you for shopping!")
        
        if purchases:
            print("\n----- Receipt -----")
            total = sum(purchases)
            print(f"Total (with VAT): {total:.2f} SR")
        else:
            print("You didn't purchase anything.")

        print("Goodbye!")
        break

    elif start != "yes":
        print("Please type 'yes' or 'no'.")
        continue

    print("\nAvailable items:")
    for num, (name, _) in items.items():
        print(f"{num}. {name}")

    choice = int(input("Choose an item (1-4): "))

    if choice in items:
        item_name, base_price = items[choice]
        vat_price = base_price * 1.15
        purchases.append(vat_price)
        
        print(f"\nYou chose: {item_name}")
        print(f"Price including 15% VAT: {vat_price:.2f} SR")

    else:
        print("Invalid choice. Please choose between 1 and 4.")
