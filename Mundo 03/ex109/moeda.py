def metade(preco, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)

def dobro(preco, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)

def aumentar(preco, porcentagem, formatar=False):
    res = preco + (porcentagem / 100 * preco) 
    return res if not formatar else moeda(res)

def diminuir(preco, porcentagem, formatar=False):
    res = preco - (porcentagem / 100 * preco)
    return res if not formatar else moeda(res)

def moeda(preco, sigla='R$'):
    return f'{sigla}{preco:.2f}'.replace('.', ',')
