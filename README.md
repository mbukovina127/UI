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

## Assignment 3: Handwritten Digit Classification with Neural Networks (Z3a)

### Topic

**Supervised learning** using **deep neural networks**.

### Description

This assignment trains a neural network to classify handwritten digits from the **MNIST dataset**. MNIST is a standard benchmark dataset containing grayscale images of digits (0–9).

Key concepts demonstrated:

* Dataset preprocessing and normalization
* Neural network training
* Model evaluation and accuracy measurement
* Use of GPU-accelerated frameworks

### Key Files

* `Z3a/mnist.py` – Dataset loading, model definition, training loop

### Libraries Used

* `torch` – Core deep learning framework
* `torchvision` – Dataset utilities and transforms

