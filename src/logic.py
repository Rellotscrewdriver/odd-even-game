import toss
import venue
import com


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


def determineRealWinner(plyScore, comScore):
    print("\nScoreBoard: ")
    print("Player: ", plyScore, "| Computer: ", comScore)
    if plyScore > comScore:        
        return "PLAYER WIN!!! CONGRATS"
    elif plyScore < comScore:
        return "YOU LOSE!!"
    else:
        return "TIED, REMATCH NEEDED"
