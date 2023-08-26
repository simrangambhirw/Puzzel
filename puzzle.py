import random
import time
import threading

BOARD_SIZE = 4
TILES = 'AABBCCDDEEFFGGHH'
score = 0
time_left = 60
game_over = False

# Shuffle the tiles and create the board
board = [list(TILES[i:i+BOARD_SIZE]) for i in range(0, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE)]
random.shuffle(board)
for row in board:
    random.shuffle(row)

# Create a covered board
covered_board = [['*' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(b):
    for row in b:
        print(' '.join(row))
    print()

def get_user_choice():
    while True:
        try:
            row, col = map(int, input("Enter row and column (e.g. '1 2' for first row, second column): ").split())
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and covered_board[row][col] == '*':
                return row, col
        except ValueError:
            pass
        print("Invalid choice. Try again.")

def timer():
    global game_over
    time.sleep(time_left)
    if not game_over:
        print("\nTime's up! Try again.")
        game_over = True

print("Memory Puzzle Game")
print("==================")
print_board(covered_board)

# Start the timer
timer_thread = threading.Thread(target=timer)
timer_thread.start()

while not game_over:
    # Get the first tile
    print("Select the first tile:")
    row1, col1 = get_user_choice()
    covered_board[row1][col1] = board[row1][col1]
    print_board(covered_board)

    # Get the second tile
    print("Select the second tile:")
    row2, col2 = get_user_choice()
    covered_board[row2][col2] = board[row2][col2]
    print_board(covered_board)

    # Check for a match
    if board[row1][col1] == board[row2][col2]:
        print("It's a match!")
        score += 1
    else:
        print("Not a match. Try again.")
        time.sleep(1)
        covered_board[row1][col1] = '*'
        covered_board[row2][col2] = '*'
        print_board(covered_board)

    # Check if all tiles are uncovered
    if all(cell != '*' for row in covered_board for cell in row):
        print(f"Congratulations! You matched all pairs!")
        game_over = True

# End the game if the user didn't finish within the timer's duration
if not game_over:
    print("You couldn't finish on time. Try again!")
