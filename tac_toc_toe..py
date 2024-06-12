import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there are any empty spaces left on the board
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to get the user's move
def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("The cell is already occupied. Try again.")
        except ValueError:
            print("Invalid move. Please enter a number between 1 and 9.")

# Function to get the computer's move
def get_computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

# Main game function
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # User is 'X' and computer is 'O'
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        if current_player == "X":
            print("Your turn.")
            row, col = get_user_move(board)
        else:
            print("Computer's turn.")
            row, col = get_computer_move(board)
        
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            if current_player == "X":
                print("Congratulations! You win!")
            else:
                print("Computer wins. Better luck next time!")
            break
        
        if is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
