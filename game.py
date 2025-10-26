import random
from utils import roll_two_d6

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False



def tie_breaker(p1_name, p2_name) -> dict:
    flag = True
    res = ""
    while flag:
        scor_player1 = roll_two_d6()
        a = 0
        scor_player2 = roll_two_d6()
        b = 0

        for roll in scor_player1:
            a += roll
        for roll in  scor_player2:
            b += roll
        print(f"the roll result of {p1_name} is: {scor_player1}\n"
             f"the roll result of {p2_name} is: {scor_player2} \n")

        if a > b:
            res = p1_name
            flag = False


        elif b > a:
            res = p2_name
            flag =  False

        else:
            print("let's try agen: \n")

    return res















