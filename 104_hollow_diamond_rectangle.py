n = int(input("Enter size: "))
for i in range(n):
    left = "*" * (i + 1)
    right = "*" * (n - i)
    gap = " " * max(1, 2 * (n - i) - 1)
    print(left + gap + right)
for i in range(n - 2, -1, -1):
    left = "*" * (i + 1)
    right = "*" * (n - i)
    gap = " " * max(1, 2 * (n - i) - 1)
    print(left + gap + right)
