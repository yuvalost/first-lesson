import random


def print_board(board):

    print("   (1)|    (2)|   (3)  ")
    print("      |       |     ")
    print(f" {board[0][0]}    |  {board[0][1]}    |  {board[0][2]} ")
    print(" -----|-------|-----")
    print("   (4)|    (5)|   (6)  ")
    print("      |       |     ")
    print(f" {board[1][0]}    |  {board[1][1]}    |  {board[1][2]} ")
    print(" -----|-------|-----")
    print("   (7)|    (8)|   (9)  ")
    print("      |       |     ")
    print(f" {board[2][0]}    |  {board[2][1]}    |  {board[2][2]} ")


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player 1: {user_name}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print("That cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def get_computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

def guess_starting_player():
    guess = input("Guess who starts (X or O): ")
    if guess == 'X' or 'O':
        return guess
    # else:
    #     return random.choice(['X', 'O'])


def main():
    global user_name
    print("Welcome to Tic-Tac-Toe!")
    user_name = input("please enter your name: ")
    print(f"Hey {user_name} lets see who starts....")
    starting_player = guess_starting_player()
    print(f"ok so {starting_player} is going to start.")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = starting_player
    computer = 'X' if starting_player == 'o' else 'o'

    computer_turn = False


    print_board(board)

    while True:
        if not computer_turn and player == 'X':
            row, col = get_player_move(player, board)
        elif not computer_turn and player == 'O':
            row, col = get_computer_move(board)
            print_board(board)
            print(f"Computer played your turn!")

        else:
            row, col = get_computer_move(board)
            print(f"Computer played your turn!")

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That cell is already occupied. Try again.")
            continue

        print_board(board)

        if check_win(board, player):
            if player == starting_player:
                print(f"{user_name} wins!")
            else:
                print("Computer wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # player = 'X' if player == 'O' else 'O'

        player = starting_player if player == computer else computer


if __name__ == "__main__":
    main()
