# Créé par t.hausmann, le 14/05/2024 en Python 3.7
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_data = iris.data[:][iris.target != 2] # on conserve les étiquettes 0 et 1
iris_target = iris.target[:][iris.target != 2]






## Paramétrage réseau de neurones





def test(iris_data, iris_target):
    # récupération des données

    # découpage des données
    X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target,
    test_size=0.3, random_state=None)

    # normalisation des données X_train et X_test
    # objet scaler - mise à l'échelle des données a comme attributs min/max de chaque
    # colonne de X_train
    scaler = MinMaxScaler(feature_range=(0, 1), copy=False)
    X_train_scl = scaler.fit_transform(X_train)
    X_test_scl = scaler.transform(X_test)

    pmc = MLPClassifier(hidden_layer_sizes = (6,6), max_iter = 500 , learning_rate_init
    = 0.01)
    pmc.fit(X_train_scl, y_train)

    return pmc.score(X_test_scl, y_test)


lst_score = []
n = range(100)
for i in n:
 lst_score.append(round(100 * test(iris_data, iris_target), 2))
plt.plot (n, lst_score, "b.-", label="scores")
plt.legend()
plt.show()