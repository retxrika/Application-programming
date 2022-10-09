import os

# Выводит заголовок.
def print_header():
    os.system('cls')
    print('ПРОГРАММА ШИФРОВАНИЯ И РАСШИФРОВКИ ШИФРА ЦЕЗАРЯ\n' +
          '===============================================\n')

# Собирает данные пользователя.
def get_data():
    print_header()
    str = input('Введите строку (латиница/кириллица): ')
    while True:
        try:
            shift = int(input('Введите сдвиг (число): '))
        except:
            print('Ошибка: неверно введенно значение! Попробуйте ещё раз...')
            continue

        return (str, shift)

# Выводит результат.
def print_result(str):
    print_header()
    print("Готовая строка:", str)

# Возвращает корректное значение в случае 
# сдвига заходящего за пределы алфавита.
def get_correct_value(c, start_c, end_c, shift):
    while ord(c) + shift < ord(start_c):
        shift = shift + 1 + ord(end_c) - ord(start_c)
    while ord(c) + shift > ord(end_c):
        shift = shift - 1 - ord(end_c) + ord(start_c) 
    
    return chr(ord(c) + shift)

# Возвращает зашифрованную/расшифрованную строку.
def get_encryption(str, shift):
    enc = []
    for c in str:
        if c >= 'a' and c <= 'z':
            enc.append(get_correct_value(c, 'a', 'z', shift))
        elif c >= 'A' and c <= 'Z':
            enc.append(get_correct_value(c, 'A', 'Z', shift))
        elif c >= 'а' and c <= 'я':
            enc.append(get_correct_value(c, 'а', 'я', shift))
        elif c >= 'А' and c <= 'Я':
            enc.append(get_correct_value(c, 'А', 'Я', shift))
        else:
            enc.append(c)
    return ''.join(enc)

# Ввод пользователя строки и сдвига.
str, shift = get_data()
# Шифровка.
result = get_encryption(str, shift)
# Вывод результата.
print_result(result)



    
    