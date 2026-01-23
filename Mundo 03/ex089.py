ficha = []

continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    
    continuar = None
    while continuar not in ('S', 'N'):
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar not in ('S', 'N'):
            print('Entrada inválida.')

print('-' * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-' * 30)

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print('-' * 30)
    aluno = int(input('Deseja visualizar as notas de qual aluno? (999 para interromper): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno >= 0 and aluno < len(ficha):
        print(f'Notas do de {ficha[aluno][0]} são {ficha[aluno][1]}')
    else:
        print('Este aluno não está na lista')
print('>>> VOLTE SEMPRE <<<')
        
