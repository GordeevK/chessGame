from board import Board
import re

def parse_move_command(command):
    pattern = r"move (\d+),(\d+) (\d+),(\d+)"
    match = re.match(pattern, command)
    if match:
        from_value = (int(match.group(1)), int(match.group(2)))
        to_value = (int(match.group(3)), int(match.group(4)))
        return from_value, to_value
    else:
        print("Неверный формат команды - move")

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

