hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))
if hours < 0 or rate < 0:
    print("Invalid input")
else:
    salary = min(hours, 40) * rate + max(0, hours - 40) * rate * 1.5
    print("Salary:", round(salary, 2))
