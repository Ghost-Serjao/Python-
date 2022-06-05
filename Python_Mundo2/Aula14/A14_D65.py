resp = 'S'
soma = quant = media = maior = menor = 0 
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0] #[0] considerar so a °1 letra
media = soma / quant 
print(f'Você digitou {quant} numeros e a media foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')









#ler varios numeros inteiros
#no final mostre a media entre todos 
#os valores e qual foi o maior e menor
#deve perguntar se o usuario quer continuar ou não
