sair = False
soma = cont = 0
while not sair:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        sair = True
    else:
        soma += n
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
