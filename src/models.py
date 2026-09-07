import numpy as np


class LinearRegressionGD:
    """Linear regression trained via batch gradient descent."""

    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.w = 0.0
        self.b = 0.0
        self.loss_history = []

    def fit(self, X, y):
        X = np.asarray(X).flatten()
        y = np.asarray(y).flatten()
        n = len(y)

        for _ in range(self.n_iterations):
            y_pred = self.w * X + self.b
            loss = np.mean((y_pred - y) ** 2)
            self.loss_history.append(loss)

            error = y_pred - y
            dw = (2 / n) * np.sum(error * X)
            db = (2 / n) * np.sum(error)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

        return self

    def predict(self, X):
        X = np.asarray(X).flatten()
        return self.w * X + self.b