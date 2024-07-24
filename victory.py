# MODULE 4
import random
import datetime
import locale
from datetime import datetime

num_to_text_genitive = {
    1: "первого",
    2: "второго",
    3: "третьего",
    4: "четвёртого",
    5: "пятого",
    6: "шестого",
    7: "седьмого",
    8: "восьмого",
    9: "девятого",
    10: "десятого",
    11: "одиннадцатого",
    12: "двенадцатого",
    13: "тринадцатого",
    14: "четырнадцатого",
    15: "пятнадцатого",
    16: "шестнадцатого",
    17: "семнадцатого",
    18: "восемнадцатого",
    19: "девятнадцатого",
    20: "двадцатого",
    21: "двадцать первого",
    22: "двадцать второго",
    23: "двадцать третьего",
    24: "двадцать четвёртого",
    25: "двадцать пятого",
    26: "двадцать шестого",
    27: "двадцать седьмого",
    28: "двадцать восьмого",
    29: "двадцать девятого",
    30: "тридцатого",
    31: "тридцать первого"
}

month_to_text_genitive = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}


celebrities = [
    ("Альберт Эйнштейн", "14.03.1879"),
    ("Махатма Ганди", "02.10.1869"),
    ("Нельсон Мандела", "18.07.1918"),
    ("Мэрилин Монро", "01.06.1926"),
    ("Джон Ф. Кеннеди", "29.05.1917"),
    ("Мартин Лютер Кинг-младший", "15.01.1929"),
    ("Принцесса Диана", "01.07.1961"),
    ("Элвис Пресли", "08.01.1935"),
    ("Одри Хепберн", "04.05.1929"),
    ("Стив Джобс", "24.02.1955")]

def get_date_of_birth_str(celebrity):
    input_dob_str = input(f'Введите "dd.mm.yyyy" когда родил(ся)/(ась) {celebrity[0]} ')
    if(input_dob_str.index('.') > 0 and len(input_dob_str) == 10):
        return input_dob_str
    else:
        print('Неправильный формат! Вводите дату в формате "dd.mm.yyyy".')
        return ''
    
def print_cursive_date_from_str(date_str):
    if(date_str[:1] == '0'):
        day_str = num_to_text_genitive[int(date_str[1:2])]
    else:
        day_str = num_to_text_genitive[int(date_str[:2])]
    if(date_str[3:4] == '0'):
        month_str = month_to_text_genitive[int(date_str[4:5])]
    else:
        month_str = month_to_text_genitive[int(date_str[3:5])]
    return day_str + ' ' + month_str + ' ' + date_str[6:] + ' года'
    

count_right_answer = 0
total_questions = 0
max_celebraties_for_game = 5

random_celebrities = random.sample(celebrities, max_celebraties_for_game)

total_questions = len(random_celebrities)

greeting = 'Играем! Викторина на знание года рождения знаменитости!'
print(greeting)

play_again = True
while play_again:
    for celebrity in random_celebrities:
        if(get_date_of_birth_str(celebrity) == celebrity[1]):
            count_right_answer += 1
            print('Отлично!')
        else:
            print('Неправильный ответ!')
            print(f'Нв самом деле: {celebrity[0]} родился(ась) {print_cursive_date_from_str(celebrity[1])}')

    score = (count_right_answer*100)/total_questions
    score_negative = ((total_questions - count_right_answer)*100)/total_questions
    print(f'Ваш процент правильных ответов: {score}')
    print(f'Ваш процент неправильных ответов: {score_negative}')
    print(f'Всего правильных ответов: {count_right_answer} из {total_questions}')
    print(f'Всего неправильных ответов: {total_questions - count_right_answer} из {total_questions}')
    print('Если хотите сыграть еще введите 1, если нет, то 0 ')
    repeat_str = input('Итак, введите ваш ответ: ')
    if(repeat_str.isnumeric() and repeat_str == '0'):
        play_again = False
    else:
        print(greeting)
        count_right_answer = 0
        
print('Игра закончена! Спасибо, что играли!')

