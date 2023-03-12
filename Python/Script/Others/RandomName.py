import random

generate_time = 50
min_letter_num = 4
max_letter_num = 5

for i in range(generate_time):
    letter_num = random.randint(min_letter_num, max_letter_num)
    for j in range(letter_num):
        print(chr(random.randint(97, 122)), end="")
    print("")