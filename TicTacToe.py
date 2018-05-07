"""There are 3 main conditions to be checked for declaring the winner
1) Check diagonally 
    a) in any given n by n square there will 2 diagonals
2) Check Horizontally for all the rows for the entire board
3) Check Vertically  for all the columns for the entire board"""

def win_check(board):
    width = len(board[0])
    height = len(board)

    # Horizontal
    for y in range(height):
        if board[y][0] != 0 and all(board[y][i] == board[y][0] for i in range(1, width)):
            return board[y][0]

    # Vertical
    for x in range(width):
        if board[0][x] != 0 and all(board[i][x] == board[0][x] for i in range(1, height)):
            return board[0][x]

    #Diagonals exists only if the board is square
    if width == height:
        #1st Diagonal
        if board[0][0] != 0 and all(board[i][i] == board[0][0] for i in range(1, width)):
            return board[0][0]
        #2nd Diagonal
        if board[0][-1] != 0 and all(board[i][-1 - i] == board[0][-1] for i in range(1, width)):
            return board[0][-1]
    return False

def prompt(question, check_func=lambda i: i.lower() == "y"):
    while True:
        value = check_func(input(question))
        if value is not None:
            return value

#Check positive values, if positive return val
def chk_pos(string):
    try:
        val = int(string)
        if val > 0: return val
    except ValueError:
        pass


def board_coord(board):
    def f(i):
        i = i.split(" ")
        if len(i) != 2: return
        x = chk_pos(i[0])
        y = chk_pos(i[1])
        if x is None or y is None: return
        if board[y - 1][x - 1] != 0: return
        return (x - 1, y - 1)
    return f

"""Print board"""
def display_board(board):
    def cell(value):
        if value == 0:
            return "  "
        elif value == 1:
            return "xx"
        elif value == 2:
            return "oo"
        raise ValueError("Invalid cell value: %r" % value)

    width = len(board[0])
    height = len(board)
    result = []

    result.append("     ")
    for i in range(width):
        result.append("%2d " % (i + 1,))
    result.append("\n")

    for y in range(height):
        result.append("    " + "+--" * width + "+\n") # separator
        result.append("%3d " % (y + 1,))
        for x in range(width):
            result.append("|" + cell(board[y][x]))
        result.append("|\n")
    result.append("    " + "+--" * width + "+")

    print("".join(result))


def play(board_size):
    board = [[0 for x in range(board_size[0])] for y in range(board_size[1])]
    #Number of turns played
    played_turn = 0
    #There cant be moves more than n * n
    while played_turn < board_size[0] * board_size[1] and not win_check(board)  :
        print("Player %d's (%s) turn is up!" % (played_turn % 2 + 1, ("xx", "oo")[played_turn % 2]))
        display_board(board)
        (x, y) = prompt("Please enter board coordinates to place your piece on.\nEnter 1 2 for 1st row 2nd column \n(Note) SPACE SHOULD BE SPECIFIED BEWTWEEN VALUES:\n ", board_coord(board))
        board[y][x] = played_turn % 2 + 1
        played_turn += 1

    print("**** GAME OVER ****")
    display_board(board)

    winning_player = win_check(board)
    if not winning_player:
        print("The game was a tie!")
    else:
        print("Player %d (%s) won!" % (winning_player, ("xx", "oo")[winning_player - 1]))


if __name__ == "__main__":
    board_size = (prompt("Please enter tic-tac-toe board width:  ", chk_pos),
                  prompt("Please enter tic-tac-toe board height: ", chk_pos))
    play(board_size=board_size)
    while prompt("Would you like to continue? Type (y/n) "):
        board_size = (prompt("Please enter tic-tac-toe board width:  ", chk_pos),
                      prompt("Please enter tic-tac-toe board height: ", chk_pos))
        play(board_size=board_size)