import random
import hang_name
import art
from replit import clear

print("Welcome to ")
print(art.logo)
print("\n")

live = 6
r = random.choice(hang_name.word_list)
l = int(len(r))
print("\nThe word is\n")
blank = []
for _ in range(l):
    blank += "_"
print(f"{' '.join(blank)}\n\n")
end = False
used = []

while end == False:
    print(
        "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
    )
    print(f"Already used letters: {used}\n\n")
    c = input("Guess a letter:  ")

    guess = c.lower()
    clear()
    flag = 0
    f = 1
    lu = len(used)

    for i in range(lu):
        if guess == used[i]:
            f = 0

    if f == 1:
        used.append(guess)
        for x in range(l):
            if guess == r[x]:
                print("\nNice guess\n")
                blank[x] = guess
                flag = 1
        if flag == 0:
            print(
                f"\nYou guessed {c}\nThats not a letter in the word\nYou loose a live\n"
            )
            live = live - 1

    elif f == 0:
        print("\nYou guessed it already\nTry a new letter\n")
    print(f"{art.stages[live]}\n")
    print(f"{' '.join(blank)}\n")

    if "_" not in blank:
        end = True
        print(
            "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
        )
        print("You won")
        print(
            "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
        )

    if live == 0:
        end = True
        print(
            "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
        )
        print("You lose")
        print(f"The word was {r}")
        print(
            "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
        )


    
