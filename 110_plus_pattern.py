n = int(input("Enter odd size (e.g. 5): "))
if n % 2 == 0:
    print("Please enter an odd size")
else:
    mid = n // 2
    for i in range(n):
        print("".join("*" if i == mid or j == mid else " " for j in range(n)))
