print("========== BILL GENERATOR ==========")

items = []
total = 0

print("Available items:")
print("1. Rice       - Rs.40/kg")
print("2. Wheat      - Rs.35/kg")
print("3. Sugar      - Rs.50/kg")
print("4. Oil        - Rs.120/liter")
print("5. Milk       - Rs.56/liter")
print("6. Eggs       - Rs.6/piece")

prices = {
    1: ("Rice", 40),
    2: ("Wheat", 35),
    3: ("Sugar", 50),
    4: ("Oil", 120),
    5: ("Milk", 56),
    6: ("Eggs", 6),
}

def read_item_number():
    while True:
        try:
            item_no = int(input("\nEnter item number (1-6, 0 to finish): "))
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue
        if item_no in prices or item_no == 0:
            return item_no
        print("Invalid item! Choose a number from 1 to 6, or 0 to finish.")


def read_quantity(item_name):
    while True:
        try:
            quantity = float(input(f"Enter quantity for {item_name}: "))
        except ValueError:
            print("Invalid quantity! Enter a number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        return quantity


while True:
    item_no = read_item_number()
    if item_no == 0:
        break
    qty = read_quantity(prices[item_no][0])
    price = prices[item_no][1] * qty
    items.append((prices[item_no][0], qty, prices[item_no][1], price))
    total += price
    print(f"Added: {prices[item_no][0]} x {qty} = Rs.{price}")

print("\n" + "=" * 50)
print("              BILL RECEIPT")
print("=" * 50)
print(f"{'Item':<12} {'Qty':<8} {'Rate':<10} {'Amount':<10}")
print("-" * 50)

for item in items:
    print(f"{item[0]:<12} {item[1]:<8} Rs.{item[2]:<8} Rs.{item[3]:<8}")

print("-" * 50)
print(f"{'TOTAL':>30} Rs.{total}")
print("=" * 50)
print("Thank you for shopping!")
