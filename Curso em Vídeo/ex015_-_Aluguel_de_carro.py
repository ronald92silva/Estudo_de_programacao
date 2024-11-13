dias = int(input('Quantos dias usou o carro?\n'))
km = int(input('Quantos km percorreu?\n'))

diaria = int(60)
km_rodado = float(0.15)

res = (dias * diaria) + (km * km_rodado)

print('O valor à pagar é de {}'.format(res))
