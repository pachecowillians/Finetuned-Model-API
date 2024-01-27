from flask import Blueprint, request, jsonify
from app.model.model import ClassifierModel
from app.utils.tokenizer import Tokenizer

classifier_api = Blueprint('classifier_api', __name__)

model = ClassifierModel()
tokenizer = Tokenizer()

@classifier_api.route('/classify', methods=['POST'])
def classify_text():
    data = request.get_json(force=True)
    text = data['text']

    # Tokenize input text
    inputs = tokenizer.tokenize(text)

    # Perform inference
    prediction = model.predict(inputs)

    # Prepare the response
    response = {
        'text': text,
        'predicted_class': prediction['label'],
        'class_probabilities': prediction['probabilities']
    }

    return jsonify(response)
