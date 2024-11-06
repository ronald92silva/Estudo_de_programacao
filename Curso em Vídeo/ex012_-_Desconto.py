valorInicial = float(input('Valor do produto:\n'))
valorDesconto = float(input('Desconto %:\n'))

desconto = valorDesconto / float(100)

print('R$ {:.2f} com {}"%" de desconto fica R$ {:.2f}'.format(valorInicial,valorDesconto, valorInicial * (1 - desconto)))
