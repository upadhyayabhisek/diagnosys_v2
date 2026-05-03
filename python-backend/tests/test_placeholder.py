import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app
from chatbot import predict_disease, get_recommendations
from db import create_user


@pytest.fixture
def client():
    """Setting up a virtual Flask test client"""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret'

    with app.test_client() as client:
        yield client


# =========================
# ML MODEL TESTS
# =========================

def test_prediction_output_format():
    """Check if the model returns a string and a float confidence"""
    disease, confidence = predict_disease("I have a high fever and headache")
    assert isinstance(disease, str)
    assert isinstance(confidence, float)


def test_nepali_fallback():
    """Check if nonsense input triggers the unknown disease response"""
    disease, confidence = predict_disease("I want to eat pizza", lang="np")
    assert disease == "अज्ञात"


# =========================
# FLASK ROUTE TESTS
# =========================

def test_home_route(client):
    """Check if the home page works"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"MediAI Backend running" in response.data


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


# =========================
# AUTH + ADMIN FLOW TEST
# =========================

def test_admin_login_and_logout_flow(client):
    """
    Test:
    admin login → access admin panel → simulate logout → access blocked
    """

    # 1. Create admin user
    create_user(
        name="Admin User",
        email="admin@test.com",
        password="admin123",
        role="admin"
    )

    # 2. Login as admin
    login_response = client.post('/login', json={
        "email": "admin@test.com",
        "password": "admin123"
    })

    assert login_response.status_code in [200, 302]

    # 3. Access admin panel (should succeed)
    admin_response = client.get('/admin')

    assert admin_response.status_code in [200, 302]
    assert admin_response.status_code != 401

    # =========================
    # 4. SIMULATE useAuth().logout()
    # =========================

    with client.session_transaction() as sess:
        sess.clear()

    after_logout_response = client.get('/admin')

    assert after_logout_response.status_code in [302, 401, 403]

