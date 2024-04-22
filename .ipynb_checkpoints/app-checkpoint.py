from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


# Load the model and features
with open('Grade_prediction.pickle', 'rb') as file:
    model, features = pickle.load(file)

# Ensure that features is a list
features = list(features)

# Prediction function
def predict_grade(features_values):
    return model.predict([features_values])[0]

# Convert to grade as A, B, C, or D
def convert_to_grade(predicted_grade):
    if predicted_grade < 0.2:
        return 'A'
    elif predicted_grade < 1:
        return 'B'
    elif predicted_grade < 2:
        return 'C'
    else:
        return 'D'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        Sex = float(request.form['Sex'])
        High_School_Type = float(request.form['High_School_Type'])
        Sports_activity = float(request.form['Sports_activity'])
        Weekly_Study_Hours = float(request.form['Weekly_Study_Hours'])
        Attendance = float(request.form['Attendance'])
        Reading = float(request.form['Reading'])
        Listening_in_Class = float(request.form['Listening_in_Class'])
        Project_work = float(request.form['Project_work'])

        # Make prediction
        features_values = [Sex, High_School_Type, Sports_activity, Weekly_Study_Hours, Attendance, Reading, Listening_in_Class, Project_work]
        predicted_grade = predict_grade(features_values)
        grade = convert_to_grade(predicted_grade)

        return render_template('index.html', grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
