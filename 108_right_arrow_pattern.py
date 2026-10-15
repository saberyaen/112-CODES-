n = int(input("Enter size: "))
for i in range(1, n + 1):
    print("*" + " " * max(1, n - 1) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" + " " * max(1, n - 1) + "*" * i)
