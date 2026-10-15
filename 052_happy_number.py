def digit_square_sum(n):
    return sum(int(d) ** 2 for d in str(n))

n = int(input("Enter a positive integer: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = digit_square_sum(n)
print("Happy number" if n == 1 else "Not a happy number")
