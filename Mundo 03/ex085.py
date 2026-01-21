valores = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i+1}° valor: '))    
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

if valores[0]:
    valores[0].sort()
    print(f'Os valores pares são: {valores[0]}')
else:
    print('Você não digitou nenhum número par')

if valores[1]:
    valores[1].sort()
    print(f'Os valores impares são: {valores[1]}')
else:
    print('Você não digitou nenhum número impar')
