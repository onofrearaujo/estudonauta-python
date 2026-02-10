def metade(preco):
    return preco / 2

def dobro(preco):
    return preco * 2

def aumentar(preco, porcentagem):
    porcento = porcentagem / 100
    resultado = porcento * preco + preco
    return resultado


def moeda(preco, sigla='R$'):
    return f'{sigla}{preco:.2f}'.replace('.', ',')
