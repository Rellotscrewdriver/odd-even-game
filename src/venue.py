import logic
import com

plyScore = 0
comScore = 0

def plyChosePos():
    print("choose batting or balling?")
    chooseVenue = input("your input: ")
    if chooseVenue == "batting":
        print("\nplayer chose batting, computer had to choose balling")
        startPlaying("bat")
        # here computer should choose balling
    elif chooseVenue == "balling":
        print("\nplayer chose balling, computer had to choose batting")
        startPlaying("ball")
        # here computer should choose batting

def startPlaying(plyChoice):
    if plyChoice == "bat":
        plyBattin()
        print("\nnow it's time to switch sides\nnow the computer is batting now")
        comBattin()
        print(logic.determineRealWinner(plyScore, comScore))
    elif plyChoice == "ball":
        comBattin()
        print("\nnow it's time to switch sides\nnow the player is batting now")
        plyBattin()
        print(logic.determineRealWinner(plyScore, comScore))

def plyBattin(): 
    global plyScore
    while True:
        batScore = int(input("\nEnter a number between 1 to 6: "))
        ballScore = com.compTossDraw()
        print("computer draws", ballScore)
        if batScore == ballScore:
            print("\nyou lose, your score was: ", plyScore)
            break
        else:
            plyScore += batScore
            print("\nyou win, your score is now: ", plyScore)


def comBattin():
    global comScore
    while True:
        ballScore = int(input("\nEnter a number between 1 to 6: "))
        batScore = com.compTossDraw()
        print("computer draws", batScore)
        if batScore == ballScore:
            print("\ncomputer lose, his score was:", comScore)
            break
        else:
            comScore += batScore
            print("\nhe wins, his score is now:", comScore)
