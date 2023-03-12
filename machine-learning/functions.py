import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def formatacao_texto(texto):
    text = 'Taxa de acerto do algoritmo: {:.2f}%'.format(texto * 100)
    return text


def read_table(url):
    return pd.read_csv(url)


def percentagem_acerto(x, y):
    fim = len(x) * 0.75
    comeco = int(fim)
    SEED = 20
    treino_x, treino_y, teste_x, teste_y = train_test_split(x,
                                                            y,
                                                            random_state=SEED,
                                                            test_size=0.25,
                                                            stratify=y,
                                                            )

    treino_x = x[:comeco]
    treino_y = y[:comeco]
    teste_x = x[comeco:]
    teste_y = y[comeco:]

    text = 'Treinairemos com {} elementos e testaremos com {} elementos'
    print(text.format(len(treino_x), len(teste_x)))

    modelo = LinearSVC()
    modelo.fit(treino_x, treino_y)
    previsoes = modelo.predict(teste_x)
    acc = accuracy_score(teste_y, previsoes)
    print(formatacao_texto(acc))
