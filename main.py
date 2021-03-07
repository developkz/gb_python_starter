# Два числа 20 и 22. Нужно вычислить их сумму.

print(20 + 22)

EURO_RUB = 72
penny_in_pocket = int(input('Input number of penny: '))

# control_penny_in_pocket = 1345
# print('Two pockets:', type(penny_in_pocket), type(control_penny_in_pocket))

rub_in_pocket = penny_in_pocket / 100
euro_in_pocket = rub_in_pocket // EURO_RUB
cents_in_pocket = rub_in_pocket % EURO_RUB
print(f'Euro: {euro_in_pocket}, cent: {cents_in_pocket}')
