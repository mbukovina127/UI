import numpy as np
from matplotlib import pyplot as plt

from Z3a.backpropagation.linear import Linear, Tanh, Sigmoid
from Z3a.backpropagation.model import Model, Loss

if __name__ == '__main__':
    # XOR dataset
    X = np.array([[0, 1], [0, 0], [1, 0], [1, 1]])
    y = np.array([[0], [0], [0], [1]])

    # Model definícia
    momentum = 0.9
    layers = [
        Linear(2, 4, momentum),
        Tanh(),
        Linear(4, 4, momentum),
        Tanh(),
        Linear(4, 1, momentum),
        Sigmoid()
    ]

    model = Model(layers)
    loss_function = Loss()

    # Parametre tréningu
    lr = 0.05
    epochs = 500
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
    plt.title(f"Training Loss    mom:{momentum:.2}    lrn.r:{lr:.2}")
    plt.show()
