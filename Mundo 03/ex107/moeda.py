def metade(preco):
    return preco / 2

def dobro(preco):
    return preco * 2


def aumentar(preco, porcentagem):
    porcento = porcentagem / 100
    resultado = porcento * preco + preco
    return resultado 


def diminuir(preco, porcentagem):
    porcento = porcentagem / 100
    resultado = preco - (porcento * preco)
    return resultado
