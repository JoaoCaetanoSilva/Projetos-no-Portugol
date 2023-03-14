from math import sqrt, ceil, floor

num = int(input('Numero: '))
raiz = sqrt(num)
print('A raiz do numero: {} aredonda pra cima é: {}'.format(num, ceil(raiz)))
print('A raiz do numero: {} é: {:.2f}'.format(num, raiz))
print('A raiz do numero: {} aredonda pra baixo é: {}'.format(num, floor(raiz)))
