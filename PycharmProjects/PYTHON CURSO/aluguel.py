km = float(input('Quantos Km foram rodados com o carro? R: '))
dias = int(input('Por quantos dias esse carro foi alugado? R: '))

resultado1 = km * 0.15
resultado2 = dias * 60
resultado3 = resultado1 + resultado2

km_ajustando = f' {km:_.0f}'
km_ajustado = km_ajustando.replace('.', '.').replace('_', '.')

resultado_ajustando = f' {resultado3:_.2f}'
resultado_ajustado = resultado_ajustando.replace('.', ',').replace('_', '.')

print(f'Voce andou:{km_ajustado} Km, por {dias} dias, entao terá que pagar:{resultado_ajustado}')