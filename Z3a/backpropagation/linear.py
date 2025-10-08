import numpy as np

# Lineárna vrstva
class Linear:
    def __init__(self, input_size, output_size, momentum=0.0):
        limit = np.sqrt(6 / (input_size + output_size))
        self.weights = np.random.uniform(-limit, limit, (input_size, output_size))
        self.bias = np.zeros((1, output_size))
        self.input = None
        self.grad_weights = None
        self.grad_bias = None
        self.v_weights = np.zeros_like(self.weights)
        self.v_bias = np.zeros_like(self.bias)
        self.momentum = momentum

    def forward(self, x):
        self.input = x
        return np.dot(x, self.weights) + self.bias

    def backward(self, grad_output):
        self.grad_weights = np.dot(self.input.T, grad_output)
        self.grad_bias = np.sum(grad_output, axis=0, keepdims=True)
        return np.dot(grad_output, self.weights.T)

    def update(self, lr):
        if self.momentum > 0:
            # Update with momentum
            self.v_weights = self.momentum * self.v_weights - lr * self.grad_weights
            self.v_bias = self.momentum * self.v_bias - lr * self.grad_bias
            self.weights += self.v_weights
            self.bias += self.v_bias
        else:
            # Vanilla gradient descent
            self.weights -= lr * self.grad_weights
            self.bias -= lr * self.grad_bias


# Aktivácie
class Sigmoid:
    def forward(self, x):
        self.output = 1 / (1 + np.exp(-x))
        return self.output

    def backward(self, grad_output):
        return grad_output * self.output * (1 - self.output)

class Tanh:
    def forward(self, x):
        self.output = np.tanh(x)
        return self.output

    def backward(self, grad_output):
        return grad_output * (1 - self.output ** 2)

class ReLU:
    def forward(self, x):
        self.input = x
        return np.maximum(0, x)

    def backward(self, grad_output):
        grad_input = grad_output.copy()
        grad_input[self.input <= 0] = 0
        return grad_input
