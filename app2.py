from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

def detect_disease(image):
    """
    Placeholder function for disease detection.
    In real cases, use a trained model to predict the disease based on the tongue image.
    """
    # Here you could load your trained model and run inference
    return "Healthy"  # Example result, replace with real inference

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    image = Image.open(BytesIO(image_data))

    # Convert image to OpenCV format for processing
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Preprocessing steps, e.g., resizing, normalizing, etc.
    processed_image = cv2.resize(open_cv_image, (224, 224))  # Resize for model input
    
    # Predict disease using the placeholder function
    disease = detect_disease(processed_image)
    
    return jsonify({'disease': disease})

if __name__ == '__main__':
    app.run(debug=True)
