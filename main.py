from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_deployment import predict

if __name__ == '__main__':
    data = load_data('./data/sample_data.csv')
    processed_data = preprocess_data(data)
    train_model(processed_data)
    sample_input = processed_data.iloc[:1][['temperature', 'pressure', 'vibration']]
    print(predict(sample_input))