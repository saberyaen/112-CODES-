import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Not a quadratic equation (a must not be zero)")
else:
    d = b*b - 4*a*c
    r1 = (-b + cmath.sqrt(d)) / (2*a)
    r2 = (-b - cmath.sqrt(d)) / (2*a)
    print("Roots:", r1, "and", r2)
