# global_name = ''
# def print_user_name(name, day='Monday', num_of_prints=1):
#     """
#     Func for beautiful print:
#     Два позиционных аргумента
#     :param name: локальная переменная внутри функции
#     :param num_of_prints: локальная переменная внутри функции
#     :return:
#     """
#     list_of_users = []
#     for i in range(num_of_prints):
#         list_of_users.append(f'Hello, dear {name}! Today is {day}')
#     return list_of_users
#
#
# day = 'Tuesday'
# name_0 = 'Katya'
# name_1 = 'Basil'
# name_2 = 'Vasil'
# name_3 = 'Kirill'
#
# print_user_name(name_1, num_of_prints=2)  # позиционные аргументы
# print_user_name(name_0)  # позиционные и именнованные аргументы
# print_user_name(num_of_prints=3, name=name_2, day='Sunday')  # именнованные аргументы
# print_user_name(name_3, day)
# lena_list = print_user_name('Lena')
# print(lena_list)


def user_info(**kwargs):
    """
    Функция возвращает кортеж значений из:
    Можно ли допустить к работе?
    Оповещение следующего отдела.
    was_ill - болел ли короной
    Пример возвращаемых данных (True), (False, KFC)
    :return:
    """

    if kwargs['temperature'] > 36.6 and kwargs['was_ill']:
        print('Go to work')
        return (False)
    elif kwargs['temperature'] > 36.6 and not kwargs['was_ill']:
        print('User is ill')
        return (False, kwargs['work_place'])
    else:
        print('Go to work сопливый')
        return (True)


user_dict = {'name': 'Basil',
             'age': 25,
             'temperature': 36.6,
             'work_places': ['KFC', 'Burger King', 'Кофемания'],
             'was_ill': False,
             'work_place': 'Bookshop'}

def update_work(user_dict, new_place):
    user_dict['work_places'].append(new_place)
    user_dict['work_place'] = user_dict['work_places'][-1]
    return user_dict


print(user_info(**user_dict))
print(update_work(user_dict, 'EHS'))

# def user_info(*args):
#     print(args[1], type(args))
#     for arg in args:
#         arg = str(arg) + '!'
#         print('We have this info:', arg)
#
#
# print(*user_info_data)
# # user_info(user_info_data)  # передает один аргумент - список
# user_info('Vasil', 25, 36.7, 'KFC')
# # print(user_check('Basil', 38.4, 'KFC', False))
# # print(user_check('Vasil', 38.4, 'Bookshop', True))
# # print(user_check('Kirill', 36.6, 'KFC', True))
# # print(user_check('Katya', 36.6, 'KFC', False))

'''
user_dict = {'name': 'Basil',
             'age': 25,
             'temperature': 36.6,
             'work_places': ['KFC', 'Burger King', 'Кофемания']}

print(user_dict['work_places'])
user_dict['temperature'] = 37.8
user_dict['is ill'] = True
user_dict['work_places'].append('Moscow City')
print(user_dict)
# print(user_dict['work_places'])
del user_dict['work_places']
print(user_dict.get('work places'))
print(user_dict.get('education'))
print(dir(user_dict))
'''