# This program implements the "guess the number" game
# One player chooses a random number within the specified
# range while the other player tries to guess that number.
# the player can use the buttons on the side to change
# the range of secret number.

# In addition to minor formatting changes and error checking,
# I've also added the feature which allows for the user to
# think of a number while the computer tries to guess. 

# imports
import simpleguitk as simplegui
import random
import math

# global variables
secret_number = 0 # for when the player is guessing
current_guess = 0 # for when the computer is guessing
user_is_guessing = True
current_range = 100
guesses_remaining = 7
upper_limit = 100 # for when computer is guessing
lower_limit = 0 # for when computer is guessing

def new_game():
    """
    This is a wrapper that leads into a new game.
    The type of new game depends on whether the
    computer or the player is the one guessing
    """
    print "--------\nNew Game\n--------\n"
    if user_is_guessing:
        new_game_user_guessing()
    else:
        new_game_computer_guessing()
    
def new_game_user_guessing():
    """
    This function generates a new game by creating a
    random secret number (within range), reseting the
    number of guesses remaining to be proportional to
    the range, and printing out some information for the
    user to get started
    """
    global secret_number, guesses_remaining
    # creates random number between 0-99
    secret_number = random.randrange(0, current_range)
    # general formula for calculating the number of guesses needed
    guesses_remaining = int(math.ceil(math.log(current_range, 2)))
    # printing out the information
    print "Try to guess the secret number. Enter your guesses"
    print "into the input area. The range is from 0 to", current_range
    print "guesses remaining:", guesses_remaining
    print ""
    
def new_game_computer_guessing():
    """
    This function generates a new game by generating a number
    of guesses remaining proportional to the range, initializing
    upper and lower limits, creating an initial guess for the
    computer, and printing out instructions for the user
    """
    global current_guess, guesses_remaining
    global upper_limit, lower_limit
    # general formula for guesses remaining
    guesses_remaining = int(math.ceil(math.log(current_range, 2)))
    lower_limit = 0
    upper_limit = current_range
    # the computer's guess is always the average of the upper and lower limit
    current_guess = (upper_limit + lower_limit) / 2
    # printing out the information
    print "Think of a random number between 0 and", (current_range - 1)
    print "For each guess that the computer makes, type \"higher\", \"lower\","
    print "or \"correct\" into the input area."
    print "The computer is allowed", guesses_remaining, "guesses.\n"
    # concatonating with '+' gets rid of the space the comma leaves
    print "Is it", (str(current_guess) + "?")
    print ""
    
def range100():
    """
    This function changes the upper limit of the game
    to 100 and starts a new game
    """
    global current_range
    current_range = 100
    print "The range is now 0-99"
    new_game()

def range1000():
    """
    This function changes the upper limit of the game
    to 1000 and starts a new game
    """
    global current_range
    current_range = 1000
    print "The range is now 0-999"
    new_game()
    
def user_guesses():
    """
    This function flags that the user should be the
    one guessing and starts a new game
    """
    global user_is_guessing
    user_is_guessing = True
    print "The user is now the one guessing"
    new_game()
    
def computer_guesses():
    """
    This function flags that the computer should be the
    one guessing and starts a new game
    """
    global user_is_guessing
    user_is_guessing = False
    print "the computer is now the one guessing"
    new_game()
    
def input_text(text):
    """
    This is a wrapper that processes inputted text.
    If the player is guessing it processes it as a
    guess. If not, it processes it as a response.
    """
    if user_is_guessing:
        input_guess(text)
    else:
        input_response(text)
    
def input_guess(guess):
    """
    This function processes the user entering a number,
    comparing it to the secret number and responding
    accordingly. This function should only be called
    if the user is the one guessing.
    """
    global guesses_remaining
    # Checks to make sure the guess is a number
    if not guess.isdigit():
        print "Error: please make sure to enter a numerical value\n"
    else:
        guess_num = int(guess)
        print "Your guess was", guess_num
        guesses_remaining -= 1
        print "guesses remaining:", guesses_remaining
        # if the user guesses correctly
        if guess_num == secret_number:
            print "\nCorrect!!!" # '\n' = go to next line
            # minor check for grammar (guesses vs. guess)
            if (guesses_remaining != 1):
                print "You guessed the correct number with", guesses_remaining, "guesses to spare!"
            else:
                print "You guessed the correct number with 1 guess to spare!"
            print "Let's play again!\n"
            new_game()
        else:
            # checks if the guess was too high or too low
            if secret_number > guess_num:
                print "Higher! \n"
            else:
                print "Lower! \n"
            # checks to see if the player has remaining guesses
            # if not, the game starts over
            if guesses_remaining == 0:
                print "That's it! You're all out of guesses!"
                print "the secret number was", secret_number
                print "Let's play again!\n"
                new_game()
                
def input_response(response):
    """
    This function processes the user entering a response
    to the computer's previous guess, and adjusts the
    computer's next move accordingly. This function should
    only be called if the computer is the one guessing.
    """
    global current_guess, guesses_remaining
    global upper_limit, lower_limit
    # to account for case sensitivity 
    response_lc = response.lower()
    # checks to make sure the user entered a valid response 
    if (response_lc != "higher") and (response_lc != "lower") and (response_lc != "correct"):
        print "Error: I don't understand. Please enter \"higher\", \"lower\", or \"correct\"."
    else:
        guesses_remaining -= 1
        # if the computer's last guess was correct
        if response_lc == "correct":
            print "Yay, I got it!"
            print "Let's play again!\n"
            new_game()
        # if it was incorrect, but it still has guesses left
        elif guesses_remaining > 0:
            if response_lc == "higher":
                lower_limit = current_guess + 1
            else:
                upper_limit = current_guess - 1
            current_guess = (upper_limit + lower_limit) / 2
            # minor check for grammar (guesses vs. guess)
            if (guesses_remaining > 1):
                print "Hm, I've got", guesses_remaining, "guesses left..."
            else:
                print "Hm, only 1 guess left..."
            print "Is it", (str(current_guess) + "?\n")
        # if the computer is incorrect and out of guesses
        # this condition should theoretically never be reached
        # (unless due to human or computer error)
        else:
            print "Ack, I'm out of guesses! How'd that happen?"
            print "Oh well- you win. Let's play again!\n"
            new_game()


def introduction():
    """
    This function provides quick introduction on how to play
    the game, as well as explains some additional features of
    the program
    """
    print "Welcome to \"guess a number\", where one player thinks"
    print "of a secret number and the other player tries to guess it."
    print "Use the input area to enter guesses or responses."
    print "You can also use the buttons on the left to change the"
    print "range of the secret number. Additionally, you can change"
    print "whether the user or the computer is the one guessing."
    print "We'll start with a range of 0-99 with the user guessing."
    print ""
    
# main methods of program
frame = simplegui.create_frame("Guess a number", 200, 200)
frame.add_input("Input Area", input_text, 100)
frame.add_button("Range: 0-99", range100, 100)
frame.add_button("Range: 0-999", range1000, 100)
frame.add_button("Player guesses", user_guesses, 100)
frame.add_button("Computer guesses", computer_guesses, 100)
introduction()
new_game()