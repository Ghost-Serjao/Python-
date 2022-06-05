print('Calculo IMC')
peso = float(input('digite seu peso(Kg): '))
altura = float(input('Digite sua altura(M): '))
imc = peso / altura ** 2
if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso ideial')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')













#calcuar imc (peso e altura)
#abaixo do peso 18.5
#entre 18.5 e 25 peso ideal 
# 25 ate 30 sobrepeso 
# 30 ate 40 obesdade 
# acima de 40 obesidade morbida