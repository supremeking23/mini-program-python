# number of guesses
guesses = 5

hidden_word = "stream"

still_has_tries = True


while still_has_tries:
    guess_word = input("what's the word ? ")
    if hidden_word == guess_word:
        print("you guess it right")
        break
    else:
        guesses-=1
        if guesses == 0:
            still_has_tries = False
else:
    print("sorry you run out of tries")
    
print("you reach the end of the game")