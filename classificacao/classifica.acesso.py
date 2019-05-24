from dados import carregar_acessos

x, y = carregar_acessos()

#primeiras 90 linhas
treino_dados = x[:90]
treino_marcacoes = y[:90]
#ultimas 9 linhas
teste_dados = x[-9:]
teste_marcacoes = y[-9:]

#print(teste_dados)
#rint(treino_marcacoes)

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_dados)
taxa_acertos = 100 * total_acertos / total_elementos
print(taxa_acertos)
print(total_elementos)
print(resultado)