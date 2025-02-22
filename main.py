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
        input()


board = Board()
command = ""
while command != "exit":
    board.print_board()
    print("Команды:")
    print("exit -> выход \nmove <from> <to> -> Ход из клетки <from> в клетку <to>")
    command = str(input())
    if command[:4] == "move":
        move_from, move_to = parse_move_command(command)
        board.move(move_from, move_to)
    else:
        print("Нет такой команды")
        input()

