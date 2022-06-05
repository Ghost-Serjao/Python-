ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], [media]])
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"N":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[1]}')
while True:
    resp2 = str(input('Quer saber a nota de quem? '))
    if resp2 == 999:
        print('Finalizando...')
        break
    if resp == ficha[0]:
        print(f'A notas de {ficha[0]} foram: {[1]} e {[2]}')
    if resp2 <= len(ficha) -1:
        print(f'Notas de {ficha[resp2][0]} são {ficha[resp2][1]}')




#Ler nome e duas notas de varios alunos 
#guardar numa lista composta 
#[[nome[notas]], [nome[notas]], [nome[notas]], [nome[notas]], [nome[notas]], [nome[notas]], [nome[notas]] ]
#no final mostre um boletin com a media de cada um
#permitir que o uso mostre as notas de cada aluno individualmente 