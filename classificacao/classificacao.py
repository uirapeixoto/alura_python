# eh gordinho? tem perninha curta? faz au au?
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
marcacoes = [1, 1, 1, -1, -1, -1]
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
#marcacoes que cabem no modelo
modelo.fit(dados, marcacoes)
#variavel para o teste
teste = [misterioso1, misterioso2, misterioso3]
#a biblioteca tenta adivinha (prediser) que tipo de animal está no teste
print(modelo.predict(teste))
#testando os resultados
marcacoes_teste = [-1,1,-1]
resultado = modelo.predict(teste)
print(resultado - marcacoes_teste)
diferencas = resultado - marcacoes_teste
acertos = [d for d in diferencas if d==0]
total_acertos = len(acertos)
total_elementos = len(teste)
taxa_acertos = 100.0 * total_acertos / total_elementos
print(total_elementos)
print(total_acertos)
print(taxa_acertos)
print(acertos)