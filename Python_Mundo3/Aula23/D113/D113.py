def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('Por favor, digite um númeor inteiro válido')
        else:
            return n

def leiafloat():
    while True:
        try:
            n = float(input('Digitte um número real: '))
        except (ValueError, TypeError):
            print('Por favor, digite um número real valido:  ')
        else:
            return n


num1 = leiaint()
num2 = leiafloat()

print('-'*20)
print(f'''Número inteiro:{num1}
número real:{num2} ''')
print('-'*20)
#Reescreva a função leiaint que fizemos no desafio 104
#Incluir possibilidade de digitar num do tipo invalido
#Criar uma função leiafloat com a mesma funcionalidade
#Ler numero inteiro e real