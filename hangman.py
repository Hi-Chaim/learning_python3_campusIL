HANGMAN_ASCII_ART = "  _    _\n | |  | |\n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\\n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|\n                      __/ |\n                     |___/\n"
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, MAX_TRIES)
guess = input("Guess a letter: ")
if len(guess) > 1 and guess.isalpha():
    print("E1")
if len(guess) == 1 and guess.isalpha() == False:
    print("E2")
if len(guess) > 1 and guess.isalpha() == False:
    print("E3")
if len(guess) == 1 and guess.isalpha():
    print(guess.lower())
user_word = input("Please enter a word: ")
print("_ " * len(user_word))
