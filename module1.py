# Créé par t.hausmann, le 13/05/2024 en Python 3.7
# Créé par pc, le 17/04/2024 en Python 3.7
# -*- coding: utf-8 -*-
# implémentation d'un perceptron

import numpy as np
import matplotlib.pyplot as plt  # corrected import statement

####################   PRÉPARATION DES DONNÉES        ####################
# à faire à la fin

####################           PERCEPTRON             ####################
# DONNÉES D'ENTRÉES D'ENTRAINEMENT
X_train = np.load("X_train_elev.npy")
y_train = np.load("y_train_elev.npy")

# PARAMETRES DU PERCEPTRON
epochs = 100
eta = 0.01

# FONCTION ACTIVATION
def activation(s):
    return np.heaviside(s, 0)  # added threshold value to np.heaviside

# SOMME PONDÉRÉE
def entrainement(epochs, eta, X_train, y_train):
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
    poids = np.zeros(X_train.shape[1])  # initialized weights with zeros
    biais = 0.0
    # boucle d'iteration d'ajustement des poids et du biais
    for j in range(epochs):
        # a chaque iteration on parcourt les donnees d'apprentissage
        for i in range(len(X_train)):
            s = np.dot(poids, X_train[i]) + biais  # added biais to the weighted sum
            y_predict = activation(s)         # lance la fonction d'activation
            erreur = y_train[i] - y_predict  # corrected error calculation
            #  mise a jour des poids et du biais
            poids += erreur * eta * X_train[i]
            biais += erreur * eta
    return poids, biais

essai_train = entrainement(epochs, eta, X_train, y_train)
assert essai_train[0][0] == 0.08499999999999998
assert essai_train[0][1] == -0.15000000000000002
assert essai_train[1] == -0.01

####################           TEST DU PERCEPTRON             ##################
# DONNÉES D'ENTRÉES DE TEST
X_test = np.load("X_test_elev.npy")
y_test = np.load("y_test_elev.npy")  # added this line
poids = essai_train[0]
biais = essai_train[1]

# PRÉDICTION DU PERCEPTRON
def predict(poids, biais, X_test, y_test):
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
    s = np.dot(X_test, poids) + biais  # added biais to the weighted sum
    y_prediction = activation(s)
    erreur = 0
    list_test = [(y_test[i], y_prediction[i]) for i in range(len(y_test))]
    for i in range(len(y_test)):
        if y_prediction[i] != y_test[i]:
            erreur += 1
    return list_test, erreur/len(y_test)*100

essai_test = predict(essai_train[0], essai_train[1], X_test, y_test)
assert essai_test[0] == [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1), (0, 0), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 0), (1, 0), (1, 1), (1, 1)]
assert essai_test[1] == 12.0

####################           FRONTIERE             ##################
# DONNÉES GLOBALES
X_data = np.concatenate((X_train, X_test), axis=0)

def frontiere(poids, biais):
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
    x11 = min(X_data[:, 0])
    x12 = -(biais + poids[0] * x11) / poids[1]
    x21 = max(X_data[:, 0])
    x22 = -(biais + poids[0] * x21) / poids[1]
    return (x11, x12), (x21, x22)

droite_frontiere = frontiere(essai_train[0], essai_train[1])
assert droite_frontiere == ((4.3, 7.0), (2.369999999999999, 3.8999999999999986))

#########################    AFFICHAGE DES DONNEES   #############################
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], s=15, marker='.', color='g', label="X_train")
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], s=15, marker='.', color='r', label="X_train")
plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1], s=20, marker='^', color='g', label="X_test")
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1], s=20, marker='^', color='r', label="X_test")
plt.plot([droite_frontiere[0][0], droite_frontiere[1][0]], [droite_frontiere[0][1], droite_frontiere[1][1]], "b-", label="frontière")
plt.axis([min(X_data[:, 0]) - 0.2, max(X_data[:, 0]) + 0.2, min(X_data[:, 1]) - 0.2, max(X_data[:, 1]) + 0.2])
plt.grid()
plt.legend(title=f"exactitude : {100 - essai_test[1]}%")
plt.show()
