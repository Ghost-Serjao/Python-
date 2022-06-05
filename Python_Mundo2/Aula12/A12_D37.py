numero = int(input('Digite um numero'))
print('''Escolha uma das bases para conversão: 
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{numero} convertido para binario é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('opção ivalida tente novamente')

















#ler um numero inteiro qualquer e peça para o usuario escolher a base de conversão
#binario
#octal 
#hexadecimal