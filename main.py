from board import Board
import re


def parse_move_command(parse_command):
    pattern = r"move ([A-H][1-8]) ([A-H][1-8])"
    match = re.match(pattern, parse_command, re.IGNORECASE)
    if match:
        from_value = match.group(1)
        to_value = match.group(2)
        return from_value, to_value
    else:
        print("Неверный формат команды - move")


def parse_possible_moves_command(parse_command):
    pattern = r"possible moves ([A-H][1-8])"
    match = re.match(pattern, parse_command, re.IGNORECASE)
    if match:
        value = match.group(1)
        return value
    else:
        print("Неверный формат команды - possible moves")


board = Board()
command = ""
while command != "exit":
    board.print_board()
    print("Команды:")
    print("exit -> выход \nmove <from> <to> -> Ход из клетки <from> в клетку <to>")
    print("possible moves <position>")
    command = str(input())
    if command[:4] == "move":
        move_from, move_to = parse_move_command(command)
        board.move(move_from, move_to)
    if command[:14] == "possible moves":
        board.print_piece_possible_moves(parse_possible_moves_command(command))
        print("Нажмите Enter для продолжения")
        input()
    else:
        print("Нет такой команды")
        print("Нажмите Enter для продолжения")
        input()
