def preprocess_data(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data

if __name__ == '__main__':
    from data_ingestion import load_data
    data = load_data('../data/sample_data.csv')
    processed_data = preprocess_data(data)
    print(processed_data.head())