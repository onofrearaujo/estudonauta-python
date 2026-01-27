continuar = 'S'
pessoas = []
while continuar == 'S':    
    pessoa = {}
    pessoa['nome'] = str(input('Digite o nome: ')).strip()
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa)

    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('Deseja cadastrar mais alguem? [S/N] ')).strip().upper()
print('~'*45)

print(f'- Foram cadastradas {len(pessoas)} pessoas')

soma_idades = 0
for p in pessoas:
    soma_idades += p['idade'] 

media_idades = soma_idades / len(pessoas)
print(f'- A media de idade do grupo é de {media_idades} anos')

mulheres = []
for m in pessoas:
    if m['sexo'] == 'F':
        mulheres.append(m['nome'])
print(f'- As mulheres cadastradas foram: {mulheres}')

print(f'- Lista das pessoas que estão acima da média')
for p in pessoas:
    print(f'=> Nome = {p["nome"]} - Sexo = {p["sexo"]} - Idade = {p["idade"]}')
