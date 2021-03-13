"""
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки
"""

input_number = [1, 2, 4, 6, 11, 18]
for number in input_number:
    if number == 1:
        print(number, 'процент')
    elif number == 2 or number == 3 or number == 4:
        print(number, 'процента')
    else:
        print(number, 'процентов')