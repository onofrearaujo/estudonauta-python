maior_dezoito = 0
mulheres_menores = 0
homens = 0

while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    
    idade = int(input('Idade: '))
    
    if idade >= 18:
        maior_dezoito += 1
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    if sexo == 'M':
        homens += 1
        
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
    
    print('-' * 30)
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        
    if continuar == 'N':
        break
    
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {maior_dezoito}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menores} mulheres com menos de 20 anos')
    
    
