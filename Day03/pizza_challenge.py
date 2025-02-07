from numpy.core.defchararray import upper

print("Welcome to Python Pizza Deliveries!")
size = upper(input("What size pizza do you want? S, M or L: "))
while size != "S" and size != "M" and size != "L":
    print("Wrong option, try again!")
    size = upper(input("What size pizza do you want? S, M or L: "))
pepperoni = upper(input("Do you want pepperoni in your pizza? Y or N:"))
while pepperoni != "Y" and pepperoni != "N":
    print("Wrong option, try again!")
    pepperoni = upper(input("Do you want pepperoni in your pizza? Y or N:"))
extra_cheese = upper(input("Do you want extra cheese in your pizza? Y or N: "))
while extra_cheese != "Y" and extra_cheese != "N":
    print("Wrong option, try again!")
    extra_cheese = upper(input("Do you want extra cheese in your pizza? Y or N: "))
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is $ {bill}.")