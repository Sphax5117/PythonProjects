# Créé par pc, le 17/04/2024 en Python 3.7
# -*- coding utf-8 -*-
# implémentation d'un perceptron

import numpy as np
import matplotlib.pyplot as plt
import random

# ouverture du fichier contenant les données
iris_data = np.load("iris_data.npy")
# préparation des données
# liste d'index de 0 à 99
n = range(len(iris_data))
# tirage au sort de 75% des indexes pour le train
train_idx = random.sample(n, int(len(iris_data)*.75))
# le reste des indexes pour le test (non mélangés)
test_idx = [i for i in n if i not in train_idx]
# on remplie les arrays X_train et y_train avec les valeurs de iris_data
# aux indexes de train_idx
X_train = iris_data[train_idx, 0:2]
y_train = iris_data[train_idx, 2].astype(int)
# idem pour X_test et y_test avec test_idx
X_test = iris_data[test_idx, 0:2]
y_test = iris_data[test_idx, 2].astype(int)
# normalise les coordonnées entre [0, 1]
min_x1 = min(X_train[:, 0])
max_x1 = max(X_train[:, 0])
min_x2 = min(X_train[:, 1])
max_x2 = max(X_train[:, 1])
for i in X_train :
 i[0] = (i[0] - min_x1) / (max_x1 - min_x1)
 i[1] = (i[1] - min_x2) / (max_x2 - min_x2)
for i in X_test :
 i[0] = (i[0] - min_x1) / (max_x1 - min_x1)
 i[1] = (i[1] - min_x2) / (max_x2 - min_x2)


# PARAMETRES DU PERCEPTRON
epochs = 100
eta = 0.01

# FONCTION ACTIVATION
def activation (s) :
    return np.heaviside(s,0)

# SOMME PONDÉRÉE
def entrainement (epochs, eta, X_train, y_train) :
    """ entrainement du perceptron
        # arguments et données :
            epochs(int) nbr d'iterations du calcul des poids
            eta(float) taux d'apprentissage
            X_train(ndarray) donnees d'apprentissage
            y_train(ndarray) étiquette des données d'apprentissage
        # return
            poids(ndarray) ajustes
            biais(float64) ajuste
    """
    poids = [0.0,0.0]
    biais = 0.0
    # boucle d'iteration d'ajustement des poids et du biais
    for j in range (epochs) :
        # a chaque iteration on parcourt les donnees d'apprentissage
        for i in range(len(X_train)):
            s = np.dot(poids, X_train[i]) + biais                         # calcule la somme ponderee !! Avec des matrices
            y_predict = activation(s)         # lance la fonction d'activation
            erreur = y_train[i] - y_predict                     # calcule l'erreur
            #  mise a jour des poids et du biais
            poids += erreur * eta * X_train[i]
            biais += erreur * eta
    return poids, biais



essai_train = entrainement(epochs, eta, X_train, y_train)




 ############### TEST DU PERCEPTRON             ##################
# DONNÉES D'ENTRÉES DE TEST

# PRÉDICTION DU PERCEPTRON


def predict (poids,biais,X_test,y_test) :
    """ predit y_test avec les poids et le biais ajustes
        # arguments, données
            poids(ndarray) ajustes
            biais(ndarray) ajuste
            X_test(ndarray) donnees de test
            y_test(ndarray) étiquette des données de test
        # return
            list_test(list(tuple)) couple (y_test, y_predict)
            % d'erreur
    """
    s = np.dot(X_test, poids) + biais              # calcule en une fois toutes les sommes pondérées
    y_prediction = activation(s)      # calcule en une fois toutes les prédictions
    erreur = 0
    list_test = []
    for i in range (len(y_test)) :
        if y_prediction[i] != y_test[i] :
            erreur += 1
        list_test.append((y_test[i], y_prediction[i]))
    return list_test, erreur/len(X_test)*100

essai_test = predict(essai_train[0], essai_train[1], X_test, y_test)


########## FRONTIERE             ##################
# DONNÉES GLOBALES
X_data = np.concatenate((X_train, X_test), axis = 0)

def frontiere (poids, biais, X_data) :
    """ calcule les 2 coordonnees du segment de droite qui separe les données
        en deux ensembles
        # parametres :
            poids(ndarray) ajustes
            biais(float) ajuste
        # donnees :
            X_train(ndarray) donnees d'apprentissage
        # return
            les 2 tuples de coordonnees du segment 'frontiere' pour plt
    """

    x11 = min(X_train[:, 0])
    x12 = max(X_train[:, 0])
    w0, w1, w2 = biais, poids[0], poids[1]
    a = -w1/w2
    b = -w0/w2
    x21 = a * x11 + b
    x22 = a * x12 + b
    return (x11, x12),(x21, x22)

droite_frontiere = frontiere(essai_train[0], essai_train[1], X_train)

#    AFFICHAGE DES DONNEES   #############################
plt.scatter(X_train[y_train == 0][:,0], X_train[y_train == 0][:,1], s=15, marker='.', color='g', label= "X_train")
plt.scatter(X_train[y_train == 1][:,0], X_train[y_train == 1][:,1], s=15, marker = "+", color = 'r', label= "X_train")
plt.scatter(X_test[y_test == 0][:,0], X_test[y_test == 0][:,1], s=20, marker='^', color = 'g', label= "X_test")
plt.scatter(X_test[y_test == 1][:,0], X_test[y_test == 1][:,1], s=20, marker='^', color = 'r', label= "X_test")
plt.plot(droite_frontiere[0], droite_frontiere[1], "b-", label="frontière")
plt.axis([min(X_data[:, 0]) - 0.2, max(X_data[:, 0]) + 0.2, min(X_data[:, 1]) - 0.2, max(X_data[:, 1]) + 0.2])
plt.grid()
plt.legend(title = f"exactitude : {100 - essai_test[1]}%")
plt.show()