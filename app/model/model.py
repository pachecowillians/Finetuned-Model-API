from transformers import DistilBertForSequenceClassification
import torch

class ClassifierModel:
    def __init__(self, model_path="distilbert-base-uncased-finetuned-sst-2-english"):
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
    
    def predict(self, inputs):
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        predicted_class_index = torch.argmax(outputs.logits).item()
        predicted_label = "positive" if predicted_class_index == 1 else "negative"
        
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=1).tolist()[0]
        
        return {'label': predicted_label, 'probabilities': probabilities}
