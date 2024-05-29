from constants import (
    EMPTY_CELL,
    TOP_FIELD_CELLS,
    TOP_FIELD_LINE,
    MID_FIELD_LINE,
    BOTTOM_FIELD_LINE,
)


field = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*'],
]

# Возвращает текущее игровое поле field
def get_field():
    global field
    return field

# Выводит в теминал оформленное игровое поле
def show_field():
    global field

    i = 1
    print(TOP_FIELD_LINE)
    print(TOP_FIELD_CELLS)

    for line in field:
        print(MID_FIELD_LINE)
        print('|', i, end=" |  ")
        
        for cell in line:
            print(cell, ' | ', end=' ')

        i += 1
        print()

    print(BOTTOM_FIELD_LINE)


def set_cell_in_field(row: int, col: int, player: str):
    """
        функция устанавливает player_value в поле
        row - номер строки
        col - номер столбца
        player_value - значение игрока - Х или О
    """

    global field
    
    if field[row][col] == EMPTY_CELL:
        field[row][col] = player
        return True
    else: 
        return False
