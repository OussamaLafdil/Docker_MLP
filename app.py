from flask import Flask, request, render_template_string, jsonify
import pickle
import numpy as np
import json

# Load the saved model
with open('ecg_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# HTML Template for Upload Form
UPLOAD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ECG Prediction</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">ECG Prediction</h1>
        <p class="text-muted text-center">Upload a JSON file containing the features for prediction</p>
        <form method="POST" action="/predict" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="json_file" class="form-label">Upload JSON File</label>
                <input type="file" class="form-control" id="json_file" name="json_file" accept=".json" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
"""

# HTML Template for Result Page
RESULT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prediction Result</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5 text-center">
        <h1>Prediction Result</h1>
        <p class="display-4">Prediction: <strong>{{ prediction }}</strong></p>
        <p class="display-6">{{ interpretation }}</p>
        <a href="/" class="btn btn-primary mt-3">Try Again</a>
    </div>
</body>
</html>
"""

# Routes
@app.route('/')
def home():
    """Render the file upload form."""
    return render_template_string(UPLOAD_HTML)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests from a JSON file."""
    try:
        # Check if a JSON file is uploaded
        json_file = request.files.get('json_file')
        if not json_file:
            return jsonify({'error': 'No JSON file uploaded'}), 400

        # Load and validate JSON file
        json_data = json.load(json_file)
        if "features" not in json_data or len(json_data["features"]) != 140:
            return jsonify({'error': 'JSON file must contain a "features" key with exactly 140 values'}), 400

        # Extract features from JSON
        features = np.array(json_data["features"]).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features)[0][0]
        rounded_prediction = round(prediction)

        # Interpret the prediction
        if rounded_prediction == 0:
            interpretation = "ECG normal (patient sain)"
        elif rounded_prediction == 1:
            interpretation = "ECG anormal (présence d’une anomalie)"
        else:
            interpretation = "Prediction unclear"

        return render_template_string(RESULT_HTML, prediction=rounded_prediction, interpretation=interpretation)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
