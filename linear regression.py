### Créé par t.hausmann, le 27/09/2022 en Python 3.7
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##def estimate_coef(x, y):
##    # number of observations/points
##    n = np.size(x)
##
##    # mean of x and y vector
##    m_x = np.mean(x) # MEAN = la moyenne
##    m_y = np.mean(y)
##
##    # calculating cross-deviation and deviation about x
##    SS_xy = np.sum(y*x) - n*m_y*m_x
##    SS_xx = np.sum(x*x) - n*m_x*m_x #don't know deviation for the moment
##
##    # calculating regression coefficients
##    b_1 = SS_xy / SS_xx
##    b_0 = m_y - b_1*m_x
##    '''use equation to compute the regression coef (b_0 is
##    equal to y_intercept (where the line is crossing y) and b_1 is equal to the
##    slope(l'inclinaison)
##    '''
##    return (b_0, b_1)
##
##def plot_regression_line(x, y, b):
##    # plotting the actual points as scatter plot
##    plt.scatter(x, y, color = "m",
##               marker = "o", s = 30)
##
##    # predicted response vector
##    y_pred = b[0] + b[1]*x
##
##    # plotting the regression line
##    plt.plot(x, y_pred, color = "g")
##
##    # putting labels
##    plt.xlabel('x')
##    plt.ylabel('y')
##
##    # function to show plot
##    plt.show()
##
##def main():
##    # observations / data
##    x = np.array([0, 1, 2, 3, 4, 8, 6, 7, 8, 9])
##    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
##
##    # estimating coefficients
##    b = estimate_coef(x, y)
##    print("Estimated coefficients:\nb_0 = {}  \
##          \nb_1 = {}".format(b[0], b[1]))
##
##    # plotting regression line
##    plot_regression_line(x, y, b)
##
##if __name__ == "__main__":
##    main()


""" I'm turning the script into a dynamic script to train myself """

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x) # MEAN = la moyenne
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x #don't know deviation for the moment

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    '''use equation to compute the regression coef (b_0 is
    equal to y_intercept (where the line is crossing y) and b_1 is equal to the
    slope(l'inclinaison)
    '''
    return (b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()

def main():
    # observations / data
    x1=[]
    n=int(input("Number of elements in array FOR X:"))
    for i in range(0,n):
       l=int(input())
       x1.append(l)
    print(x1)
    x1 = np.array(x1)
    y1=[]
    for i in range(0,n):
       l=int(input())
       y1.append(l)
    print(x1)
    y1 = np.array(y1)

    # estimating coefficients
    b = estimate_coef(x1, y1)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x1, y1, b)

if __name__ == "__main__":
    main()