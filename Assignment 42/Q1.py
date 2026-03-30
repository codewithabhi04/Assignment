import numpy as np

def MarvellousPredictor():
    # Dataset
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of X:", X)
    print("Values of Y:", Y)

    # Mean
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of X:", mean_x)
    print("Mean of Y:", mean_y)

    n = len(X)

    # Calculate slope (m)
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2

    m = numerator / denominator

    # Calculate intercept (c)
    c = mean_y - (m * mean_x)

    print("Slope (m):", round(m,2))
    print("Intercept (c):", round(c,2))

    # Final regression equation
    print("Regression Equation: Y =", round(m,2), "X +", round(c,2))

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()