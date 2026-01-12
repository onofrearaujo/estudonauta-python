expressao = str(input('Digite a expressão: '))

pilha = []
for c in expressao:
    if c == '(':
        pilha.append(c)   
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
            break

if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
