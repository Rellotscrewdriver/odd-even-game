import com
import toss
def compreResults(plyerChoice, cpuChoice):
    finlResult = (plyerChoice + cpuChoice) % 2 == 0 
    if finlResult == True:
        print("even came from the results")
        return "even"
    else:
        print("odd came from the results")
        return "odd"
