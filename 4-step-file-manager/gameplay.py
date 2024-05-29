from field_module import get_field
from constants import (
    EMPTY_CELL, # *
    ABC, # abc
    ABC_NUMS, # 123
    LETTER_TO_INDEX, # словарь с ключами-буквами и индексами-значениями
    WIN_LINE_O, # ['x', 'x', 'x']
    WIN_LINE_X, # ['o', 'o', 'o']
)

# Проверяет, правильно ли введен ход игрока
def check_turn(player_turn: str):
    # Если длина player_turn не 2, там могут быть варианты: 1, ккк..., пробел или пустота
    if len(player_turn) != 2:
        return False
    # Первый символ должен быть цифрой
    elif player_turn[0] not in ABC_NUMS:
        return False
    # Второй символ должен быть буквой
    elif player_turn[1:] not in ABC:
        return False
    
    return True

# Проверяет путая ли ячейка на игровом поле
def is_cell_free(player_turn: str): # 1a | 2b | 3c
    row = int(player_turn[0]) - 1
    col = LETTER_TO_INDEX[player_turn[1]]
    field = get_field() # [ ['*','*','*'], ['*','o','*'], ['x','*','*'] ]

    if field[row][col] == EMPTY_CELL:
        return True

    return False

# Проверяет победителя
def chech_win(player_x: str, player_o: str, field: list):
    # Изначально победитель пустой
    winner = None
    is_winner = False

    for i in range(3):
        # проверка рядов. После проверки победитель становится кто-то из игроков
        if field[i] == WIN_LINE_X:
            winner = player_x
            is_winner = True
        if field[i] == WIN_LINE_O:
            winner = player_o
            is_winner = True

    # проверка диагоналей. После проверки победитель становится кто-то из игроков
    if field[0][0] == field[1][1] == field[2][2] == 'x':
        winner = player_x
        is_winner = True
    if field[2][0] == field[1][1] == field[0][2] == 'x':
        winner = player_x
        is_winner = True
    if field[0][0] == field[1][1] == field[2][2] == 'o':
        winner = player_o
        is_winner = True
    if field[2][0] == field[1][1] == field[0][2] == 'o':
        winner = player_o
        is_winner = True

    # проверка стобцов. После проверки победитель становится кто-то из игроков
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == 'x':
            winner = player_x
            is_winner = True
        if field[0][i] == field[1][i] == field[2][i] == 'o':
            winner = player_o
            is_winner = True
    
    # проверка ничьи. После проверки победитель становится слово "ничья"
    if not is_winner:
        if EMPTY_CELL not in field[0] and \
            EMPTY_CELL not in field[1] and \
            EMPTY_CELL not in field[2]:

            winner = 'ничья'
   
    # Возврат результата
    if winner == 'ничья':
        return "Ничья!"
    # Кто-то из игроков победил
    elif winner == player_x or winner == player_o:
        return f"{winner.capitalize()} поебдил!"
    # Возвращаем пустоту и игра продолжается,
    # если не ничья и никто не выйграл
    return winner   
