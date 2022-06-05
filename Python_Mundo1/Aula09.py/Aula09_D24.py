#ler o nome da cidade e dizer se começa ou não com a palvra 'santo'
cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')