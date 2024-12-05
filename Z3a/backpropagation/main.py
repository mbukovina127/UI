import numpy as np
from matplotlib import pyplot as plt

from Z3a.backpropagation.linear import Linear, Tanh, Sigmoid
from Z3a.backpropagation.model import Model, MSELoss

if __name__ == '__main__':
    # XOR dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Model definícia
    layers = [
        Linear(2, 4),
        Tanh(),
        Linear(4, 1),
        Sigmoid()
    ]

    model = Model(layers)
    loss_function = MSELoss()

    # Parametre tréningu
    lr = 0.3
    epochs = 3000
    losses = []

    # Tréning
    for epoch in range(epochs):
        # Forward
        output = model.forward(X)
        loss = loss_function.forward(output, y)
        losses.append(loss)

        # Backward
        loss_grad = loss_function.backward()
        model.backward(loss_grad)

        # Update
        model.update(lr)

        # Logging
        if epoch % 50 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    # Výstup modelu po tréningu
    print("Trained output:", model.forward(X))

    plt.plot(losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.xscale('linear')
    plt.title('Training Loss')
    plt.show()
