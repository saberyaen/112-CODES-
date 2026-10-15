units = float(input("Enter electricity units used: "))
if units < 0:
    print("Invalid units")
else:
    # Example slab rates; replace with your course's specified rates if given.
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Electricity bill:", round(bill, 2))
