import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

if __name__ == '__main__':
    data = load_data('../data/sample_data.csv')
    print(data.head())