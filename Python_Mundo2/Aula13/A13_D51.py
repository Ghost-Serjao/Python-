primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print(f'{c}', end='->')
print('ACABOU')
    








#Ler o primeiro termo e a razão de uma progressão aritimetica
#no final mostre os 10 primeiros termos dessa progressão