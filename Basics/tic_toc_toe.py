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
    if the_board['top-L'] and the_board['top-M'] and the_board['top-R'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['top-L'] and the_board['mid-L'] and the_board['bot-L'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['top-L'] and the_board['mid-M'] and the_board['bot-R'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['mid-L'] and the_board['mid-M'] and the_board['mid-R'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['bot-L'] and the_board['bot-M'] and the_board['bot-R'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['top-R'] and the_board['mid-R'] and the_board['bot-R'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['top-R'] and the_board['mid-M'] and the_board['bot-L'] == 'X':
        print_board(turn)
        print("Congrats X, You won the Game")
        sys.exit()
    if the_board['top-L'] and the_board['top-M'] and the_board['top-R'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['top-L'] and the_board['mid-L'] and the_board['bot-L'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['top-L'] and the_board['mid-M'] and the_board['bot-R'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['mid-L'] and the_board['mid-M'] and the_board['mid-R'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['bot-L'] and the_board['bot-M'] and the_board['bot-R'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['top-R'] and the_board['mid-R'] and the_board['bot-R'] == 'O':
        print_board(turn)
        print("Congrats O, You won the Game")
        sys.exit()
    if the_board['top-R'] and the_board['mid-M'] and the_board['bot-L'] == 'O':
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
        print("{0} is already occupied, Enter into other left position".format(move))








