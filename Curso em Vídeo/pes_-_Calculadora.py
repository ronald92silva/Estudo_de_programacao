print('CALCULADORA\n')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite o segundo: '))
op = input('Digite qual operação deseja realizar: \n+ (soma)\n- (subutrair)\n/ (dividir)\n* (multiplicar)\n')

if op == '+':
    print(num1 + num2)
if op == '-':
    print(num1 - num2)
if op == '/':
    print(num1 / num2)
if op == '*':
    print(num1 * num2)
