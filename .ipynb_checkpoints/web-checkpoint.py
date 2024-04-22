from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model and features
def load_model():
    with open('Grade_prediction.pickle', 'rb') as f:
        model, features = pickle.load(f)
    return model, features

model, features = load_model()

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json()
    
    # Extract features from the request data
    input_features = [data[feature] for feature in features]
    
    # Make prediction
    predicted_grade = model.predict([input_features])[0]
    grade = convert_to_grade(predicted_grade)  # You need to define convert_to_grade function
    
    # Return the prediction as JSON
    return jsonify({'grade': grade})

if __name__ == '__main__':
    app.run(debug=True)
