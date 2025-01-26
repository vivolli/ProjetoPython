from datetime import date
ano = int(input('''Digite o ano para verificação. 
Digite 1 para considerar o ano da maquina: '''))
if  ano == 1:
    ano = date.today().year
if  ano % 400 == 0:
    print(f'{ano} é um Ano Bissexto!')
else:
   if ano % 100 == 0:
    print(f'{ano} nao é um Ano Bissexto!')
   else:
    if ano % 4 == 0:
        print(f'{ano} é um Ano Bissexto')
    else:
        print(f'{ano} nao é um Ano Bissexto!')