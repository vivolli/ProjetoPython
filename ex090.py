aluno = {}
aluno['nome'] = input('Digite seu nome: ').capitalize()
aluno['media'] = float(input(f'Sua media, {aluno['nome']}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] > 5 < 6.99:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('='*25)
print(f'''Aluno: {aluno['nome']}\nMédia: {aluno['media']}\nSituação: {aluno['situacao']}''')
print('='*25)
