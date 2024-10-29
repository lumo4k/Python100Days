height = float(input("What is your height in cm? "))

if height > 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"${bill} is added to your bill for the ride! ")
    elif 12 < age < 18:
        bill = 7
        print(f"${bill} is added to your bill for the ride! ")
    else:
        bill = 12
        print(f"${bill} is added to your bill for the ride! ")

    wants_photos = input("Do you want photos from your ride for $3? Type y to Yes and n to No: ")
    if wants_photos == 'y':
        bill += 3
        print("Here, pick up your photos after pay the bill")
    else:
        print("It`s ok, just pay your bill here.")

    print(f"Your final bill is {bill}")
else:
    print("You can`t ride the Rollercoaster!")