cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit:", round(sp - cp, 2))
elif sp < cp:
    print("Loss:", round(cp - sp, 2))
else:
    print("No profit, no loss")
