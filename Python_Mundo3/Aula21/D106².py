def ajuda(com):
    help(com)

def titulo(msg):
    tam = len(msg)
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!')

#Sem cores pq o VS code n suporta 