import random

words = ["coffee", "friendship", "happiness", "courage", "nature", "hope", "travel", "love", "smile", "sun",
         "rain", "mountain", "sea", "moon", "star", "beach", "book", "time", "dream", "forest"]

chosen_word = random.choice(words)
secret = []
for i in range(len(chosen_word)):
    secret.append("_")
total_found = 0
life = 5

while ''.join(str(l) for l in secret) != chosen_word and life > 0:
    while True:
        print(secret)
        # print(choosen_word)
        letter = input("Choose a letter: ")
        if len(letter) == 1:
            letters_found = 0
            for i in range(len(chosen_word)):
                if letter.lower == chosen_word[i]:
                    secret[i] = letter
                    letters_found += 1
                    total_found += 1
            if total_found == 0:
                life -= 1
                print(f"Lifes: {life}")

            print(f"You have found {letters_found} letters! ")
            print()
            print()
            break
    if ''.join(str(l) for l in secret) == chosen_word:
        print("Congrats, you found the secret word, thanks for playing! ")
        print(f"The chosen word is {chosen_word}")
    elif life == 0:
        print("You died, try again another time, but thanks for playing anyway! ")
        print(f"The chosen word is {chosen_word}")