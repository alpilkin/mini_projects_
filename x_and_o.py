from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|", board[0][0], "|", board[0][1], "|", board[0][2], "|", sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|", board[1][0], "|", board[1][1], "|", board[1][2], "|", sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|", board[2][0], "|", board[2][1], "|", board[2][2], "|", sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if user_move < 1 or user_move > 9:
                print("Invalid input. Make it right.")
                continue
            if user_move not in board[0] and \
                    user_move not in board[1] and \
                    user_move not in board[2]:
                print("This space is already occupyed. Choose valid space")
                continue
            break
        except ValueError:
            print("Wrong format of an input. Please, correct your input")
            continue
        except:
            print("Something unexpected has happend...")

    # Update of the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == user_move:
                board[i][j] = "O"
    display_board(board)

    # Check if winning condition for User
    victory_for(board, "O")


def make_list_of_free_fields(board):
    free_space = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == "O" or board[row][column] == "X":
                continue
            else:
                free_space.append((row, column))
    return free_space


def victory_for(board, sign):
    winner_dictionary = {"X": "Computer won!", "O": "You won!"}

    # Check if it is a winner condition
    if board[0][0] == board[0][1] == board[0][2] == sign or \
            board[1][0] == board[1][1] == board[1][2] == sign or \
            board[2][0] == board[2][1] == board[2][2] == sign or \
            board[0][0] == board[1][1] == board[2][2] == sign or \
            board[0][2] == board[1][1] == board[2][0] == sign or \
            board[0][0] == board[1][0] == board[2][0] == sign or \
            board[0][1] == board[1][1] == board[2][1] == sign or \
            board[0][2] == board[1][2] == board[2][2] == sign:
        print(winner_dictionary[sign])
        exit()

    # Check if it is a "Draw"
    if make_list_of_free_fields(board) == []:
        print("It a draw... maybe next time...")
        exit()

    # Next turn
    if sign == "X":
        enter_move(board)
    else:
        draw_move(board)


def draw_move(board):
    # Computer move
    free_space = make_list_of_free_fields(board)
    if len(free_space) == 1:
        computer_move = 0
    else:
        computer_move = randrange(len(free_space) - 1)

    # Update of the board
    board[free_space[computer_move][0]][free_space[computer_move][1]] = "X"
    print("My turn:")
    display_board(board)

    # Check if winning condition for Computer
    victory_for(board, "X")


# Board creation
initial_board = []
initial_board.append([j for j in range(1, 4)])   # First row
initial_board.append([j for j in range(4, 7)])   # Second row
initial_board.append([j for j in range(7, 10)])  # Third row
initial_board[1][1] = "X"

print("""
Let's begin our little game...
My turn is first ))))
        """)
display_board(initial_board)
enter_move(initial_board)
