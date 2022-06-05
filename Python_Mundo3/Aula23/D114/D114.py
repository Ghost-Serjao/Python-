import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('Não é possivel conectar ao site do PUDIM :(') 
else:
    print('O site do PUDIM ta on meu consagrado')


#Criar um codigo que teste se o site "PUDIM" esta acessivel no PC usado
