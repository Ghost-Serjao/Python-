print('Triangulo')
r1 = float(input('Lado 1: '))
r2 = float(input('Lado 2: '))
r3 = float(input('Lado 3: '))
if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os lados acima podem fromar um trinagulo', end='') 
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else: #Não precisa perder tempo testando se essa for a ultima opção que restar (deixar a mais dificil por ultimo)
        print("Isosceles") 
else:
    print('Os lados acima não podem formar um triangulo.')




#Refazer desafio 35
#mostrar que tipo de triangulo sera formado
#equilatero:todos os lados iguais
#isosceles:dois lados iguais
#escaleno:todos os lados diferentes 