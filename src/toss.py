# starts the game
def startTossing():
    global plyChoice #made this variable global since determinewinner() function needs it after taking it's userinput
    print("\nWhat do you choose? odd or even?")
    plyChoice = input("your input: ")
    compreToss()

# compares the toss and determines what computer will choose next
def compreToss():
    if plyChoice == "odd" or plyChoice == "Odd":
        print("\ncomputer chose even")
    elif plyChoice == "even" or plyChoice == "Even":
        print("\ncomputer chose odd")
    else:
        print("\ninvalid choice, try again")

def tossMatch():
    print("\ndraw from range 1 to 6")
    draw = int(input("your input: "))
    return draw
