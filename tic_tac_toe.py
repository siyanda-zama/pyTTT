
import random

def drawBoard(board):
    #this function prints the board

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def inputPlayerLetter():

    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print("\nDo you want to be X or O?")
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
#this function randomly chooses which player will go first
    if random.randint(2, 3) == 3:
        return 'player'
    else:
        return 'computer'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False
    print("\nDo you want to play again? (yes or no)")
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # Using bo instead of board and le instead of letter instead of typing as much.

    # Across the top:
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or \
    # Across the middle:
    (bo[4] == le and bo[5] == le and bo[6] == le) or \
    # Across the bottom:
    (bo[1] == le and bo[2] == le and bo[3] == le) or \
    # Down the left side:
    (bo[7] == le and bo[4] == le and bo[1] == le) or \
    # Down the middle:
    (bo[8] == le and bo[5] == le and bo[2] == le) or \
    # Down the right side:
    (bo[9] == le and bo[6] == le and bo[3] == le) or \
    # diagonal:
    (bo[7] == le and bo[5] == le and bo[3] == le) or \
    # diagonal:
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('\nWhat is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Return none if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Check if computer can win next move.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5
    # Move on one the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("\n\nWelcome to Tic Tac Toe!")
print("\n   |   |")
print(" " + "7" + " | " + "8" + " | " + "9")
print("   |   |")
print("-----------")
print("   |   |")
print(" " + "4" + " | " + "5" + " | " + "6")
print("   |   |")
print("-----------")
print("   |   |")
print(" " + "1" + " | " + "2" + " | " + "3")
print("   |   |")

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("\nThe " + turn + " will go first.")
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("\nHooray! You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("\nThe game is a tie!")
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("\nThe computer has beaten you! You lose.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("\nThe game is a tie!")
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

