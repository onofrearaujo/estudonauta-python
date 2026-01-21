vetor = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(valor)
    vetor.append(linha)
print('-=' * 30)

for linha in vetor:
    for valor in linha:
        print(f'[ {valor} ]', end='')       
    print()
