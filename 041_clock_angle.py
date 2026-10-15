hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minute (0-59): "))
if not 1 <= hour <= 12 or not 0 <= minute <= 59:
    print("Invalid time")
else:
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    print("Smaller angle:", min(angle, 360 - angle))
