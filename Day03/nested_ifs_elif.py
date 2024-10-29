height = float(input("What is your height in cm? "))

if height > 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("You need to pay $5")
    elif 12 < age < 18:
        print("You need to pay $7")
    else:
        print("You need to pay $12")
else:
    print("You can`t ride the Rollercoaster!")