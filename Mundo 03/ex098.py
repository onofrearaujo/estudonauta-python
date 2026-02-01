def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('~' * 35)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
    else:
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
    print('FIM')
    
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)

