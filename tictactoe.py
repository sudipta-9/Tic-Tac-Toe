import random

def create_board():
  board = []
  for i in range(3):
    row = []
    for j in range(3):
      row.append(0)
    board.append(row)
  return board

def print_board(board):
  for i in range(3):
    for j in range(3):
      print(board[i][j], end=" ")
    print()

def get_user_input():
  while True:
    cell = input("Enter your move (1-9): ")
    if cell.isdigit() and 1 <= int(cell) <= 9:
      return int(cell) - 1

def is_valid_move(board, cell):
  if board[cell // 3][cell % 3] != 0:
    return False
  return True

def make_move(board, cell, player):
  board[cell // 3][cell % 3] = player

def check_winner(board, player):
  # Check rows
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == player:
      return True

  # Check columns
  for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] == player:
      return True

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] == player:
    return True

  if board[0][2] == board[1][1] == board[2][0] == player:
    return True

  return False

def game_over(board):
  for player in [1, 2]:
    if check_winner(board, player):
      return player

  if all(cell != 0 for row in board for cell in row):
    return -1  # Draw

  return 0  # Game not over yet

def main():
  board = create_board()
  player = 1

  while True:
    print_board(board)

    # Get user's move
    cell = get_user_input()

    # Make the move
    if not is_valid_move(board, cell):
      print("Invalid move!")
      continue

    make_move(board, cell, player)

    # Check if the game is over
    winner = game_over(board)
    if winner != 0:
      print_board(board)
      print("Player {} wins!".format(winner))
      break

    # Switch players
    player = 2 if player == 1 else 1

  if winner == -1:
    print_board(board)
    print("The game is a draw!")             
if __name__ == "__main__":
 main()
