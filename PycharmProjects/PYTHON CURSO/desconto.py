preco = float(input('Qual o preco? '))
calculo = preco - (preco * 5 / 100)
print('O valor total é: {:,.2f}, mas com o desconto de 5% o valor cairá para: {:,.2f}'.format(preco, calculo))