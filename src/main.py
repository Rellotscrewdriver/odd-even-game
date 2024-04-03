import toss
import logic
import com

print("Welcome to the portable cricket session!")

while True:
    toss.startTossing()
    logic.determineWinner(logic.compreResults(toss.tossMatch(), com.compTossDraw()))
