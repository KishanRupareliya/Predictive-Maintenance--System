from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(data):
    X = data[['temperature', 'pressure', 'vibration']]
    y = data['maintenance_required'].map({'No': 0, 'Yes': 1})
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, '../models/trained_model.pkl')
    return model

if __name__ == '__main__':
    from data_preprocessing import preprocess_data
    from data_ingestion import load_data
    data = load_data('../data/sample_data.csv')
    processed_data = preprocess_data(data)
    model = train_model(processed_data)
    print('Model trained and saved.')