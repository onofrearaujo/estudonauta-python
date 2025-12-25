import random

nome_1 = input('Digite o nome do aluno 1: ')
nome_2 = input('Digite o nome do aluno 2: ')
nome_3 = input('Digite o nome do aluno 3: ')
nome_4 = input('Digite o nome do aluno 4: ')

lista = [nome_1, nome_2, nome_3, nome_4]

sorteado = random.choice(lista)

print(f'O aluno sorteado para apagar o quadro foi {sorteado}')
