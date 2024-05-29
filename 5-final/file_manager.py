# Проверка существования файла
try:
    # Пробуем открывать файл для чтения
    with open('score/score.txt', 'r') as file:
        file.read()
# Если не получается, то
except Exception as error:
    # создаем файл
    with open('score/score.txt', 'w') as file:
        file.write('')


def load_data_from_file():
    names_list = []
    scores_list = []
 
    # Читаем файл
    with open('score/score.txt', 'r') as file:
        # Каждую новую строку файла делаем элементом списка
        lines = file.read().split("\n") # name1#3, name2#5, ...

        # Извлекаем имена и рекорды из файла
        for line in lines:
            # Если не пустая строка
            if line != '':
                # Добавляем имя во временный список
                names_list.append(
                    line.split("#")[0]
                )
                # Добавляем рекорды во временный список
                scores_list.append(
                    line.split("#")[1]
                )
    return names_list, scores_list


def show_score():
    # Загружаем все данные из файла
    names_list, scores_list = load_data_from_file()
    
    print('\n' + 'ТАБЛИЦА ИГРОКОВ')    
    
    if len(names_list) < 1:
        print('.....пусто.....')
        return

    print('----------------')
    for i in range(len(names_list)):
        print(f'Игрок: {names_list[i].capitalize()} --- {scores_list[i]} побед(ы)')
    print()


def update_score_file(current_name, score):
    # Загружаем все данные из файла
    names_list, scores_list = load_data_from_file()
    
    # Добавляем рекорды игроку или создаем нового
    is_player_exist = False
    # Перебираем по индексам всех игроков во временном списке
    for i in range(len(names_list)):
        # Если найден текущий игрок
        if names_list[i] == current_name.lower():
            # Увеличиваем ему рекорд
            scores_list[i] = int(scores_list[i]) + score
            is_player_exist = True
    # Если игрок не найден
    if not is_player_exist:
        # Добавляем игрока+рекорд во временный список
        names_list.append(current_name.lower())
        scores_list.append(score)
    # Обновляем файл с рекордами
    with open('score/score.txt', 'w') as file:
        # Перебираем временный список игроков по индексам
        for i in range(len(names_list)):
            # Формируем строку вида имя#рекорд + перенос на следующую строку
            string_line = f'{names_list[i]}#{scores_list[i]}' + '\n'
            # Записываем строку
            file.write(string_line)

