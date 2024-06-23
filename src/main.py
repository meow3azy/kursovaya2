import os
from src.transactions import print_last_transactions

if __name__ == "__main__":
    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, '../data/operations.json')
    print_last_transactions(file_path)
