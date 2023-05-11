import sys
from sys import exit
board_list = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]


def board():
    print(f"{board_list[0]}|{board_list[1]}|{board_list[2]}")
    print(f"{board_list[3]}|{board_list[4]}|{board_list[5]}")
    print(f"{board_list[6]}|{board_list[7]}|{board_list[8]}")


def turns(current_player, winner):
    while winner is None:
        board_input = int(input("Choose a position from 1-9: "))
        board_list[board_input - 1] = current_player
        if current_player == "X":
            current_player = "Y"
        elif current_player == "Y":
            current_player = "X"

        board()
        if board_list[0] == board_list[1] == board_list[2] != "-":
            winner = board_list[0]
            print(f"{winner} wins!")
        elif board_list[3] == board_list[4] == board_list[5] != "-":
            winner = board_list[3]
            print(f"{winner} wins!")
        elif board_list[6] == board_list[7] == board_list[8] != "-":
            winner = board_list[6]
            print(f"{winner} wins!")
        elif board_list[0] == board_list[3] == board_list[6] != "-":
            winner = board_list[0]
            print(f"{winner} wins!")
        elif board_list[2] == board_list[4] == board_list[7] != "-":
            winner = board_list[2]
            print(f"{winner} wins!")
        elif board_list[3] == board_list[5] == board_list[8] != "-":
            winner = board_list[3]
            print(f"{winner} wins!")
        elif board_list[0] == board_list[4] == board_list[8] != "-":
            winner = board_list[0]
            print(f"{winner} wins!")
        elif board_list[2] == board_list[4] == board_list[6] != "-":
            winner = board_list[2]
            print(f"{winner} wins!")


def play():
    board()
    turns("X", None)


play()
