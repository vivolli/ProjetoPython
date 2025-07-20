numero = []
for peso in range(1,6):
    pessoas = float(input(f'Paciente {peso}ª digite seu peso: '))
    numero.append(pessoas)
print(f'O maior peso digitado foi {max(numero):.2f}Kg')
print(f'O menor peso digitado foi {min(numero):.2f}Kg')
#Usei o append para facilitar e diminuir as linhas