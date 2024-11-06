salario = float(input('Seu salário:\n'))

reajuste = float(input('Reajuste de %:\n'))

print('Seu salário passa a ser de R$ {:.2f}'.format(salario * (1 + (reajuste/100))))
