import pytest
from app import app
from chatbot import predict_disease, get_recommendations

@pytest.fixture
def client():
    """Setting up a virtual Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prediction_output_format():
    """Check if the model returns a string and a float confidence"""
    disease, confidence = predict_disease("I have a high fever and headache")
    assert isinstance(disease, str)
    assert isinstance(confidence, float)

def test_nepali_fallback():
    """Check if nonsense input triggers the unknown disease response"""
    disease, confidence = predict_disease("I want to eat pizza", lang="np")
    assert disease == "अज्ञात"


def test_home_route(client):
    """Check if the home page works"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"mediai Backend running" in response.data

def test_analyze_endpoint(client):
    """Check if the /analyze endpoint returns JSON success"""
    payload = {
        "message": "I feel very weak and tired",
        "lang": "en"
    }
    response = client.post('/analyze', json=payload)
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'prediction' in data