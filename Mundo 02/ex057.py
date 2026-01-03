nome = str(input('Digite o seu nome: ')).strip()

sexo = ' '

while sexo not in ('M', 'F'):
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo not in ('M', 'F'):
        print('Digite um sexo válido')
        
print('=== DADOS ===')
print(f'Nome: {nome}')
print(f'Sexo: {sexo}')
