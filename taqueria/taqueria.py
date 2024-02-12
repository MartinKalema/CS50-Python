total = 0 

items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

def main():
    try:
        add_item()
    except EOFError: # End of File error (CTRL +)
        print()

def add_item():
    global total
    global items
    item = input("Item: ").strip().lower()
    items = {key.lower(): value for key, value in items.items()}
    
    if item in items.keys():
        total += items.get(item)
        print(f"Total: ${total:.2f}")
        add_item()
    else:
        add_item()
        


main()
