valores = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(n)
    valores.append(linha)

print('-=' * 30)
soma_pares = 0
soma_terceira = 0
maior_valor = valores[1][0]
for p, linha in enumerate(valores):
    for pos, v in enumerate(linha):
        print(f'[ {v} ]', end='')
        if v % 2 == 0:
            soma_pares += v
        if pos == 2:
            soma_terceira += v 
        if p == 1 and v > maior_valor:
            maior_valor = v
    print()
print('-=' * 30)

print(f'A soma dos valores pares é {soma_pares}.')

print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {maior_valor}.')
