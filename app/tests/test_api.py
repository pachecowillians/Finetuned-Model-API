import json
import pytest
from ..app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_classify_text_positive(client):
    response = client.post('/api/classify', json={"text": "This is a positive example."})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['predicted_class'] == 'positive'

def test_classify_text_negative(client):
    response = client.post('/api/classify', json={"text": "This is a negative example."})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['predicted_class'] == 'negative'
