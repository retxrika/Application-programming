def get_num_before_twenty(digit):
    return {
        0: "",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать"
    }[digit]

def get_num_after_twenty(firstDigit):
    return { 
        0: "",
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто"
    }[firstDigit]

def get_hundreds(firstDigit):
    return {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот"
    }[firstDigit]

def parse_three_digit(num): 
    parse_two_digit(num)
    num //= 100
    numStr.append(get_hundreds(num % 10))

def parse_two_digit(num):
    if (num % 100 >= 20):
        numStr.append(get_num_before_twenty(num % 10))
        num //= 10
        numStr.append(get_num_after_twenty(num % 10))
        num //= 10
    else:
        numStr.append(get_num_before_twenty(num % 100))

def get_thousand_with_correct_end(lastTwoDigit):
    if lastTwoDigit > 20:
        lastTwoDigit %= 10

    if lastTwoDigit == 1:
        return "тысяча"
    elif lastTwoDigit >= 2 and lastTwoDigit <= 4:
        return "тысячи"
    else:
        return "тысяч"

def get_correct_case_ruble(lastTwoDigit):
    if lastTwoDigit > 20:
        lastTwoDigit %= 10

    if lastTwoDigit == 1:
        return "рубль"
    elif lastTwoDigit >= 2 and lastTwoDigit <= 4:
        return "рубля"
    else:
        return "рублей"

def change_case(num):
    for i in range(len(num)):
        if num[i] == "один":
            num[i] = "одна"
            break
        elif num[i] == "два":
            num[i] = "две"
            break

while(True):
    try:
        num = int(input("Введите сумму для выдачи: "))
    except:
        print("ERROR: Неверно введена сумма! Попробуйте ещё раз...")
        continue
    if num < 1 or num > 999999:
        print("ERROR: Введенная сумма выходит за диапазон! Попробуйте ещё раз...")
        continue
    break
    
numStr = []

isThousand = isChangeCase = False

if (num >= 1000):
    isThousand = True
    if ((num // 1000 % 10 == 1 or num // 1000 % 10 == 2) 
        and num // 1000 % 100 != 11 
        and num // 1000 % 100 != 12):
        isChangeCase = True

numStr.append(get_correct_case_ruble(num % 100))

while(num > 0):
    # Добавление слова тысяча со своим окончанием.
    if isThousand and num < 1000:
        numStr.append(get_thousand_with_correct_end(num % 100))
        
    # Парсинг трехзначного числа.
    if (num % 1000 >= 100):
        parse_three_digit(num)
    # Парсинг одно-двузначного числа.
    else:
        parse_two_digit(num)
    
    num //= 1000
        
numStr.reverse()

# Замена при необходимости падежа у окончания тысячи.
if isChangeCase:
    change_case(numStr)

print(' '.join(numStr).capitalize())







