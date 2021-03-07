test_number = [1234, 5555, 333]  #must to see 10, 15, 9

for number in test_number:
    number_sum = 0
    while number:
        number_sum += number % 10
        number = number // 10
    print(number_sum)