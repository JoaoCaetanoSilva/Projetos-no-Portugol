import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

salario = float(input('Qual o salario? '))
calculo = salario + (salario * 15 / 100)
print('O salario é: {}, mas com o ajuste do novo cargo subirá para: {}'.format(locale.currency(salario, grouping=True), locale.currency(calculo, grouping=True)))