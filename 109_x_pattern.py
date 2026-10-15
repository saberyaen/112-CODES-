n = int(input("Enter odd size (e.g. 5): "))
for i in range(n):
    row = [" "] * n
    row[i] = "*"
    row[n - 1 - i] = "*"
    print("".join(row))
