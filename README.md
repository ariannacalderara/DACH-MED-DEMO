DACH-MED-DEMO: Federated Knowledge Graphs for Healthcare

This repository demonstrates a **prototype architecture** that combines **Federated Learning (FL)** and **RDF-based Knowledge Graphs (KG)** for the healthcare domain. The project simulates a decentralized scenario where multiple medical institutions (clients) collaboratively contribute to a global RDF Knowledge Graph, **without sharing raw patient data**.

## Objective

The goal of this project is to showcase how:
- Each **client** builds its **local RDF Knowledge Graph** from data.
- A central **federated learning server** orchestrates the training and **aggregates knowledge** across clients.
- A final **global Knowledge Graph** is generated to represent shared insights across all data sources.

To simulate a decentralized architechture, the dataset used (diabetes.csv) is split among 2 participating clients. Each client models a KG and then these get aggregated into a global one. Clients never share the raw csv files and this is why this technique is widely adopted for sesntive data with special privacy requirements.
