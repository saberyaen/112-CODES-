n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is undefined for negative integers")
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print("Factorial:", result)
