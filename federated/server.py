from flwr.server.strategy import FedAvg
import flwr as fl
import logging
from rdflib import Graph
import glob
import os

logging.basicConfig(level=logging.INFO)

def main():
    strategy = FedAvg()  
    fl.server.start_server(config=fl.server.ServerConfig(num_rounds=3), strategy=strategy)
    
def build_global_kg(output_path="data/ttl/global_kg.ttl"):
    g = Graph()
    ttl_files = glob.glob("data/ttl/client_*.ttl")

    if not ttl_files:
        print("Nessun KG locale trovato.")
        return

    for ttl_file in ttl_files:
        g.parse(ttl_file, format="turtle")
        print(f"✓ Aggiunto: {ttl_file}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    g.serialize(destination=output_path, format="turtle")
    print(f"\n🌐 Global KG salvato in: {output_path}")

if __name__ == "__main__":
    fl.server.start_server(config=fl.server.ServerConfig(num_rounds=3))
    build_global_kg()