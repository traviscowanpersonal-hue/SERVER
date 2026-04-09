from flask import Flask, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    price = float(data.get("price", 0))

    # SIMPLE REAL STRATEGY (you can upgrade later)
    # Example: basic logic (replace later with smarter one)
    
    if price % 2 > 1:  
        return "BUY"
    else:
        return "SELL"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)