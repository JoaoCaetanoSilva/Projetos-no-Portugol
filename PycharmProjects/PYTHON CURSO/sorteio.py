from random import randint
aleatorio = randint(1, 4)
if aleatorio == 1:
    print('Marcos apagara')
if aleatorio == 2:
    print('Ana apagara')
if aleatorio == 3:
    print('João apagara')
if aleatorio == 4:
    print('Katarine apagara')

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacao de trabalhos será: {}'.format(lista))