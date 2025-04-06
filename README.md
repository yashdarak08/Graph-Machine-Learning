# Graph Deep Learning for Sparse Datasets

Graphs are very fascinating on their own but when you add Machine Learning to them, it gets a whole lot more fun!
This project leverages advanced graph machine learning techniques to enhance predictions of potential mergers and acquisitions (M&A) by uncovering acquisition patterns and relationships within sparse datasets.

## Project Overview

- **Project Stucture:**  
The project is organized into several key components, each focusing on a specific aspect of the graph machine learning pipeline.
Graph-Deep-Learning-for-Sparse-Datasets/
```bash
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── raw/                # Raw data files (e.g., scraped financial data)
│   └── processed/          # Processed data and generated knowledge graphs
├── src/
│   ├── data_extraction.py  # Web scraping and data extraction code
│   ├── data_processing.py  # Data cleaning and transformation scripts
│   ├── knowledge_graph.py  # Code to build and interact with Neo4j graphs
│   └── model_training.py   # Scripts for training Graph Neural Networks
├── notebooks/
│   ├── EDA.ipynb           # Exploratory Data Analysis notebook
│   └── model_training.ipynb# Notebook for GNN training experiments
└── docs/
    ├── architecture.md     # Detailed architecture and design documents
    └── usage.md            # Instructions on setting up and running the project

```

- **Objective:**  
  Design and implement a Graph Machine Learning model tailored for sparse M&A networks.

- **Key Contributions:**
  - Developed a comprehensive pipeline that extracts and processes over **250 GB** of online financial data through web scraping.
  - Transformed raw data into structured knowledge graphs using **Neo4j**.
  - Trained predictive models using **Graph Neural Networks (GNNs)** and node embeddings.
  - Achieved an improvement of **2%** in prediction accuracy compared to traditional models.

## Repository Structure

- **data/**  
  Contains both raw and processed datasets.

- **src/**  
  Source code for each step in the pipeline:
  - Data extraction via web scraping.
  - Data processing and transformation into knowledge graphs.
  - Building and training graph-based models.

- **notebooks/**  
  Jupyter notebooks for exploratory data analysis (EDA) and model experimentation.

- **docs/**  
  Documentation including system architecture and detailed usage instructions.

- **requirements.txt**  
  A list of required Python libraries for setting up the project environment.
