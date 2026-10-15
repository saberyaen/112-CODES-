import math
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("LCM:", 0 if a == 0 or b == 0 else abs(a * b) // math.gcd(a, b))
