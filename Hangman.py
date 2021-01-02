
import random
with open("wordlist.txt", "r") as f: 
        words = []
        for elem in f.readlines():
            words.append(elem.rstrip())

def hangman_multiplayer(wrd):
    print(f"Welcome to Hangman! I am thinking of a word with {len(wrd)} letters.")
    guesses = 10
    letters_guessed = 0
    guessed_so_far = []
    blank = []
    for letter in wrd:
        blank.append("_ ")
    while (letters_guessed < len(wrd)) and (guesses > 0):
        a = input("What is your guess? ")
        if a in guessed_so_far:
            print("You've already that that letter.")
        if a in wrd:
            for i in range(len(wrd)):
                if wrd[i] == a:
                    blank[i] = a + " "
                    letters_guessed += 1
            print("".join(blank))
            print(f"You have {guesses} guesses remaining.")
            guessed_so_far.append(a)
        if (not a in wrd) and (a not in guessed_so_far):
            guesses -= 1
            print(f"{a} was not in the word. You have {guesses} guesses remaining.")
            guessed_so_far.append(a)
    if guesses == 0:
        print("Sorry, you're out of guesses. The word was {wrd}.")
    else:
        print(wrd)
        print("Congratulations, you got the word right!")

def hangman_single():
    hangman_multiplayer(words[random.randrange(len(words))])

hangman_single()


            