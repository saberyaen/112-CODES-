marks = float(input("Marks percentage: "))
attendance = float(input("Attendance percentage: "))
income = float(input("Annual family income: "))
# Example criteria; change them if your faculty gives specific thresholds.
if marks >= 85 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
