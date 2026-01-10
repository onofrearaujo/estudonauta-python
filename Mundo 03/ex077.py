palavras = ('aprender', 'programar', 'linguagem', 'python', 'notebook', 
            'computador', 'vscode', 'programador', 'estudo', 'futuro', 
            'palavra', 'mundo', 'programa', 'programacao', 'matematica')

for palavra in palavras:
    encontradas = ''
    for letra in palavra.lower():
        if letra in 'aeiou':
            encontradas += f' {letra}'
    print(f'Na palavra {palavra} temos:{encontradas}', )
