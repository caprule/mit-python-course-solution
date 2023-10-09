import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""

    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else:
            guessed_word += "_ "

    return guessed_word


def get_avaliable_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    avaliable_letters = ""
    for letters in all_letters:
        if letters not in letters_guessed:
            avaliable_letters += letters

    return avaliable_letters


def hangman(secret_word):
    letters_guessed = []
    guesses_left = 6
    warnings = 3
    print("The secret word contains ", len(secret_word), " letters and you are starting with 6 guesses")

    while guesses_left > 0:
        print("you have ", guesses_left, "guesses left")
        avaliable_letters = get_avaliable_letters(letters_guessed)
        print("Available letters: ", avaliable_letters)

        user_guess = input("Please guess a letter: ").lower()
        if len(user_guess) != 1:
            print("Invalid input, please put in a single letter")

            if warnings > 0:
                warnings -= 1
                print("You have ", warnings, " warning(s) left.")
            else:
                guesses_left -= 1
                print("You have", guesses_left, "guess(es) left.")
            continue
        if user_guess in letters_guessed:
            print("oops, you have already guessed that letter!!")
            if warnings > 0:
                warnings -= 1
                print("You have ", warnings, " warning(s) left.")
            else:
                guesses_left -= 1
                print("You have", guesses_left, "guess(es) left")
                continue

        elif user_guess in secret_word:
            letters_guessed.append(user_guess)
            print("Good guess!!")

        else:
            letters_guessed.append(user_guess)
            print("oops , that letter is not in my word.")
            guesses_left -= 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        print("Guessed word: ", guessed_word)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you've won!")
            break

    if not is_word_guessed(secret_word, letters_guessed):
        print("Sorry, you've run out of guesses. The word was:", secret_word)


# def match_with_gaps(my_word, other_word):
#     my_word = secret_word
#     other_word = ""

#     for letters in my_word:
#         if letters not in other_word:
#             return False
#     return True

# def show_possible_matches(my_word):
#     my_word = my_word.replace(" ", "")
#     matches_found = False


#     for word in wordlist:
#         if match_with_gaps(my_word, word):
#             print(word)
#             matches_found = True

#     if not matches_found:
#         print("No matches found")


# def hangman_with_hints(secret_word):
#     letters_guessed = []
#     guesses_left = 6
#     warnings = 3
#     print("The secret word contains " , len(secret_word), " letters and you are starting with 6 guesses")

#     while guesses_left > 0:
#         print("you have ", guesses_left , "guesses left" )
#         avaliable_letters = get_avaliable_letters(letters_guessed)
#         print("Available letters: ", avaliable_letters)

#         user_input = input("Please guess a letter: " ).lower()

#         if user_input == '*':
#             show_possible_matches(get_guessed_word(secret_word, letters_guessed))
#             continue

#         if len(user_input) != 1:
#             print("Invalid input, please put in a single letter")

#             if warnings > 0:
#                 warnings -= 1
#                 print("You have ",warnings," warning(s) left.")
#             else:
#                 guesses_left -= 1
#                 print("You have" , guesses_left ,"guess(es) left.")
#             continue
#         if user_input in letters_guessed:
#             print("oops, you have already guessed that letter!!" )
#             if warnings > 0:
#                 warnings -= 1
#                 print("You have ",warnings," warning(s) left.")
#             else:
#                 guesses_left -= 1
#                 print("You have" , guesses_left ,"guess(es) left")
#                 continue

#         elif user_input in secret_word:
#             letters_guessed.append(user_input)
#             print("Good guess!!" )

#         else:
#             letters_guessed.append(user_input)
#             print("oops , that letter is not in my word." )
#             guesses_left -= 1


#         if user_input not in secret_word:
#             if user_input in "aeiou":
#                 guesses_left -= 2  # Deduct 2 guesses for a wrong vowel
#             else:
#                 guesses_left -= 1

#         guessed_word = get_guessed_word(secret_word, letters_guessed)

#         print("Guessed word: ", guessed_word)

#         if is_word_guessed(secret_word, letters_guessed):
#             print("Congratulations, you've won!")
#             break

#     if not is_word_guessed(secret_word, letters_guessed):
#         print("Sorry, you've run out of guesses. The word was:", secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
