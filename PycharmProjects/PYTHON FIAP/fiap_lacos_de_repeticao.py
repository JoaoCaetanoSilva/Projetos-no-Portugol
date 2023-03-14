# Laço condicional enquanto faça:

# opcao = input("Digite S ou N: ")
#
# while opcao != "s" and opcao != "n":
#     print("Voce digitou um valor invalido, por favor digite-o novamente.")
#     opcao = input("Digite S ou N: ")
#
# print("Voce digitou correto")

# Laço pós condicional faça enquanto:

# soma = 0
#
# while True:
#     num = int(input("Digite um numero: "))
#     if num <= 10:
#         soma = num + soma
#     else:
#         break
# print("A soma é: ", soma)

# Laço contador:

# num = int(input("Digite 5 numeros: "))
#
# maior = num
# for cont in range(1, 5, 1):
#     num = int(input("Digite o proximo: "))
#     if num > maior:
#         maior = num
# print("O maior numero é: ", maior)

# 3 laços:

# num1 = int(input("Escreva o 1 numero: "))
# num2 = int(input("Escreva o 2 numero: "))

# for count in range(num1, num2 + 1, 1):
#     print(count, "")

# or

# while num1 <= num2:
#     print(num1, " ")
#     num1 = num1 + 1

# or

# while True:
#     print(num1, " ")
#     num1 = num1 + 1
#     if num1 > num2:
#         break