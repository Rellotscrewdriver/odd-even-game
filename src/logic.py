import toss

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
    else:
        print("computer wins")
