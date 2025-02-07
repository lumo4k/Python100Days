import sys

from numpy.core.defchararray import upper

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island! \nYour Mission is to find the Treasure.")

while True:
    path = upper(input("Do you want to go to the Left or Right? \n"))
    if path == "RIGHT" or path == "LEFT":
        break

if path == "RIGHT":
    print("You fall into a lake with Piranhas, you died!")
    sys.exit()
elif path == "LEFT":
    print("You run to the path in the left, and after minutes, on your left you have a cave, and on your right, "
          "you can follow the road that you have been following.")

while True:
    path = upper(input("Do you want to go to the Left or Right? \n"))
    if path == "RIGHT" or path == "LEFT":
        break

if path == "LEFT":
    print("You entered in a troll cave and after he chases and catch you, you died! ")
    sys.exit()
elif path == "RIGHT":
    print("Walking some time on the road, you found a wizard, who offers you three doors to enter "
          "Red, blue and yellow, which one you choose: ")

while True:
    path = upper(input("Which door do you choose? \n"))
    if path == "YELLOW" or path == "BLUE" or path == "RED":
        break

if path == "RED":
    print("You fall into the lava realm and burn to death, you died! ")
elif path == "BLUE":
    print("After entering into the blue door, you see yourself melting, after that you realise that you "
          "become a slime, you don't die, but you are a slime now!")
elif path == "YELLOW":
    print("You win, congratulations, just sit here for a moment and enjoy! ")
