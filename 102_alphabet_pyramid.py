n = int(input("Enter number of rows (1-13): "))
for i in range(1, min(n, 13) + 1):
    left = "".join(chr(64 + j) for j in range(1, i + 1))
    right = "".join(chr(64 + j) for j in range(i - 1, 0, -1))
    print(" " * (n - i) + left + right)
