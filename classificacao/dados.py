import csv

def carregar_acessos():
    #dados = []
    #marcacoes = []
    x = []
    y = []
    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    #descarta a primeira linha, os cabecalhos
    next(leitor)
    for home,como_funciona,contato,comprou in leitor:
        dado = [int(home),int(como_funciona),int(contato)]
        x.append(dado)
        y.append(int(comprou))
    return x, y


