reta_1 = int(input('Digite o valor da reta 1: '))
reta_2 = int(input('Digite o valor da reta 2: '))
reta_3 = int(input('Digite o valor da reta 3: '))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print('As retas acima PODEM FORMAR Triângulo:', end = ' ')
    if reta_1 == reta_2 == reta_3:
        print('Equilátero')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Essas retas não podem formar um triangulo')
    