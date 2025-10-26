from game import *
from utils import *
def play_game():
    name_a = input("please enter your name:")
    name_b = input("please enter your name:")
    a_info = {"player_name": name_a , "score": 0 , "pass_count": False}
    b_info = {"player_name": name_b , "score": 0 , "pass_count": False}

    pass_fleg = not (a_info["pass_count"] and b_info["pass_count"])
    while pass_fleg:

        print(f"'{a_info["player_name"]}' please Choose 'p' for 'pass' or 'r' for 'roll' \n")
        player1_p_or_r = turn_decision()

        match player1_p_or_r:
            case "r":
                roll_of_a = roll_two_d6()
                sum_roll_of_a = sum_roll_two_d6(roll_of_a)
                a_info["score"] += sum_roll_of_a
                print(f"{a_info["player_name"]} your roll result is: {roll_of_a} \n"
                      f"{a_info["player_name"]} your score is : '{a_info["score"]}' \n"
                      f"{b_info["player_name"]} your score is : '{b_info["score"]}' \n")
                a_info["pass_count"] = False
                if is_bust(a_info["score"]):
                    if is_exact_100(a_info["score"]):
                        print(f"player:'{a_info["player_name"]}' your the winner! \n your score is: '{a_info["score"]}' \n")
                        break
                    else:
                        print(f"player:'{b_info["player_name"]}' your the winner! \n player '{a_info["player_name"]}' is out of range 100 \n")
                        break
            case "p":
                a_info["pass_count"] = True


        print(f"'{b_info["player_name"]}' please Choose 'p' for 'pass' or 'r' for 'roll' \n")
        player2_p_or_r = turn_decision()
        match player2_p_or_r:
            case "r":
                roll_of_b = roll_two_d6()
                sum_roll_of_b = sum_roll_two_d6(roll_of_b)
                b_info["score"] += sum_roll_of_b
                print(f"{b_info["player_name"]} your roll result is: {roll_of_b}\n"
                      f"{b_info["player_name"]} your score is : '{b_info["score"]}' \n"
                      f"{a_info["player_name"]} your score is : '{a_info["score"]}' \n")
                b_info["pass_count"] = False
                if is_bust(b_info["score"]):
                    if is_exact_100(b_info["score"]):
                        print(f"player:'{b_info["player_name"]}' your the winner! \n your score is: '{b_info["score"]}' \n")
                        break
                    else:
                        print(f'player:"{a_info["player_name"]} your the winner!" \n player "{b_info["player_name"]}" is out of range 100 \n')
                        break
            case "p":
                b_info["pass_count"] = True

        pass_fleg = not(a_info["pass_count"] and b_info["pass_count"])




    closer_to_target_check = closer_to_target(a_info["score"], b_info["score"])
    if closer_to_target_check == 3:
        equal_winner_result = tie_breaker(a_info["player_name"], b_info["player_name"])
        if equal_winner_result == a_info["player_name"]:
            print(f"{a_info["player_name"]} your the winner!")
        else:
            print(f"{b_info["player_name"]} your the winner! ")

    else:
        if closer_to_target_check == 1:
            print(f"player {a_info["player_name"]} your the winner! \n"
                  f"player {a_info["player_name"]} your score is: '{a_info["score"]}' \n"
                  f"player {b_info["player_name"]} your score is: '{b_info["score"]}' \n")
        if closer_to_target_check == 2:
            print(f"player {b_info["player_name"]} your the winner! \n"
                  f"player {b_info["player_name"]} your score is: '{b_info["score"]}' \n"
                  f"player {a_info["player_name"]} your score is: '{a_info["score"]}' \n")







if __name__ == "__main__":
    play_game()
