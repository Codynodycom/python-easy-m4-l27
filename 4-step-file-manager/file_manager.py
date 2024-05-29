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
