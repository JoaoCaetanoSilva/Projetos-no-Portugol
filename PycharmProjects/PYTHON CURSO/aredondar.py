from math import ceil, floor

num = float(input('Numero: '))
if num > 0.5:
    print('Aredondando pra cima dá: {}'.format(ceil(num)))
else:
    print('Aredondando pra baixo dá: {}'.format(floor(num)))
# /
# n1 = int(input('valor 1: '))
# a = n1 + 1
# b = n1 - 1
# print('Valor: {}'.format(n1) + '\nvalor acima: {}'.format(a) + '\nvalor abaixo: {}'.format(b))