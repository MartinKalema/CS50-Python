amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    inserted_amount = int(input("Insert Coin: "))

    if inserted_amount  == 10 or inserted_amount == 25 or inserted_amount == 5:
        amount_due -= inserted_amount

    if amount_due <= 0:
        print("Change Owed:", abs(amount_due))