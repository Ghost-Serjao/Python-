frase = str(input('Digite uma frase: ')).strip().upper()
print(frase[:: -1])
if frase == frase[:: -1]:
    print('Essa frase é um palindromo.')
else:
    print('Essa frase não é um palindromo.')

#frase = "Mundo mundo vasto mundo"
#print(frase[::-1])








#Criar um progama que leia uma frase qualquer 
#e diga se ela é um palindromo
#fazer o progama tirar os espaços
#Ex: APOS A SOPA
