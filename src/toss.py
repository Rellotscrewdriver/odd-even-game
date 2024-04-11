# starts the game
def startTossing():
    global plyChoice #made this variable global since determinewinner() function needs it after taking it's userinput
    print("\nWhat do you choose? odd or even?")
    plyChoice = input("your input: ")
    compreToss()

# compares the toss and determines what computer will choose next
def compreToss():
    if plyChoice.lower() == "odd":
        print("\ncomputer chose even")
    elif plyChoice.lower() == "even":
        print("\ncomputer chose odd")
    else:
        print("\ninvalid choice, try again")

# prompt the user to input from 1 to 6
def tossMatch():
    print("\ndraw from range 1 to 6")
    draw = int(input("your input: "))
    return draw
