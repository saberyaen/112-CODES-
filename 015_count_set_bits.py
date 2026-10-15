n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer")
else:
    print("Number of set bits:", bin(n).count("1"))
