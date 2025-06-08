import flwr as fl
import pandas as pd
import numpy as np
from kg_utils import build_knowledge_graph
from collections import Counter

class FLClient(fl.client.NumPyClient):
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.kg = build_knowledge_graph(self.df, client_id="client_2")
        self.kg.serialize(destination="data/ttl/client_2.ttl", format="turtle")

        # Simple "embedding": histogram of predicate usage
        self.embedding = self._get_embedding()  
    
    def _get_embedding(self):
        predicates = [str(p) for _, p, _ in self.kg]
        counts = Counter(predicates)
        
        # Create a sorted list of known predicates
        keys = sorted(list(counts))
        values = [counts[k] for k in keys]
        return np.array(values, dtype=np.float32)
    
    def get_parameters(self, config):
        return [self.embedding]

    def set_parameters(self, parameters):
        self.embedding = parameters[0]  # Only one embedding per client

    def fit(self, parameters, config):
        return self.get_parameters(config), len(self.df), {}

    def evaluate(self, parameters, config):
        return 0.0, len(self.df), {}


if __name__ == "__main__":
    fl.client.start_numpy_client(
        server_address="localhost:8080", client=FLClient("data/splits/client_2.csv"))
