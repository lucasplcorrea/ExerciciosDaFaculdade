# Importando bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset Iris
data = pd.read_csv('/home/lucas/Documents/GitHub/ExerciciosDaFaculdade/2024 - Inteligencia Artificial/Agenda 06 - NP2/dataset-iris.csv', header=None)
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Dividir o dataset em X (features) e y (target)
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

# Configuração de Validação Cruzada com Stratified K-Fold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Função para calcular métricas de avaliação
def evaluation_metrics(y_true, y_pred, model_name):
    print(f"\nMétricas para o modelo {model_name}:")
    print("Acurácia:", accuracy_score(y_true, y_pred))
    print("Precisão:", precision_score(y_true, y_pred, average='weighted'))
    print("Revocação:", recall_score(y_true, y_pred, average='weighted'))
    print("F1 Score:", f1_score(y_true, y_pred, average='weighted'))
    print("\nMatriz de Confusão:")
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(y), yticklabels=np.unique(y))
    plt.xlabel("Predito")
    plt.ylabel("Real")
    plt.title(f"Matriz de Confusão para {model_name}")
    plt.show()

# Modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
y_pred_knn = cross_val_predict(knn, X, y, cv=cv)
evaluation_metrics(y, y_pred_knn, "KNN")

# Modelo SVM
svm = SVC(kernel='linear')
y_pred_svm = cross_val_predict(svm, X, y, cv=cv)
evaluation_metrics(y, y_pred_svm, "SVM")

# Comparação de Acurácia entre KNN e SVM usando cross_val_score
acc_knn = cross_val_score(knn, X, y, cv=cv, scoring='accuracy')
acc_svm = cross_val_score(svm, X, y, cv=cv, scoring='accuracy')
print(f"\nAcurácia média KNN: {np.mean(acc_knn):.2f}")
print(f"Acurácia média SVM: {np.mean(acc_svm):.2f}")
