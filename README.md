Steps to follow:

1. Install required libraries 
    - Create a virtual environment
    - Then install the necessary packages (pip install flwr pandas scikit-learn rdflib openai python-dotenv matplotlib networkx)
    - if needed install torch (PyTorch) - pip install torch torchvision

2. Data Preparation
    - let's use diabetes.csv from kaggle (https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
    - create and run split_data.py

3. Federated Learning Set-up with Flower
    - complete server.py
    - define client_1.py and client_2.py
    - Run: server.py, client_1.py (in new terminal) and client_2.py (in another terminal)