nomedapessoa = str(input('Digite seu nome completo: ')).strip()
resultado = nomedapessoa.split()
print(f'Seu primeiro nome é: {resultado[0]}')
print(f'Seu ultimo nome é: {resultado[len(resultado)-1]}')
#nesse ex, o resuldado na 4 linha diz respeito ao comprimento (len), no caso
#{resultado[len(resultado)-1]},
#ficando assim, o {resultado [do comprimento (do resultado) -1]}
