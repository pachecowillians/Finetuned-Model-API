from transformers import DistilBertTokenizer

class Tokenizer:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    
    def tokenize(self, text):
        return self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
