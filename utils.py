import random

def roll_two_d6() -> tuple[int, int]:
    rool1 = random.randint(1,6)
    rool2 = random.randint(1, 6)
    return rool1, rool2

def sum_roll_two_d6(roll: tuple)-> int:
    total = 0
    for i in roll:
        total += i
        total = int(total)
    return total


def is_bust(score: int) -> bool:
    if score < 100:
        return False
    else:
        return True

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if a > b:
        return 1
    if b > a:
        return 2
    else:
        return 3

def turn_decision() -> str:
    flag = True
    res = ""
    while flag:
        input_fn = input("please enter only 'r' or 'p' : \n")
        match input_fn:
            case "r":
                flag = False
                res = "r"
            case "p":
                flag = False
                res = "p"
    return res









