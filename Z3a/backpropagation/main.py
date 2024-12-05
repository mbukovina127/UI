import numpy as np
from matplotlib import pyplot as plt

from Z3a.backpropagation.linear import Linear, Tanh, Sigmoid
from Z3a.backpropagation.model import Model, MSELoss

if __name__ == '__main__':
    # XOR dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [0], [0], [1]])

    # Model definícia
    layers = [
        Linear(2, 4),
        Tanh(),
        Linear(4, 1),
        Sigmoid()
    ]

    model = Model(layers)
    loss_fn = MSELoss()

    # Parametre tréningu
    lr = 0.1
    epochs = 1500
    losses = []

    # Tréning
    for epoch in range(epochs):
        # Forward
        output = model.forward(X)
        loss = loss_fn.forward(output, y)
        losses.append(loss)

        # Backward
        loss_grad = loss_fn.backward()
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
    plt.title('Training Loss')
    plt.show()
