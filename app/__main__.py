from flask import Flask
from app.api.classifier_api import classifier_api

app = Flask(__name__)
app.register_blueprint(classifier_api, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
