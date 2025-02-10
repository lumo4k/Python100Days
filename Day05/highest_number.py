import random

scores = [random.randint(1, 200) for n in range(30)]

max_number = 0
for score in scores:
    if score > max_number:
        max_number = score

print(f"This is the highest number: {max_number}")