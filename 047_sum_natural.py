n = int(input("Enter N: "))
if n < 0:
    print("Enter a non-negative integer")
else:
    print("Sum:", n * (n + 1) // 2)
