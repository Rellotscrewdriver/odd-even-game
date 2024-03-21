import com
def chooseToss():
    print("What do you choose? odd or even?")
    plyChoice = input("your input: ")
    return plyChoice
def compreToss(playaChoice):
    if playaChoice == "odd" or playaChoice == "Odd":
        print("computer chose even")
    elif playaChoice == "even" or playaChoice == "Even":
        print("computer chose odd")
    else:
        print("invalid choice, try again")
