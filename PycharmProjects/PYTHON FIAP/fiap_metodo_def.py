# def horario(hora):
#     if hora >= 1 and hora < 6:
#         msg = ("MADRUGADA")
#     if hora >= 6 and hora <= 12:
#         msg = ("DIA")
#     if hora >= 13 and hora <= 18:
#         msg = ("TARDE")
#     if hora >= 19 and hora <= 24:
#         msg = ("NOITE")
#     else:
#         print("Valor invalido")
#     print(msg)
# horario(34)

# /

# def pi():
#     return 3.14159
#
# r = 5
# a = pi() * r ** 2
# print("A area do circulo com raio:", r, "é:", a)

# /

# def nota_valida(nota):
#     if nota >= 0 and nota <= 10:
#         return True
#     else:
#         return False
#
# nota1 = float(input("Digite a 1°nota: "))
# if (nota_valida(nota1)):
#     nota2 = float(input("Digite a 2°nota: "))
#     if (nota_valida(nota2)):
#         media = (nota1 + nota2) / 2
#         print("A media entre as notas {} e {} é: {}".format(nota1, nota2, media))
#     else:
#         print("Invalido")
# else:
#     print("Invalido")

x = 5
y = 10
if x != y:
    y = y + x
    x = x - y
x = y + 1
y = x + 1
print(f"x = {x} e y = {y}")