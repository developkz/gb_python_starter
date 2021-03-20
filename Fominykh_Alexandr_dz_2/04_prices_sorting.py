"""
1. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

2. Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).

3. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

product_prices = [53.14, 18.7, 20.33, 11.45, 13.67, 94.7, 7.0, 4.2, 64.1, 33.8]

#  1
print(f'Вывести на экран эти цены через запятую в одну строку:')
for i in product_prices:
    product_prices_split = str(i).split('.')
    product_prices_integer = int(product_prices_split[0])
    product_prices_after_dot = int(product_prices_split[1])
    print(f'{product_prices_integer:02} руб {product_prices_after_dot:02} коп', end=", ")

print(' ')

#  2
print(f'Вывести цены, отсортированные по возрастанию:')
for i in sorted(product_prices):
    product_prices_split = str(i).split('.')
    product_prices_integer = int(product_prices_split[0])
    product_prices_after_dot = int(product_prices_split[1])
    print(f'{product_prices_integer:02} руб {product_prices_after_dot:02} коп', end=", ")

print('')
print(f'Доказать, что объект списка после сортировки остался тот же: \n{product_prices}')

#  3
product_prices_desc = sorted(product_prices, reverse=True)
print(f'Цены пяти самых дорогих товаров по возрастанию(минимальный код): \n{sorted(product_prices_desc[:5])}')

print(f'Цены пяти самых дорогих товаров по возрастанию(подробно):')
for i in sorted(product_prices_desc[:5]):
    product_prices_split = str(i).split('.')
    product_prices_integer = int(product_prices_split[0])
    product_prices_after_dot = int(product_prices_split[1])
    print(f'{product_prices_integer:02} руб {product_prices_after_dot:02} коп', end=", ")
