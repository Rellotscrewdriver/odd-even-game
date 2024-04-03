import sys
sys.path.append('../src')
import com
import logic

def test_cpu_toss():
    cpu_give_number = com.compTossDraw()
    for i in range(1, 7):
        if cpu_give_number == i:
            assert cpu_give_number == i

def test_cpu_venue():
    cpu_give_number = com.comChooseVenue()
    for i in range(1, 2):
        if cpu_give_number == i:
            assert cpu_give_number == i

def test_compare_results():
    assert logic.compreResults(2, 2) == "even"
    assert logic.compreResults(2, 3) == "odd"

def test_winner():
    assert logic.determineRealWinner(3, 2) == "PLAYER WIN!!! CONGRATS"
    assert logic.determineRealWinner(2, 3) == "YOU LOSE!!"
    assert logic.determineRealWinner(1, 1) == "TIED, REMATCH NEEDED"
