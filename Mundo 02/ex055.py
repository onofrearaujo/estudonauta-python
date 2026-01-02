maior = 0
menor = 0
for i in range(3):
    peso = float(input(f'Digite o peso da {i + 1}ª pessoa KG: '))

    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
    
print(f'MAIOR PESO LIDO FOI: {maior:.2f}Kg')
print(f'MENOR PESO LIDO FOI: {menor:.2f}Kg')
  