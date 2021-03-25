"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""


def num_translate_adv(number):
    if number in translations:
        print(translations[number])
    elif number[0].istitle():
        number = number.lower()
        if number in translations:
            print(translations[number].capitalize())
    else:
        return None


translations = {'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}

input_number = input('Введите числительное от 0 до 10. Например "one": ')
num_translate_adv(input_number)
