import random
import math

def main():
    GAME_END_POINTS = 10
    COMPUTER_HOLD = 10
    is_user_turn = True
    print("\n")
    print("Welcome to Jeopardy Dice!")
    print("\n")
    user_plcr = 0
    computer_plcr = 0

    while(user_plcr <= GAME_END_POINTS and computer_plcr <= GAME_END_POINTS):
        print_current_player(is_user_turn)
        user_total = take_turn(is_user_turn,COMPUTER_HOLD)
        user_plcr = user_plcr + user_total
        if user_total >= GAME_END_POINTS:
            print("user wins!")
            break
        is_user_turn = get_next_player(is_user_turn)
        print_current_player(is_user_turn)
        computer_total = take_turn(is_user_turn,COMPUTER_HOLD)
        computer_plcr = computer_plcr + computer_total
        if computer_total >= GAME_END_POINTS:
            print("computer wins!")
            break
        report_points(user_plcr,computer_plcr)
        print("\n")
        is_user_turn = get_next_player(is_user_turn)

def print_current_player(is_user_turn):
    if is_user_turn == True:
        print "-----------------------------\n" + "It is now the human's turn"
    elif is_user_turn == False:
        print "-----------------------------\n" + "It is now the computer's turn"

def roll_die():
    number = random.randint(1,6)
    return number

def take_turn(is_user_turn, COMPUTER_HOLD):
    human_score = 0
    computer_score = 0
    if is_user_turn == True:
        begin = raw_input("roll? [yn]")
        if begin == 'y' or begin == 'Y':
            human_rand = roll_die()
        elif begin == 'n' or begin == 'N':
            is_user_turn = False
            return human_score
        while human_rand != 1:
            human_score = human_score + human_rand
            if human_score != 0:
                human_score = str(human_score)
                human_rand = str(human_rand)
                print("roll: " + human_rand)
                print("Current Score: " + human_score)
                human_rand = int(human_rand)
                human_score = int(human_score)
                again = raw_input("roll again? [yn]")
                print("\n")
                if again == 'y' or again == 'Y':
                    human_rand = roll_die()
                    continue
                elif again == 'n' or again == 'N':
                    is_user_turn = False
                    break
            else:
                human_score = 1
                human_rand = str(human_rand)
                print("roll: " + human_rand)
                human_rand = int(human_rand)
                print("You rolled a 1. Turn over.")
                human_score = str(human_score)
                print("Current Score: " + human_score)
                human_score = int(human_score)
                return human_score
        if human_rand == 1:
            human_rand = str(human_rand)
            print("roll: " + human_rand)
            human_rand = int(human_rand)
            print("You rolled a 1. Turn over.")
            human_score = 1
            human_score = str(human_score)
            print("Current Score: " + human_score)
            human_score = int(human_score)
            return human_score
        else:
            return human_score
    elif is_user_turn == False:
        computer_rand = roll_die()
        while computer_rand != 1:
            computer_score = computer_score + computer_rand
            if computer_score != 0:
                computer_rand = str(computer_rand)
                print("roll: " + computer_rand)
                computer_rand = int(computer_rand)
                if computer_score <= COMPUTER_HOLD:
                    computer_rand = roll_die()
                    continue
                else:
                    computer_score = str(computer_score)
                    print("*computer holds on " + computer_score + "*")
                    computer_score = int(computer_score)
                    is_user_turn = True
                    break
            else:
                computer_score = 1
                computer_rand = str(computer_rand)
                print("roll: " + computer_rand)
                computer_rand = int(computer_rand)
                print("The computer rolled a 1. Turn over.")
                return computer_score
        if computer_rand == 1:
            computer_rand = str(computer_rand)
            print("rollclea " + computer_rand)
            computer_rand = int(computer_rand)
            print("The computer rolled a 1. Turn over.")
            computer_score = 1
            return computer_score
        else:
            return computer_score

def report_points(user_total,computer_total):
    print("\n")
    print("The point totals are now: ")
    user_total = str(user_total)
    print("human: " + user_total)
    user_total = int(user_total)
    computer_total = str(computer_total)
    print("computer: " + computer_total)
    computer_total = int(computer_total)

def get_next_player(is_user_turn):
    if is_user_turn == True:
        is_user_turn = False
        return is_user_turn
    elif is_user_turn == False:
        is_user_turn = True
        return is_user_turn

if __name__ == '__main__':
    main()