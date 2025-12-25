salario = float(input('Digite o salário do funcionário R$ '))

if salario > 1250:
    porcento = 10
    aumento = porcento / 100 * salario
else:
    porcento = 15
    aumento = porcento / 100 * salario

print(f'Você teve um aumento de {porcento} e ganhou R$ {aumento} a mais no seu salario de R$ {salario} totalizando R$ {salario + aumento}')