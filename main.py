gd_word = []
run = True
life = 0
man = {0: "",
       1: "|\n",
       2: "|\n|\n",
       3: "|\n|\n|\n",
       4: "|\n|\n|\n|\n",
       5: " ____\n|\n|\n|\n|\n",
       6: " ____\n|    |\n|\n|\n|\n",
       7: " ____\n|    |\n|    O\n|\n|\n",
       8: " ____\n|    |\n|    O\n|   /|\ \n|\n",
       9: " ____\n|    |\n|    O\n|   /|\ \n|   / \ \n"}

while run:
    word = input("Type a word that should be guessed: ").lower()
    print("\n" * 15)

    if word.isalpha():
        guessed = False
    elif not word.isalpha():
        print("Your word cannot contain numbers or spaces.")
        guessed = True

    h_word = ["_" for x in range(len(word))]

    while not guessed:
        print(man[life])
        print("".join(h_word) + "\n")
        print("Tested characters: " + ", ".join(gd_word) + "\n")

        g_word = input("Guess a character: ").lower()
        if len(g_word) == 1 and g_word.isalpha():

            if g_word in gd_word:
                print("You have already tested this character")

            elif g_word not in word and g_word not in gd_word:
                life += 1
                gd_word.append(g_word)


            elif g_word in word and g_word not in gd_word:
                gd_word.append(g_word)
                for c in gd_word:
                    if c in word:
                        indices = [i for i, val in enumerate(word) if val == c]
                        for i in indices:
                            h_word[i] = c

            if "".join(h_word) == word:
                guessed = True
                print("Congratulations you guessed the word:\n")
                print("".join(h_word) + "\n")
                again = input("Do you want to play again? y/n: ").lower()

                if again == "n":
                    run = False
                elif again == "y":
                    life = 0
                    gd_word = []
                    continue
                else:
                    guessed = False
                    print("You didn't type y or n")
            elif life == 9:
                guessed = True
                print(man[life])
                print("You did not guess the word...")
                print(word)
                again = input("Do you want to play again? y/n: ").lower()
                if again =="n":
                    run = False
                elif again == "y":
                    life = 0
                    gd_word = []
                    continue
                else:
                    guessed = False
                    print("You didn't type y or n")
            else:
                continue
        else:
            print("That is not a character")
