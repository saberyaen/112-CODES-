n = int(input("Enter square size (at least 2): "))
for i in range(n):
    row = []
    for j in range(n):
        row.append("*" if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 else " ")
    print("".join(row))
