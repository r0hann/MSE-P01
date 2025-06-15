def print_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_fresh_board():
    return [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]

def tic_tac_toe():
    scores = {'X': 0, 'O': 0}

    while True:
        board = get_fresh_board()
        current_player = 'X'

        while True:
            print_board(board)
            move = input(f"Player {current_player}, enter a number (1-9) to place your mark: ")

            if move not in [str(n) for n in range(1, 10)]:
                print("Invalid input. Try again.")
                continue

            placed = False
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = current_player
                        placed = True
                        break
                if placed:
                    break

            if not placed:
                print("That spot is already taken. Try another.")
                continue

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                scores[current_player] += 1
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        print(f"Scores => X: {scores['X']} | O: {scores['O']}")
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break

def main():
    tic_tac_toe()


if __name__ == "__main__":
    main()
