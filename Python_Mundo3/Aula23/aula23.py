#Tratamento de erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b 
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

#Mensagem personalizada do erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b 
except Exception as erro:
    print(f'Probrema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

#Varios except
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b 
except (ValueError, TypeError) : #Botar () se for mais de um tipo de erro
   print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiou não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
