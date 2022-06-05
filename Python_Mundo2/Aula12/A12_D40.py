print('Coloque suas notas abaixo')
nota1 = float(input('NOTA 1:'))
nota2 = float(input('NOTA 2: '))
media = (nota1 + nota2) /2 
if media <= 4.9:
    print(f'Sua media foi {media}\nVocê esta de REPROVADO.\nBoa sorte na proxima.')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua media foi {media}\nVocê esta de RECUPERAÇÃO.\nESTUDE.')
elif media >= 7.0:
    print(f'Sua media foi {media}\nVocê foi Aprovado.\nPARABENS!')









#Ler duas notas e calcular sua media 
#media entre 5.0 ou menos : reprovado
#media entre 5.0 e 6.9 : recuperação
#media 7.0 ou superior : aprovado