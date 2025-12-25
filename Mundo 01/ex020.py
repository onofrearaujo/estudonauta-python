from random import sample
nome_1 = str(input('Digite o nome do aluno 1: '))
nome_2 = str(input('Digite o nome do aluno 2: '))
nome_3 = str(input('Digite o nome do aluno 3: '))
nome_4 = str(input('Digite o nome do aluno 4: '))

lista = [nome_1, nome_2, nome_3, nome_4]

#shuffle(lista)

ordem_apresentacao = sample(lista, len(lista))

print(f'A ordem de apresentação é: {ordem_apresentacao}')
