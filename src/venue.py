import logic

def plyChosePos():
    print("choose batting or balling?")
    chooseVenue = input("your input: ")
    if chooseVenue == "batting":
        print("player chose batting, computer had to choose balling")
        logic.startPlaying("bat")
        # here computer should choose balling
    elif chooseVenue == "balling":
        print("player chose balling, computer had to choose batting")
        logic.startPlaying("ball")
        # here computer should choose batting