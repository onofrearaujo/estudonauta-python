peso = float(input('Digite o peso em Quilos: '))
altura = float(input('Digite a altura em Metros: '))

imc = peso / altura**2

print(f'\nO seu IMC: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')