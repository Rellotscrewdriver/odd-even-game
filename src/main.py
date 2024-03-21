import toss
import logic
import com

print("Welcome to the portable cricket session!")
print("I am your host, lucky. which is lucky")

while True:
    # tossing
    toss.startTossing()
    logic.determineWinner(logic.compreResults(toss.tossMatch(), com.compTossDraw()))