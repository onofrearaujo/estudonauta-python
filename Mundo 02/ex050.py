soma = 0
cont = 0
for c in range(6):
    n = int(input(f'Digite o {c+1}° número: '))
  
    if n % 2 == 0:
        soma += n
        cont += 1
    
if cont > 0 and soma > 0:
    print(f'Foram digitados {cont} números PARES e a soma deles é {soma}')
elif cont > 0:
    print(f'Foram digitados {cont} números PARES, mas todos são zero')
else:
    print('Você não digitou nenhum número par!')
