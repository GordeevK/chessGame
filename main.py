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
    white_king, black_king = board.get_kings()
    board.print_board()
    if board.get_color_move():
        if white_king.in_check(board):
            print("Белый король атакован")
        print("Ход белых")
    else:
        if black_king.in_check(board):
            print("Чёрный король атакован")
        print("Ход чёрных")
    print("Команды:")
    print("exit -> выход \nmove <from> <to> -> Ход из клетки <from> в клетку <to>")
    print("possible moves <position> -> Возможные ходы для фигуры на клетке <position>")
    command = str(input())
    if command[:4] == "move":
        move_from, move_to = parse_move_command(command)
        if board.print_piece_position(move_from) is None:
            print("Выбери фигуру")
            print("Нажмите Enter для продолжения")
            input()
        elif board.print_piece_position(move_from).is_white() == board.get_color_move():
            board.move(move_from, move_to)
        else:
            print("Не твоя очередь хода")
            print("Нажмите Enter для продолжения")
            input()
    elif command[:14] == "possible moves":
        board.print_piece_possible_moves(parse_possible_moves_command(command))
        print("Нажмите Enter для продолжения")
        input()
    else:
        print("Нет такой команды")
        print("Нажмите Enter для продолжения")
        input()
