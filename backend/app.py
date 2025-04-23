from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import os
from flask_cors import CORS
from urllib.parse import unquote
import numpy as np
from flask import Flask, render_template, send_file

app = Flask(__name__, static_folder="../static")
CORS(app)

# Folder for storage of uploaded Excel files
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# In-memory storage of uploaded file data
uploaded_files = {}

@app.route("/lib/<path:filename>")
def serve_lib(filename):
    return send_from_directory("../lib", filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        xls = pd.ExcelFile(filepath)

        if not xls.sheet_names:
            return jsonify({"error": "No valid sheets found in this file"}), 400

        df = pd.read_excel(xls, sheet_name=0)

        return jsonify({"message": f"{file.filename} uploaded successfully."}), 201

    except Exception as e:
        return jsonify({"error": f"File format error: {str(e)}"}), 500


@app.route('/api/files', methods=['GET'])
def list_files():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.xlsx')]
    return jsonify({"files": files})

@app.route('/api/data/<filename>', methods=['GET'])
def get_file_data(filename):
    filename = unquote(filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    try:
        df = pd.read_excel(filepath)
    except Exception as e:
        return jsonify({"error": f"Failed to read file: {str(e)}"}), 500

    # Clean out problematic values like NaN
    cleaned = df.replace({np.nan: None}) 

    try:
        return jsonify(cleaned.to_dict(orient='records'))
    except Exception as e:
        print("JSON conversion error:", e)
        return jsonify({"error": "Failed to convert data to JSON"}), 500



@app.route('/api/sample-chart', methods=['GET'])
def sample_chart():
    # Simulated chart data
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 15, 25]
    }
    return jsonify(data)
@app.route('/upload_form')
def show_upload_form():
    return render_template('upload_form.html')

@app.route('/dashboard')
def show_dashboard():
    return send_file("../frontend/dashboard.html")
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5423, debug=True)