def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        if is_win(game):
            print("Win!")
            break  # Terminate the game
        if n == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board
        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()
def is_win(game):
    # Check rows and columns
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    return False

def is_full(game):
    return all(cell != ' ' for row in game for cell in row)

def print_board(game):
    print("\nCurrent board:")
    for row in game:
        print(" ".join(row))
    print()

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0  # 0 for player 1, 1 for player 2

    print("Tic-Tac-Toe Game!")
    print("X = Player 1")
    print("O = Player 2")

    while True:
        print(f"Player {turn + 1} ({players[turn]}): ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3] (e.g., 1 2): ")
        
        valid_input = False
        while not valid_input:
            try:
                i, j = map(int, input().strip().split())  # 去除多余空格并分割输入
                if i < 1 or i > 3 or j < 1 or j > 3:
                    print("Invalid input! Please enter numbers between 1 and 3.")
                elif game[i - 1][j - 1] != ' ':  # 检查格子是否已被占用
                    print("This cell is already taken! Please choose another one.")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")
            except IndexError:
                print("Invalid input! Please enter two numbers separated by a space.")
        
        game[i - 1][j - 1] = players[turn]  # 标记格子
        print_board(game)

        if is_win(game):
            print(f"Player {turn + 1} wins!")
            break
        if is_full(game):
            print("It's a tie!")
            break

        turn = 1 - turn  # 切换玩家

if __name__ == "__main__":
    main()
