from constants import TURN_TEXT, LETTER_TO_INDEX, NICKNAME_INPUT
from gameplay import check_turn, is_cell_free, chech_win
from field_module import (
    get_field,
    set_cell_in_field,
    show_field,
)


# Меняет переменную с текущим игроком O --> X или наоборот
def change_player():
    global player_name, player_value

    # Проверка имени текущего игрока
    if player_name == nikname_1:
        player_name = nikname_2
        player_value = 'o'

    elif player_name == nikname_2:
        player_name = nikname_1
        player_value = 'x'


# START GAME

# Выводим доску лидеров

print('\n' + 'НОВАЯ ИГРА!' + '\n')

# Запрашиваем НИК для х
nikname_1 = input(NICKNAME_INPUT.format(1)).capitalize()
# Запрашиваем НИК для о
nikname_2 = input(NICKNAME_INPUT.format(2)).capitalize()

# Переменная для текущего игрока. Чередуется после каждого хода
player_name = nikname_1
# Переменная для Х или О для текущего игрока
player_value = 'x'


while True:
    # Выводится поле
    show_field()
    
    # Запрос хода (х | о)
    player_turn = input(TURN_TEXT.format(player_name, player_value)).lower()

    # Проверяем 1-ый и 2-ой символы на правильность
    if check_turn(player_turn=player_turn) is False:
        continue

    # Проверяем пустая ли клетка, куда игрок хочет походить
    if not is_cell_free(player_turn=player_turn):
        continue

    # Ход игрока
    set_cell_in_field(
        row=int(player_turn[0]) - 1, # a | b | c
        col=LETTER_TO_INDEX[player_turn[1]], # 1 | 2 | 3
        player=player_value # x | o
    )

    # Проверка выйгрыша
    winner = chech_win(
        player_x=nikname_1.lower(),
        player_o=nikname_2.lower(),
        field=get_field()
    )

    # Если кто-то выиграл, то выводим победителя и завершаем игру
    if winner is not None:
        show_field()
        print('\n' + winner)
        break

    # Смена игрока
    change_player()

# Определяем победителя
    # сохраняем результаты
