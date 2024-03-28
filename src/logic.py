import toss
import venue
import com

plyScore = 0
comScore = 0


# compares the results from the draw of player and computer by totaling both numbers and determining whether odd came or even
def compreResults(plyerChoice, cpuChoice):
    finlResult = (plyerChoice + cpuChoice) % 2 == 0 
    if finlResult == True:
        print("even came from the results")
        return "even"
    else:
        print("odd came from the results")
        return "odd"

# decides the final result
def determineWinner(result):
    if toss.plyChoice == result:
        print("player wins")
        venue.plyChosePos()
    else:
        print("computer wins")
        com.comChosePos()
        
def startPlaying(plyChoice):
    if plyChoice == "bat":
        plyBattin()
        #comBallin()
    elif plyChoice == "ball":
        comBattin()
        #plyBallin()

def plyBattin(): 
    global plyScore
    while True:
        batScore = int(input("Enter a number between 1 to 6: "))
        ballScore = com.compTossDraw()
        if batScore == ballScore:
            print("you lose, your score was: ", plyScore)
            break
        else:
            plyScore += batScore
            print("you win, your score is now: ", plyScore)


def comBattin():
    global comScore
    while True:
        ballScore = int(input("Enter a number between 1 to 6: "))
        batScore = com.compTossDraw()
        if batScore == ballScore:
            print("computer lose, his score was:", comScore)
            break
        else:
            comScore += batScore
            print("he wins, his score is now:", comScore)