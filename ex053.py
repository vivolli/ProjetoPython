user_answer = str(input('Digite uma frase: ')).lower().strip().replace(' ','')
inverso = user_answer[::-1]
if len(user_answer) == len(inverso):
    if inverso == user_answer:
        print('PALINDROMO!')
    else:
        print('NAO É UM PALINDROMO')
print(f'O inverso de {user_answer} é {inverso}')