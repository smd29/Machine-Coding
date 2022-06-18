import random
import sys
import time


snakes = {
62: 5,
33: 6,
49: 9,
88: 16,
41: 20,
56: 53,
98: 64,
93: 73,
95: 75
}
ladders = {
2: 37,
27: 46,
10: 32,
51: 68,
61: 79,
65: 84,
71: 91,
81: 100
}

def welcome_msg():
    msg = "let's start the game"
    print(msg)

def get_player_names():
    player1 = input("First Player: ")
    player2 = input("Second Player: ")
    print(f"Let's start the match between {player1} and {player2}")
    return player1, player2

def get_dice_value():
    time.sleep(1)
    dice_value = random.randint(1,6)
    print(f"Its a {dice_value}")
    return dice_value

#for printing
def perform_snake(player,old_val,curr_val):
    print(f"{player} got a snake: Down from {old_val} to {curr_val}")

def perform_ladder(player,old_val,curr_val):
    print(f"{player} got a ladder: Up from {old_val} to {curr_val}")

#play the actual game
def snake_ladder(player,curr_val,dice_val):
    time.sleep(1)
    old_val = curr_val
    curr_val = old_val + dice_val

    if curr_val > 100:
        print("the move is not possible")
        return old_val

    print(f"{player} moved from {old_val} to {curr_val}")
    if curr_val in snakes:
        final_val = snakes[curr_val]
        perform_snake(player,curr_val,final_val)

    elif curr_val in ladders:
        final_val = ladders[curr_val]
        perform_ladder(player, curr_val, final_val)

    else:
        final_val = curr_val

    return final_val

def check_win(player,pos):
    time.sleep(1)
    if pos == 100:
        print(f"{player} has won the game")
        sys.exit(1)

def start():
    welcome_msg()
    time.sleep(1)
    player1,player2 = get_player_names()
    time.sleep(1)

    player1_pos, player2_pos = 0,0
    while True:
        time.sleep(1)
        input1 = input(f"{player1}: hit enter to roll the dice")
        print("...Rolling the dice...")
        dice_val = get_dice_value()
        time.sleep(1)
        player1_pos = snake_ladder(player1,player1_pos,dice_val)
        check_win(player1,player1_pos)

        input1 = input(f"{player2}: hit enter to roll the dice")
        print("...Rolling the dice...")
        dice_val = get_dice_value()
        time.sleep(1)
        player1_pos = snake_ladder(player2, player2_pos, dice_val)
        check_win(player2, player2_pos)

if __name__ == "__main__":
    start()
