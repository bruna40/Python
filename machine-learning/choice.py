from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 = porco, 0 = cachorro
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0]

model = LinearSVC()

model.fit(treino_x, treino_y)

animal_misterioso = [1, 1, 1]
teste = model.predict([animal_misterioso])
# resposta esperada: [0]
print(teste)

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

testes_x = [misterio1, misterio2, misterio3]

teste_x = model.predict(testes_x)
treino_y = [0, 1, 1]

taxa_de_acerto = accuracy_score(treino_y, teste_x)


def formatacao_texto(texto):
    text = 'Taxa de acerto do algoritmo: {:.2f}%'.format(texto * 100)
    return text


print(formatacao_texto(taxa_de_acerto))
