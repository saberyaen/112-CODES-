import math
x = float(input("Enter x in radians: "))
terms = int(input("Number of terms: "))
total = 0.0
for k in range(max(0, terms)):
    power = 2 * k + 1
    term = x ** power / math.factorial(power)
    total += term if k % 2 == 0 else -term
print("Approximate sin(x):", total)
