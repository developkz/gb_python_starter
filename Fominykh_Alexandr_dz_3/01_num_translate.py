"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""

def num_translate(number):
    if number in numbers_to_translate:
        print(numbers_to_translate[number])
    else:
        return None


numbers_to_translate = {'one': 'один',
                        'two': 'два',
                        'three': 'три',
                        'four': 'четыре',
                        'five': 'пять',
                        'six': 'шесть',
                        'seven': 'семь',
                        'eight': 'восемь',
                        'nine': 'девять',
                        'ten': 'десять'}

num_translate(input('Введите числительное от 0 до 10. Например "one": '))
