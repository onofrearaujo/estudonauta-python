from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do angulo: '))

angulo_radiano = radians(angulo)

print(f'--- DADOS PARA ANGULO DE {angulo}°---')
print(f'Seno: {sin(angulo_radiano):.2f} \nCos: {cos(angulo_radiano):.2f} \nTangente: {tan(angulo_radiano):.2f}')
