import os
import keyboard


os.system('cls')
player1 = 'X'
player2 = 'O'


PLAYER = {'X': player1, 'O': player2}
GAME_BOARD = [' '] * 9
SELECTOR = '='
WINNER_BOARDS = [[True, True, True,
                 False, False, False,
                 False, False, False],

                 [False, False, False,
                 True, True, True,
                 False, False, False],


                 [False, False, False,
                  False, False, False,
                 True, True, True],

                 [True, False, False,
                 True, False, False,
                 True, False, False],


                 [False, True, False,
                 False, True, False,
                 False, True, False],


                 [False, False, True,
                 False, False, True,
                 False, False, True],

                 [True, False, False,
                 False, True, False,
                 False, False, True],


                 [False, False, True,
                 False, True, False,
                  True, False, False]]


player_position = 0
curr_player = PLAYER['X']
is_game_ended = False
winner = None
is_game_running = True


def clear_board():
    os.system('cls')


def draw_position(board_position, draw_selector=False):
    if draw_selector and board_position == player_position:
        return SELECTOR
    else:
        return GAME_BOARD[board_position]


def draw_board(draw_selector=False):

    print(f' {draw_position(0,draw_selector)} | {draw_position(1,draw_selector)} | {draw_position(2,draw_selector)} ')
    print('___|___|___')
    print(f' {draw_position(3,draw_selector)} | {draw_position(4,draw_selector)} | {draw_position(5,draw_selector)} ')
    print('___|___|___')
    print(f' {draw_position(6,draw_selector)} | {draw_position(7,draw_selector)} | {draw_position(8,draw_selector)} ')
    print('   |   |   ')

    if not is_game_ended:
        print(f'\ncurrent_player = {curr_player}')
        print("Press space to select slot")


def reset_game():
    global GAME_BOARD, pos, curr_player, is_game_ended, winner, is_game_running
    clear_board()
    GAME_BOARD = [' '] * 9
    pos = 0
    curr_player = PLAYER['X']
    is_game_ended = False
    winner = None
    is_game_running = True
    draw_board(True)


def close_game():
    global is_game_running
    is_game_running = False
    print("The game is over!")


def swap_player():
    global curr_player
    if curr_player == PLAYER['X']:
        curr_player = PLAYER['O']

    else:
        curr_player = PLAYER['X']


def is_board_full():
    for slot in GAME_BOARD:
        if slot == ' ':
            return False
    return True


def is_game_over():
    global winner
    is_over = False

    for possible_board in WINNER_BOARDS:
        is_over = True
        for pos, bool in enumerate(possible_board):
            if bool and GAME_BOARD[pos] != curr_player:
                is_over = False
                break

        if is_over:
            break

    if not is_over:
        return is_board_full()

    else:
        winner = curr_player

    return is_over


def is_position_empty():
    return GAME_BOARD[player_position] == ' '


def print_game_winner():
    if winner == None:
        print('Draw!!!')
    else:
        print(f'Player {winner} won the game!')

    print('press space to restart the game mor backspace to close')


def select_slot():
    global is_game_ended, winner
    if is_position_empty():
        GAME_BOARD[player_position] = curr_player

        if is_game_over():
            is_game_ended = True
            clear_board()
            draw_board()
            print_game_winner()

        else:
            swap_player()


def move_to_position(direction):
    global player_position

    new_position = player_position + direction
    if new_position >= 0 and new_position <= 8:
        player_position = new_position


def on_key_press(key):

    if is_game_ended:
        if key == "space":
            reset_game()
        return

    if key == "left arrow":
        move_to_position(-1)
    elif key == "right arrow":
        move_to_position(1)
    elif key == "up arrow":
        move_to_position(-3)
    elif key == "down arrow":
        move_to_position(3)

    elif key == 'space':
        select_slot()

    if not is_game_ended:
        clear_board()
        draw_board(True)


def init_keyboard():
    keyboard.on_press_key("left arrow", lambda _: on_key_press("left arrow"))
    keyboard.on_press_key("right arrow", lambda _: on_key_press("right arrow"))
    keyboard.on_press_key("up arrow", lambda _: on_key_press("up arrow"))
    keyboard.on_press_key("down arrow", lambda _: on_key_press("down arrow"))
    keyboard.on_press_key("space", lambda _: on_key_press("space"))
    keyboard.on_press_key("backspace", lambda _: close_game())


def main():
    init_keyboard()
    draw_board(True)
    while(is_game_running):
        continue


main()