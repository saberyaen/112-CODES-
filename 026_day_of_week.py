days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}
n = int(input("Enter day number (1-7): "))
print(days.get(n, "Invalid day number"))
