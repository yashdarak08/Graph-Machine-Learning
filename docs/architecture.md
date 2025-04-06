# Architecture Overview

This document outlines the architecture of the "Graph Deep Learning for Sparse Datasets" project.

## Data Pipeline

1. **Data Extraction:**
   - The web scraping module (`data_extraction.py`) extracts financial data from online sources.
   - Extracted raw data is stored in the `data/raw/` directory.

2. **Data Processing:**
   - The raw data is cleaned and structured using `data_processing.py`.
   - Processed data is saved in CSV format under `data/processed/`.

3. **Knowledge Graph Construction:**
   - A Neo4j database is used to store and manage the financial data as a knowledge graph.
   - The script `knowledge_graph.py` connects to Neo4j and creates nodes and relationships based on processed data.

4. **Graph Neural Network Training:**
   - Processed data is further used to construct a graph structure for training.
   - A GNN model is built using PyTorch and PyTorch Geometric in `model_training.py`.

## Model Architecture

- **Input:**  
  Node features derived from the processed financial data (e.g., company value).

- **GNN Layers:**  
  A two-layer Graph Convolutional Network (GCN) that learns node representations.

- **Output:**  
  Node classification into two classes (e.g., potential M&A targets).

## Deployment

- The project is designed to be modular and scalable.
- Dockerization and further deployment instructions can be added as needed.
