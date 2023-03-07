import sys
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}


def print_board(board):
    print(the_board['top-L']+'|'+the_board['top-M']+'|'+the_board['top-R'])
    print("-+-+-")
    print(the_board['mid-L']+'|'+the_board['mid-M']+'|'+the_board['mid-R'])
    print("-+-+-")
    print(the_board['bot-L']+'|'+the_board['bot-M']+'|'+the_board['bot-R'])
    print("-+-+-")


def check():
    if (the_board['top-L']== 'X') and (the_board['top-M'] == 'X') and (the_board['top-R'] == 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-L']== 'X') and (the_board['mid-L']== 'X') and (the_board['bot-L'] == 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-L']== 'X') and (the_board['mid-M']== 'X') and (the_board['bot-R'] == 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['mid-L']== 'X') and (the_board['mid-M']== 'X') and (the_board['mid-R']== 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['bot-L']== 'X') and (the_board['bot-M']== 'X') and (the_board['bot-R']== 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-R']== 'X') and (the_board['mid-R']== 'X') and (the_board['bot-R']== 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-R'] == 'X') and (the_board['mid-M']== 'X') and (the_board['bot-L']== 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-M'] == 'X') and (the_board['mid-M']== 'X') and (the_board['bot-M']== 'X'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-L']== 'O') and (the_board['top-M'] == 'O') and (the_board['top-R'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['top-L'] == 'O') and (the_board['mid-L'] == 'O') and (the_board['bot-L'] == 'O'):
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if (the_board['top-L'] == 'O') and (the_board['mid-M'] == 'O') and (the_board['bot-R'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['mid-L'] == 'O') and (the_board['mid-M'] == 'O') and (the_board['mid-R'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['bot-L'] == 'O') and (the_board['bot-M'] == 'O') and (the_board['bot-R'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['top-R'] == 'O') and (the_board['mid-R'] == 'O') and (the_board['bot-R'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['top-R'] == 'O') and (the_board['mid-M'] == 'O') and (the_board['bot-L'] == 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if (the_board['top-M'] == 'O') and (the_board['mid-M']== 'O') and (the_board['bot-M']== 'O'):
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    else:
        return


turn = 'X'
count = 0
while count < 9:
    check()
    print_board(turn)
    move = input("It's Now turn for {0}, Move on which space? ".format(turn))
    if the_board[move] == " ":
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
            count = count + 1
        else:
            turn = 'X'
            count = count + 1
    else:
        print("{0} is already occupied, Enter into other vacant position".format(move))








