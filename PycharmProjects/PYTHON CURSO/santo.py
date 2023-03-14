cidade = str(input("Em que cidade voce nasceu? ")).strip()
print(cidade[:5].upper() == 'SANTO')

nome = str(input("Qual seu nome? ")).strip()
print('Seu nome tem santo? {}'.format(('santo' in nome.lower())))