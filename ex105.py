def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    dicio['total'] = len(valores)
    dicio['maior'] = max(valores)
    dicio['menor'] = min(valores)
    dicio['média'] = sum(valores) / len(valores)
    if sit is True:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio


resp = notas(6.5, 7.5, 10, 6.5, sit=True)
print(resp)