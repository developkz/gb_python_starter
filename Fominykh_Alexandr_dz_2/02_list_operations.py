"""
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку: в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
дополнить числа до двух разрядов нулём!
*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться.
"""

weather_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
plus_minus = '+-'
i = 0
result = ' '

for i in range(len(weather_lst)):
    if (weather_lst[i][0] in plus_minus) or ('0' <= weather_lst[i] <= '9'):
        if len(weather_lst[i]) == 1:
            weather_lst[i] = '0' + weather_lst[i]
            weather_lst[i] = '"' + weather_lst[i] + '"'
        if weather_lst[i][0] in plus_minus:
            weather_lst[i] = weather_lst[i][0::-1] + '0' + weather_lst[i][1::]
            weather_lst[i] = '"' + weather_lst[i] + '"'
        if len(weather_lst[i]) == 2 and weather_lst[i].isdigit():
            weather_lst[i] = '"' + weather_lst[i] + '"'
print(result.join(weather_lst))
