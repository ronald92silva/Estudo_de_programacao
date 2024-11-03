Input = input('Digite algo: ')

if Input.isnumeric():
    print('O texto pode ser um número.', Input.isnumeric())

if Input.isdecimal():
    print('O texto pode ser um número decimal.', Input.isdecimal())

if Input.isalpha():
    print('O texto pode ser um alfabeto.', Input.isalpha())

if Input.isalnum():
    print('O texto pode ser um alfanumérico.', Input.isalnum())
