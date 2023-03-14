resultado = 2 + 3
print("Resultado:", resultado)

resultado += 2
print("Resultado:", resultado)

#///

# a = int(input("Valor: "))
# b = int(input("Valor: "))
# soma = a + b
# print("valores: {}".format(soma))
# print(f"valores: {soma}")

#///

print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distância em metros percorrida pelo patinete? ")
tempo = input("Quantos minutos o patinete demorou para percorrer essa distância? ")
velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))