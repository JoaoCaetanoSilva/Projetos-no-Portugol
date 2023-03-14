real = float(input('Quanto reais voce tem? R$: '))
dolar = real / 3.27
if dolar < 1.0:
    print('Com {:.2f} reais voce compra {:.2f} cents.'.format(real, dolar))
else:
    print('Com {:.2f} reais voce compra {:.2f} dolares.'.format(real, dolar))