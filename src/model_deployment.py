import joblib

def predict(data):
    model = joblib.load('../models/trained_model.pkl')
    return model.predict(data)

if __name__ == '__main__':
    import pandas as pd
    sample_input = pd.DataFrame({'temperature': [75], 'pressure': [32], 'vibration': [0.03]})
    predictions = predict(sample_input)
    print(f'Predictions: {predictions}')