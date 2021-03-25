"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus(*args):
    result_dict = {}
    for el in args:
        cur_letter = el[0]
        if cur_letter in result_dict.keys():
            current_list = result_dict[cur_letter]
        else:
            current_list = []
            result_dict[cur_letter] = current_list

        current_list.append(el)

    return result_dict


def sorted_thesaurus(*args):
    result_dict = {}
    sorted_dict = {}
    for el in args:
        cur_letter = el[0]
        if cur_letter in result_dict.keys():
            current_list = result_dict[cur_letter]
        else:
            current_list = []
            result_dict[cur_letter] = current_list

        current_list.append(el)

    for el_sorted in sorted(result_dict.keys()):
        sorted_dict[el_sorted] = result_dict[el_sorted]

    return sorted_dict


print('Неотсортированный словарь:')
res_list = thesaurus("Иван", "Мария", "Петр", "Илья", "Павел", "Владимир", "Василий")
print(res_list)

print('Отсортированный словарь:')
sorted_res_list = sorted_thesaurus("Иван", "Мария", "Петр", "Илья", "Павел", "Владимир", "Василий")
print(sorted_res_list)