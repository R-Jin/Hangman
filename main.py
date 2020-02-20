


gd_char = []               # Storing the guessed character here

run = True                 # For the game loop

life = 0                   # Life counter increments every time a wrong word is guessed

man = {0: "",              # The hangmans different bodyparts printed out based on the life variable
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
    # Game loop

    word = input("Type a word that should be guessed: ").lower()        # word is used to check if the guessed characters are correct
    print("\n" * 30)                                                    # Hides the word that should be guessed


    # Check if it is a valid word
    if word.isalpha():

        # Starts the guessing loop
        guessed = False

    elif not word.isalpha():

        # Reprompt you to type a word that should be guessed
        print("Your word cannot contain numbers or spaces.")
        guessed = True

    h_word = ["_" for x in range(len(word))]                            # h_word is the word hidden with underscores updates when a correct character is guessed


    # The guessing loop
    while not guessed:

        print(man[life])

        print("".join(h_word) + "\n")                                   # Guessing progress (The hidden word)

        print("Tested characters: " + ", ".join(gd_char) + "\n" * 2)    # Prints the characters that has been tested

        g_char = input("Guess a character: ").lower()                   # g_char the character that is guessed

        # Checks if g_char is a valid character
        if len(g_char) == 1 and g_char.isalpha():

            # Checks if g_char already is a tested character
            if g_char in gd_char:
                print("You have already tested this character")

            # Checks if the character is included in the word
            elif g_char not in word and g_char not in gd_char:

                # Character gets appended to gd_char and life gets incremented
                life += 1
                gd_char.append(g_char)

            elif g_char in word and g_char not in gd_char:

                gd_char.append(g_char)

                # Fill the blanks in h_word with the characters that are included in the word
                for c in gd_char:
                    if c in word:
                        indices = [i for i, val in enumerate(word) if val == c]
                        for i in indices:
                            h_word[i] = c

            # Checks if the word has been guessed
            if "".join(h_word) == word:

                # Ends the guessing loop
                guessed = True
                print("Congratulations you guessed the word:\n")
                print("".join(h_word) + "\n")

                # Play again?
                again = input("Do you want to play again? y/n: ").lower()

                if again == "n":
                    run = False
                elif again == "y":
                    life = 0
                    gd_char = []
                    continue
                else:
                    guessed = False
                    print("You didn't type y or n")

            # Checks if the guesser lost
            elif life == 9:
                guessed = True
                print(man[life])
                print("You did not guess the word...")
                print(word)

                # Play again?
                again = input("Do you want to play again? y/n: ").lower()

                if again =="n":
                    run = False

                elif again == "y":
                    life = 0
                    gd_char = []
                    continue

                else:
                    guessed = False
                    print("You didn't type y or n")
            else:
                continue
        else:
            print("That is not a character")
