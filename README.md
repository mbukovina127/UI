# README

This repository contains selected assignments from an **Artificial Intelligence** course. Each assignment focuses on a different core AI concept, progressing from classical optimization methods to modern machine learning using neural networks.

The code is written in **Python** and uses common scientific and machine-learning libraries.

---
## Installation & Environment Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Assignment 1: Genetic Algorithm for the Traveling Salesperson Problem (Z1c)

### Topic

**Evolutionary optimization** applied to the **Traveling Salesperson Problem (TSP)**.

### Description

This assignment implements a **genetic algorithm**, an optimization technique inspired by natural evolution. The goal is to find a near-optimal route that visits a set of cities exactly once and returns to the starting city while minimizing total distance.

Key concepts demonstrated:

* Population-based search
* Fitness functions
* Selection, crossover, and mutation
* Graph representation of routes

### Key Files

* `Z1c/main.py` – Runs the genetic algorithm experiment
* `Z1c/gen.py` – Genetic operators (selection, crossover, mutation)
* `Z1c/myUtils.py` – Utility functions
* Uses `networkx` for graph modeling and `matplotlib` for visualization

### Expected Output

* Printed evolution statistics
* Visualized routes showing optimization progress

---

## Assignment 2: Agglomerative Clustering (Z2c)

### Topic

**Unsupervised learning** using **agglomerative hierarchical clustering** with centroid and medoid-based approaches.

### Description

This assignment implements an **agglomerative clustering algorithm**, a bottom-up hierarchical clustering method that iteratively merges the closest clusters. The algorithm supports two distance calculation strategies: **centroid-based** (average of all points) and **medoid-based** (most centrally located actual point).

The implementation uses a distance matrix to efficiently track cluster proximities and merges clusters until a specified distance criterion is violated. The algorithm generates synthetic 2D point data clustered around initial seed points and visualizes the final clustering result.

Key concepts demonstrated:

* Hierarchical clustering with agglomerative merging
* Distance matrix optimization for efficient nearest-neighbor search
* Centroid vs. medoid center calculation strategies
* Cluster validity checking with distance thresholds
* Interactive visualization with Plotly

### Key Files

* `main.py` — Generates synthetic clustered data and runs the agglomerative algorithm
* `cluster.py` — Defines `Cluster_C` (centroid) and `Cluster_M` (medoid) cluster classes
* `matrix.py` — Implements `Matrix_C` and `Matrix_M` for distance matrix management and aggregation
* `point.py` — Point class and distance calculation utilities
* `pltly.py` — Plotly-based scatter plot visualization of final clusters
* `visuals.py` — Matplotlib-based visualization utilities (alternative)

### Algorithm Overview

1. **Initialization**: Create initial clusters from randomly generated points around seed locations
2. **Distance Matrix**: Compute pairwise distances between all clusters
3. **Iterative Merging**: 
   - Find the two closest clusters
   - Merge them if the resulting cluster meets the distance criterion
   - Update the distance matrix
   - Repeat until no valid merges remain
4. **Visualization**: Display final clusters with color-coded points and marked centers

### Usage

The algorithm can be configured for either centroid or medoid clustering by commenting/uncommenting the appropriate lines in `main.py`:

```python
# For centroid-based clustering:
allClusters.append(Cluster_C((x,y)))
MTRX = Matrix_C(allClusters, LIMIT)

# For medoid-based clustering:
allClusters.append(Cluster_M((x,y)))
MTRX = Matrix_M(allClusters, LIMIT)
```

### Parameters

* `LIMIT` (default: 500) — Maximum allowed average distance from points to cluster center
* `max_points` (default: 6,000) — Total number of points to generate
* `min, max` (default: -5000, 5000) — Coordinate space boundaries
* Initial clusters: 20 seed points with surrounding point clouds

### Libraries Used

* `plotly` — Interactive scatter plot visualization
* `matplotlib` — Alternative static visualization (in `visuals.py`)
* Standard library: `random`, `math`

### Expected Output

* Console progress indicator showing aggregation iterations
* Interactive Plotly scatter plot displaying:
  - Colored point clouds for each final cluster
  - Black 'x' markers indicating cluster centers
  - Cluster count and spatial distribution

## Assignment 3: Neural Networks and Backpropagation (Z3a)

### Topic

**Supervised learning** using **deep neural networks** with custom backpropagation implementation and production frameworks.

### Description

This assignment explores neural network fundamentals through two complementary implementations. The first part demonstrates **backpropagation from scratch** using NumPy on the XOR problem, implementing forward pass, backward pass, and gradient descent manually. The second part applies modern deep learning techniques to classify handwritten digits from the **MNIST dataset** using PyTorch, comparing different optimization strategies.

Key concepts demonstrated:

* Manual implementation of forward and backward propagation
* Gradient descent with momentum optimization
* Activation functions (Sigmoid, Tanh, ReLU)
* Multi-layer perceptron architecture
* Batch training and evaluation
* Optimizer comparison (SGD, SGD with Momentum, Adam)
* Model evaluation with confusion matrices

### Key Files

**Backpropagation Implementation:**
* `backpropagation/linear.py` — Custom Linear layer, activation functions (Sigmoid, Tanh, ReLU)
* `backpropagation/model.py` — Model container and MSE loss implementation
* `backpropagation/main.py` — XOR problem training with custom neural network

**MNIST Classification:**
* `mnist.py` — Complete MNIST training pipeline with optimizer comparison

### Experiments

**Part 1: XOR Problem (Custom Implementation)**

Trains a simple MLP to solve the XOR logical function using manually implemented backpropagation. Demonstrates the necessity of non-linear activation functions for solving non-linearly separable problems.

Network architecture:
* Input layer: 2 neurons
* Hidden layer: 4 neurons with Tanh activation
* Output layer: 1 neuron with Sigmoid activation

**Part 2: MNIST Classification (PyTorch)**

Compares three optimization strategies on handwritten digit classification:

1. **Vanilla SGD** — Basic stochastic gradient descent
2. **SGD with Momentum** — Accelerated convergence with momentum (β = 0.9)
3. **Adam** — Adaptive learning rate optimization

Network architecture:
* Input: 784 features (28×28 flattened images)
* Hidden layer 1: 128 neurons with ReLU
* Hidden layer 2: 64 neurons with ReLU
* Output: 10 classes (digits 0-9)

### Parameters

**XOR Training:**
* Learning rate: 0.1
* Epochs: 500
* Momentum: 0.0 (configurable)

**MNIST Training:**
* Batch size: 64
* Epochs: 5
* Learning rates: 0.01 (SGD), 0.001 (Adam)
* Momentum: 0.9 (for SGD with momentum)

### Libraries Used

* `numpy` — Numerical computations for custom backpropagation
* `torch` — PyTorch deep learning framework
* `torchvision` — MNIST dataset and transformations
* `matplotlib` — Training curves and loss visualization
* `sklearn` — Confusion matrix generation

### Expected Output

**XOR Problem:**
* Training loss curve over 500 epochs
* Final predictions for all XOR input combinations
* Demonstration of successful non-linear function approximation

**MNIST Classification:**
* Training and test loss curves for each optimizer
* Accuracy progression over epochs
* Confusion matrices showing per-digit classification performance
* Comparative analysis of optimizer effectiveness (typically Adam > SGD+Momentum > Vanilla SGD)

