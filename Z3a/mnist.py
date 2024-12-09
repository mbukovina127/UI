import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np

# Nastavenie zariadenia
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Transformácie a načítanie datasetu
transform = transforms.Compose([
    transforms.ToTensor()
])

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)


# Definícia modelu
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.model = nn.Sequential(
            nn.Flatten(),  # Sploštenie vstupov
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        return self.model(x)


# Funkcia na trénovanie
def train_model(model, optimizer, criterion, num_epochs=20):
    model.to(device)
    train_losses, test_losses, accuracies = [], [], []

    for epoch in range(num_epochs):
        model.train()
        train_loss = 0

        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        train_losses.append(train_loss / len(train_loader))

        # Testovanie
        model.eval()
        test_loss, correct = 0, 0
        with torch.no_grad():
            for inputs, targets in test_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, targets)
                test_loss += loss.item()

                # Predikcia
                preds = outputs.argmax(dim=1)
                correct += (preds == targets).sum().item()

        test_losses.append(test_loss / len(test_loader))
        accuracies.append(correct / len(test_dataset))

        print(f"Epoch {epoch + 1}/{num_epochs}, Train Loss: {train_losses[-1]:.4f}, "
              f"Test Loss: {test_losses[-1]:.4f}, Accuracy: {accuracies[-1]:.4f}")

    return train_losses, test_losses, accuracies


# Vizualizácia tréningu
def plot_metrics(train_losses, test_losses, accuracies, title):
    epochs = range(1, len(train_losses) + 1)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_losses, label='Train Loss')
    plt.plot(epochs, test_losses, label='Test Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title(f'{title} - Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(epochs, accuracies, label='Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title(f'{title} - Accuracy')
    plt.legend()

    plt.show()


# Funkcia na vyhodnotenie modelu
def evaluate_model(model):
    model.eval()
    all_preds, all_targets = [], []
    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            preds = outputs.argmax(dim=1)
            all_preds.extend(preds.cpu().numpy())
            all_targets.extend(targets.cpu().numpy())

    cm = confusion_matrix(all_targets, all_preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.arange(10))
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix")
    plt.show()


# Spustenie experimentov
num_epochs = 20
criterion = nn.CrossEntropyLoss()

# SGD
model_sgd = MLP()
optimizer_sgd = optim.SGD(model_sgd.parameters(), lr=0.01)
train_losses_sgd, test_losses_sgd, accuracies_sgd = train_model(model_sgd, optimizer_sgd, criterion, num_epochs)
plot_metrics(train_losses_sgd, test_losses_sgd, accuracies_sgd, "SGD")
evaluate_model(model_sgd)

# SGD with Momentum
model_momentum = MLP()
optimizer_momentum = optim.SGD(model_momentum.parameters(), lr=0.01, momentum=0.9)
train_losses_momentum, test_losses_momentum, accuracies_momentum = train_model(model_momentum, optimizer_momentum,
                                                                               criterion, num_epochs)
plot_metrics(train_losses_momentum, test_losses_momentum, accuracies_momentum, "SGD with Momentum")
evaluate_model(model_momentum)

# Adam
model_adam = MLP()
optimizer_adam = optim.Adam(model_adam.parameters(), lr=0.001)
train_losses_adam, test_losses_adam, accuracies_adam = train_model(model_adam, optimizer_adam, criterion, num_epochs)
plot_metrics(train_losses_adam, test_losses_adam, accuracies_adam, "Adam")
evaluate_model(model_adam)
