import warnings
import pickle
from flask import Flask, request, jsonify
from utilities import validate_request, preprocess, make_prediction
import os

warnings.filterwarnings('ignore')

early_detection_model_path = os.path.join(os.getcwd(), 'models/finalized_svm_model_diabetes.pkl')
diagnosis_model_path = os.path.join(os.getcwd(), 'models/finalized_lg_model_diabetes.pkl')
early_detection_model = pickle.load(open(early_detection_model_path, 'rb'))
diagnosis_model = pickle.load(open(diagnosis_model_path, 'rb'))

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to the Diabetes Prediction API"}


@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.get_json()
    error = validate_request(user_input)
    if error:
        return jsonify({"error": error}), 400

    try:
        # Preprocess the data
        data = preprocess(user_input)

        # Make a prediction
        prediction = make_prediction(early_detection_model, data)

        # Return the prediction as JSON response
        return jsonify(prediction)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
