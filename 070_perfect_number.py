n = int(input("Enter a positive integer: "))
divisor_sum = sum(i for i in range(1, n) if n > 0 and n % i == 0)
print("Perfect number" if n > 0 and divisor_sum == n else "Not a perfect number")
