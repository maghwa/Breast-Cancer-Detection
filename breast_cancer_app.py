import os
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from flask import Flask
import numpy as np
import io
from PIL import Image
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('model.h5')

# Create Flask app
app = Flask(__name__)

def predict_breast_cancer():
    # Ajouter le code CSS pour changer la couleur de la page en blanc
    put_html('''
        <style>
        body {
            background-color: white;
        }
        .pwt-btn {
            background-color: #FF69B4;
            color: white;
        }
        .pwt-btn-reset {
            background-color: orange;
        }
        </style>
    ''')
    
    put_row(
        [
            put_column(
                [
                    put_image(open(r'C:\Users\elkam\Breast-Cancer-Logo.png', 'rb').read(), width='200px'),
                ],
                size='auto'
            ),
            put_column(
                [
                    put_markdown("# Breast Cancer Classification")
                ],
                size='auto'
            )
        ],
        size='auto'
    )

    put_text("Please upload an image of a breast cell for prediction.")

    # File upload
    img = file_upload("Upload an image", accept="image/*", button_color="#FF69B4")

    # Preprocess the image
    img_array = np.array(Image.open(io.BytesIO(img['content'])))

    # Resize image to match model input size
    img_resized = Image.fromarray(img_array).resize((128, 128))

    # Preprocess the input image
    img_preprocessed = preprocess_input(np.array(img_resized))

    # Make predictions
    preds = model.predict(np.expand_dims(img_preprocessed, axis=0))
    labels = ['Normal', 'Benign', 'Malignant']
    prediction = labels[np.argmax(preds)]

    put_markdown("## Prediction Result")
    put_text(f"The uploaded image is predicted to be: {prediction}")

# Route to the web app
route = app.route('/', methods=['GET', 'POST'])
webio_app = start_server(predict_breast_cancer, routes=route, port=80)

if __name__ == '__main__':
    webio_app.run_server()
