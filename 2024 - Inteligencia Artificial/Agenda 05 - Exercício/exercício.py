import csv
import math
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Defina o caminho do arquivo local
dataset_path = './dataset-iris.csv'

# Carregar o dataset a partir de um arquivo CSV
def carregar_dados(caminho):
    dados = []
    with open(caminho, newline='') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            atributos = list(map(float, linha[:4]))
            classe = linha[4]
            dados.append((atributos, classe))
    return dados

# Função para calcular a distância Euclidiana
def calcular_distancia(ponto1, ponto2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(ponto1, ponto2)))

# Função para prever a classe de uma instância com KNN
def prever_classe(dados_treino, nova_instancia, k):
    distancias = [(calcular_distancia(nova_instancia, instancia[0]), instancia[1]) for instancia in dados_treino]
    vizinhos = sorted(distancias, key=lambda x: x[0])[:k]
    classes_vizinhas = [vizinho[1] for vizinho in vizinhos]
    return Counter(classes_vizinhas).most_common(1)[0][0]

# Avaliar o KNN no dataset Iris
def avaliar_knn(dados, k):
    X = [instancia[0] for instancia in dados]
    y = [instancia[1] for instancia in dados]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    previsoes = [prever_classe(list(zip(X_train, y_train)), x, k) for x in X_test]
    return accuracy_score(y_test, previsoes)

# Executando o KNN
dados = carregar_dados(dataset_path)
k = 3  # Defina o valor de K
acuracia = avaliar_knn(dados, k)
print(f"Acurácia do KNN com k={k}: {acuracia:.2f}")
