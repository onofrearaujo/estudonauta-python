valor_casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite quanto você ganha de salário: '))
anos = int(input('Digite em quantos anos você quer pagar: '))

prestacao_mensal = valor_casa / (anos * 12)

minimo =  30/100 * salario


print(f'Para pagar uma casa no valor de R$ {valor_casa:.2f} em {anos} anos o valor das prestações será de R$ {prestacao_mensal:.2f} por mês')
if prestacao_mensal <= minimo:
    print('O emprestimo foi aprovado!!!')
else:
    print('O emprestimo foi negado!')
    