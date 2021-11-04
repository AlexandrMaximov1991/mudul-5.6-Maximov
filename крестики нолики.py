# Пишем название игры
print(f'{"*" * 15} Игра на двоих в крестики нолики {"*" * 15}')

# Заводим переменную с типом "список" для изменения его в ходе игры
field = list(range(1, 10))

# Создаем функциюкоторая с помощью предыдущей переменной будет нам выводить игровое поле на экран
def draw_field(field):
    print('-' * 13)    # Для зрительной эстетики добавляем знаки -, |
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)

# Создаем функцию которая запрвшивать у пользователей ввод и проверять ввод на ошибки
def move_input(move_symbol):
    valid = False
    while not valid:
        move_ansver = input('На какую цифру поставить знак ' + move_symbol+ '?')
        try:
            move_ansver =int(move_ansver)               # в виде инных символов
        except:
            print(f'Вы уверены что ввели число от 1 до 9?\nПопробуйте еще раз! ')
            draw_field(field)
            continue
        if move_ansver >= 1 and move_ansver <= 9:                        # либо диапазона игрового поля
            if str(field[move_ansver -1]) not in "X0":   # так же проверяется занятость клетки
                field[move_ansver -1] =move_symbol       # если ввод пользователя прошел все проверки, то записываем его в переменную поля в элемент под номером на один меньше введенного, так как в Python счет начинается с нуля а поле начинается с единицы
                valid = True
            else:
                print(f'Данная клетка уже занята!\nПопробуйте еще раз! ') # если клетка занята, то выводится соответствующее сообщение
                draw_field(field)
        else:
            print(f'Вы ввели число вне диапазона игрового поля!\nПопробуйте еще раз! ') # так же выводится сообщение если ввод вне диапазона игрового поля
            draw_field(field)
# Создаем функцию выигрышных координат
def chek_win(field):
    win_coordinats = ((0, 1, 2), (3, 4, 5), (6, 7, 8),      # задаем переменную координат
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))
    for each in win_coordinats:
        if field[each[0]] == field[each[1]] == field[each[2]]:  # Цикл проверки координат
            return field[each[0]]
    return False

# Создаем главную функцию для игры
def game(field):
    count = 0  # задаем счетчик ходов
    win = False
    while not win:
        draw_field(field)
        if count % 2 == 0:      # если номер хода четный,
            move_input('X')     # то ходит "Х"
        else:                   # иначе
            move_input('0')     # ходит "0"
        count += 1              # с каждым ходом в счетчик добавляется единица
        if count > 4:           # послечетвертого хода, начинаем проверять символы "Х" и "0" на выиграшную комбинацию
            symbol = chek_win(field)  # если получаем совпадения
            if symbol:
                draw_field(field)
                print(symbol, ' Выиграл! Поздравляю!!! ')   # Выводим соответствующее сообщение
                win = True
                break
        if count ==9:                       # если ходов равняется девять, а выиграшной комбинации нет, то ничья
            draw_field(field)
            print('Победила дружба!!!')    # выводсообщения о ничьей
            break

game(field)

print(input('Для выхода нажмите "ENTER" клавишу!'))