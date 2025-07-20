sexo = ''
while not sexo in ('M', 'F'):
    sexo = str(input(f'Informe seu sexo [M/F]: ')).upper().strip()
    if sexo not in ('M', 'F'):
        print('Opção inválida, tente novamente.')
sexo_completo = 'Masculino' if sexo == 'M' else 'Feminino'
print(f'Resposta salva, sexo {sexo_completo}!')
