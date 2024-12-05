import numpy as np

from Z3a.backpropagation.linear import Linear


class Model:
    def __init__(self, layers):
        self.layers = layers

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, loss_grad):
        for layer in reversed(self.layers):
            loss_grad = layer.backward(loss_grad)

    def update(self, lr):
        for layer in self.layers:
            if isinstance(layer, Linear):
                layer.update(lr)

class MSELoss:
    def forward(self, predicted, target):
        self.error = predicted - target
        return np.mean(self.error ** 2)

    def backward(self):
        return 2 * self.error / self.error.shape[0]
