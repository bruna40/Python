from sklearn.svm import LinearSVC

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 = porco, 0 = cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1, 1, 1, 0, 0, 0]

model = LinearSVC()

model.fit(dados, classes)

animal_misterioso = [1, 1, 1]
teste = model.predict([animal_misterioso])
print(teste)

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

teste_misterioso = [misterio1, misterio2, misterio3]

print(model.predict(teste_misterioso))
# resposta esperada: [0, 1, 1]