import random

from numpy.core.defchararray import isdigit


def random_number_int():
    while True:
        number_random = random.randint(1, 3)
        print(number_random)
        if number_random == 1:
            break

def tentativas_contagem():
    y = 0
    counter = 0
    while y < 5:
        y_number = random.randint(1, 5)
        if y_number == y + 1:
            print(f"--> Tentativas: {counter}")
            y = y_number
            counter = 0
            print(f"Conseguimos somar -> {y}")
        else:
            counter += 1

def random_random():
    n = round(random.random() * 10)
    counter = 0
    while n != 0:
        counter += 1
        n = round(random.random() * 10)
        if n == 0:
            print(counter)
            print(n)
            break

def head_tail():
    coin_number = random.randint(0,1)
    if coin_number == 0:
        print("Heads")
    elif coin_number == 1:
        print("Tails")

def friends_roulette():
    friends  = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    print(random.choice(friends))

def rock_paper_scissors():
    while True:
        player_selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
        if isdigit(player_selection):
            player_selection = int(player_selection)

        if player_selection in range(0,3):
            break

    computer_random_selection =  random.randint(0,2)
    print(f"Computer chooses {computer_random_selection}")
    if player_selection == computer_random_selection:
        print("Draw!")
    elif player_selection == 0 and computer_random_selection == 2:
        print("You win, congrats!")
    elif computer_random_selection == 0 and player_selection == 2:
        print("Computer wins!")
    elif player_selection > computer_random_selection:
        print("You win, congrats!")
    elif computer_random_selection > player_selection:
        print("Computer wins!")
