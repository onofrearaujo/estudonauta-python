nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

print(f'Com as notas {nota_1:.1f} e {nota_2:.1f}, A nota média desse aluno é {media:.2f}')
if media < 5:
    print('REPROVADO')
elif media <= 6.9:
    print('RECUPERAÇÃO')
else:   
    print('APROVADO')
    