Input = input('Digite algo: ')

print('O texto pode ser um número.', Input.isnumeric())

print('O texto pode ser um número decimal.', Input.isdecimal())

print('O texto pode ser um alfabeto.', Input.isalpha())

print('O texto pode ser um alfanumérico.', Input.isalnum())
