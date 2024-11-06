real = float(input('Quantos reais você tem?\n'))

dolar = 3.27

print('Você pode comprar US$ {} dolares. Sobrou R$ {:.2f} reais '.format(real // dolar, real % dolar))
