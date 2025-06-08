import pandas as pd
import os
from sklearn.model_selection import StratifiedKFold

def split_data(input="data/diabetes.csv", output_dir="data/splits", n_clients=2):
    print("Reading data from:", input)
    df = pd.read_csv(input)
    print("Data shape:", df.shape)

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    skf = StratifiedKFold(n_splits=n_clients, shuffle=True, random_state=42)
    os.makedirs(output_dir, exist_ok=True)

    for i, (_, test_index) in enumerate(skf.split(X, y)):
        split = df.iloc[test_index]
        path = f"{output_dir}/client_{i+1}.csv"
        print(f"Saving split {i+1} to {path} with shape {split.shape}")
        print(f"Class distribution:\n{split['Outcome'].value_counts()}")
        split.to_csv(path, index=False)

if __name__ == "__main__":
    split_data()
