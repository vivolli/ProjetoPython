palavras = ('eduardo', 'sophia', 'nome', 'bom dia', 'eu te amo', 'prazer', 'sabor', 'estudar', 'tentar', 'fazer', 'certo',
            'conseguir', 'desistir', 'gratis', 'praticar','desejar', 'planejar', 'programador', 'developer', 'sonho', 'amor')
vogais = 'aeiou'
for listatem in palavras:
    vogais_encontradas = []
    for letras in listatem:
        if letras in vogais:
            vogais_encontradas.append(letras)
    print(f'Na palavra {listatem.upper()} existem as vogais: {', '.join(vogais_encontradas)}')
