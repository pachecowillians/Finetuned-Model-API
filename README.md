# Finetuned-Model-API
Flask API for sentiment classification using Hugging Face's fine-tuned model.

## Getting Started

### Prerequisites

- Docker
- Python 3.8 or higher

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/pachecowillians/Finetuned-Model-API.git
   cd Finetuned-Model-API
   ```

2. Run the API:

   ```bash
   docker-compose up --build
   ```

   The API will be available at http://localhost:5000/api/classify.

3. Train the Model:

   ```bash
   python training/finetune_model.py
   ```

## API Endpoints

### Classify Text

**Endpoint:**

```
POST /api/classify
```

**Request:**

```json
{
  "text": "This is a positive example."
}
```

**Response:**

```json
{
  "text": "This is a positive example.",
  "predicted_class": "positive",
  "class_probabilities": [0.013937118053436756, 0.9860628843307495]
}
```

## Built With

- Flask - Web framework
- Hugging Face Transformers - Natural language processing library