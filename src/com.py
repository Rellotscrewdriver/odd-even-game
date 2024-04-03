import random
import venue

def compTossDraw():
    return random.randint(1, 6)

def comChooseVenue():
    return random.randint(1, 2)

def comChosePos():
    chooseVenue = comChooseVenue()
    if chooseVenue == 1:
        print("computer chose batting, you had to choose balling")
        venue.startPlaying("ball")
    elif chooseVenue == 2:
        print("computer chose balling, you had to choose batting")
        venue.startPlaying("bat")       
    else:
        print("jesus, really random integer?")
