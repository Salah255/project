from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load model at startup
with open('sales_forecasting_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.json
        
        # Convert to DataFrame with correct feature order
        input_data = pd.DataFrame([[
            data['holiday_flag'],
            data['temperature'],
            data['fuel_price'],
            data['cpi'],
            data['unemployment']
        ]], columns=[
            'Holiday_Flag', 
            'Temperature',
            'Fuel_Price',
            'CPI',
            'Unemployment'
        ])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'currency': 'USD',
            'unit': 'sales'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)