valores = []

for i in range(5):
    n = int(input('Digite um número: '))
    
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('O número foi adicionado ao final da lista')
    else:
        for pos, valor in enumerate(valores):
            if n <= valor:
                valores.insert(pos, n)
                print(f'O número foi adicionado a posição {pos} uma posição')
                break
            
print(f'Os valores digitados em ordem foram: {valores}')
