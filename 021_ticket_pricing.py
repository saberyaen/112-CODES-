age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: 0")
elif age <= 12:
    print("Ticket price: 50")
elif age >= 60:
    print("Ticket price: 80")
else:
    print("Ticket price: 100")
# Example pricing; adjust rates if your faculty specifies different slabs.
