def dobro(preco, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)

def metade(preco, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)

def aumentar(preco, porcentagem, formatar=False):
    res = preco + (porcentagem / 100 * preco)
    return res if not formatar else moeda(res)

def diminuir(preco, porcentagem, formatar=False):
    res = preco - (porcentagem / 100 * preco)
    return res if not formatar else moeda(res) 

def moeda(preco, sigla='R$'):
    return f'{sigla}{preco:.2f}'.replace('.', ',')

def resumo(preco, porcento_aumento, porcento_desconto):
    titulo('RESUMO DO VALOR')

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{porcento_aumento}% de aumento: \t{aumentar(preco, porcento_aumento, True)}')
    print(f'{porcento_desconto}% de desconto: \t{diminuir(preco, porcento_desconto, True)}')
    linha()

def linha(tam = 40):
    print('-' * tam)
    return tam

def titulo(txt):
    largura = linha()
    print(txt.center(largura))
    linha()
