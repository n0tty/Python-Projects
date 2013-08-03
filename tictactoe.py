#!/usr/bin/python

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#Greetz
def greet():
  print \
  """
  TIC TAC TOE by n0tty\n
  legendtanoybose@gmail.com
  http://the-bose.com
  
__________                     
\\______   \\ ____  ______ ____  
 |    |  _//  _ \\/  ___// __ \\ 
 |    |   (  <_> )___ \\\\  ___/ 
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/ 
  """

#Instructions
def instruct():
  """Game instructions."""
  print \
  """
  Your move, 0 to 8:
  
  0|1|2
  -----
  3|4|5
  -----
  6|7|8
  """

#yes or no
def ask_yes_no(question):
  """Ask a yes or no question."""
  response = None
  while response not in ("y","n"):
    response = raw_input(question).lower()
  return response

#ask input
def ask_number(question, low, high):
  """Ask for a number within a range."""
  response = None
  while response not in range(low, high):
    response = int(raw_input(question))
  return response

#Set human and computer pieces
def pieces():
  """Determine if player or comp goes first."""
  go_first = ask_yes_no("Do you require the first move? (y/n): ")
  if go_first == "y":
    print "\nThen take the first move. You will need it."
    human = X
    computer = O
    print computer
  else:
    print "\nk, I will go first..."
    human = O
    computer = X
    print computer
  return computer, human

#initialize empty board
def new_board():
  """Create new game..."""
  board = []
  for square in range(NUM_SQUARES):
    board.append(EMPTY)
  return board

#display the game board
def display_board(board):
  """Display game board on screen."""
  print "\n\t", board[0], "|", board[1], "|", board[2]
  print "\t", "----------"
  print "\n\t", board[3], "|", board[4], "|", board[5]
  print "\t", "----------"
  print "\n\t", board[6], "|", board[7], "|", board[8], "\n"

#see if valid move
def legal_moves(board):
  """Create list of legal moves."""
  moves = []
  for square in range(NUM_SQUARES):
    if board[square] == EMPTY:
      moves.append(square)
  return moves

#winner
def winner(board):
  """Determine the game winner."""
  WAYS_TO_WIN = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
  for row in WAYS_TO_WIN:
    if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
      winner = board[row[0]]
      return winner
    if EMPTY not in board:
      return TIE

#human's chance
def human_move(board, human):
  """Get Human move."""
  legal = legal_moves(board)
  move = None
  while move not in legal:
    move = ask_number("Where would you move? (0-8): ",0,NUM_SQUARES)
    if move not in legal:
      print "\nAlready Occupied cell. Fool\n"
    print "FINE..."
    return move

#computer's chance
def computer_move(board, computer, human):
  """Make comp move."""
  board = board[:]
  BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
  print "I shall take square number "
  for move in legal_moves(board):
    board[move] = computer
    if winner(board) == computer:
      print move
      return move
    board[move] = EMPTY
  for move in legal_moves(board):
    board[move] = human
    if winner(board) == human:
      print move
      return move
    board[move] = EMPTY
  for move in BEST_MOVES:
    if move in legal_moves(board):
      print move
      return move

#switch turns
def next_turn(turn):
  """Switch turns."""
  if turn == X:
    return O
  else:
    return X

#congrat message
def congrat_winner(the_winner, computer, human):
  """Congo winner."""
  if the_winner != TIE:
    print the_winner, "won!\n"
  else:
    print "It is a TIE!\n"
  if the_winner == computer:
    print "Artificial Intelligence beats human intelligence again\n"
  elif the_winner == human:
    print "Humans are cheaters... I will be BACK for my VENGENCE human!\n"
  elif the_winner == TIE:
    print "Lucky this time... next time you won't get so close\n"

#main function
def main():
  instruct()
  computer, human = pieces()
  turn = X
  board = new_board()
  display_board(board)
  print computer, "goes to computer\n", human, "goes to Human\n"
  while not winner(board):
    if turn == human:
      move = human_move(board, human)
      board[move] = human
    else:
      move = computer_move(board, computer, human)
      board[move] = computer
    display_board(board)
    turn = next_turn(turn)
    print turn, " has to play"
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#start of prog
greet()
main()
raw_input("\n\nPress enter key to quit.")
