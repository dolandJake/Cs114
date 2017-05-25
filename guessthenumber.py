# This imports random, so that the program will have a random number it thinks of, keeping it unpredictable.
import random
correctnumber = random.randint(1, 30)
print('Time to test an organic mind. Guess a number between 1 and 30, you have six chances')

# This one tells the player that they have six chances to guess.
for guessesTaken in range(1, 7):
    print('YOU HAVE A LIMITED AMOUNT OF GUESSES!')
    guess = int(input())

    if guess == 42:
        print("That is the meaning of life, and in no way answers the question.")
    if guess < correctnumber:
        print('You guessed wrong, guess higher next time, or you will be closer to FAILURE')
    elif guess > correctnumber:
        print('You are WRONG, guess lower or you will remain wrong until you LOSE')
    else:
        break    # the correct guess breaks the loop

#this is what happens when either the player wins or loses, so the final step.
if guess == correctnumber:
    print('You did it, I genuinely cannot believe your pathetic organic mind guessed my number. It took you ' + str(guessesTaken) + ' times.')
else:
    print('Incorrect you pathetic organic. The number was, ' + str(correctnumber))

if guessesTaken == 1:
    print("How? Organics are supposed to be pathetic!")
