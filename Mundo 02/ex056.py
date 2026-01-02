soma_idades = 0

nome_homem = None
idade_homem = 0

mulheres = 0

quantidade = 4
for i in range(quantidade):
    print(f" ------ {i + 1}ª PESSOA ------")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
  
    soma_idades += idade

    if sexo == 'M' and idade > idade_homem:
        idade_homem = idade 
        nome_homem = nome
    
    if sexo == 'F' and idade < 20:
        mulheres += 1
  
    print('')
  
media_idades = soma_idades / quantidade

print(f'A media de idade do grupo é de: {media_idades:.1f} anos')

if nome_homem:
    print(f'O nome do homem mais velho é {nome_homem} com {idade_homem} anos')
else:
    print('Não foi informado nenhum homem.')
  
print(f'A quantidade de mulheres com menos de 20 anos é {mulheres}')
