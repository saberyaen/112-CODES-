n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("".join(str((i + j) % 2) for j in range(1, i + 1)))
