n = int(input("Enter N: "))
if n <= 0:
    print("N must be positive")
else:
    total = sum(1 / i for i in range(1, n + 1))
    print("Sum:", total)
