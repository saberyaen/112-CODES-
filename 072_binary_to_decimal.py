binary = input("Enter a binary number: ").strip()
if binary and all(ch in "01" for ch in binary):
    print("Decimal:", int(binary, 2))
else:
    print("Invalid binary number")
