def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param notas: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situacao
    :return: dicionario com varias informações sobre a situacao da turma
    """
    valores = {}
    valores['total'] = len(notas)
    valores['maior'] = max(notas)
    valores['menor'] = min(notas)
    valores['media'] = sum(notas) / len(notas)

    if sit:
        if valores['media'] >= 7:
            situacao = 'BOA'
        elif valores['media'] >= 5:
            situacao = 'RAZOAVEL'
        else:
            situacao = 'RUIM'
        valores['situacao'] = situacao
    return valores


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
