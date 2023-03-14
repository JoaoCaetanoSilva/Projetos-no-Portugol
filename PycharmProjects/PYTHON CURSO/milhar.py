i = int(input("Informe um numero: "))
u = i // 1 % 10
d = i // 10 % 10
c =i // 100 % 10
m = i // 1000 % 10
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))