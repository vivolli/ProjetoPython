print('Sitema de Notas, seja bem-vindo!')
nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
media = round(nota1 + nota2)/2
print(f'Sua média é {media:.1f}.')
if media < 5:
    print('Você foi reprovado!')
elif 7 > media >= 5:
    print('Você foi reprovado!')
elif media >= 7:
    print('Voce foi Aprovado!')
