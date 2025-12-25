salario_funcionario = float(input('Qual é o salário do Funcionário? R$'))
novo_salario = salario_funcionario + (15 / 100 * salario_funcionario)
print(f'Um funcionário que ganhava R${salario_funcionario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}')
