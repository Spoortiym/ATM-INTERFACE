import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_menu_page_without_auth(client):
    response = client.get('/menu')
    assert response.status_code == 302  # Should redirect to login when not authenticated

def test_balance_inquiry_page(client):
    response = client.get('/balance_inquiry')
    assert response.status_code == 302  # Redirects to login if not authenticated

def test_withdraw_page_without_auth(client):
    response = client.get('/withdraw')
    assert response.status_code == 302  # Redirects to login if not authenticated

def test_mini_statement_page(client):
    response = client.get('/mini_statement')
    assert response.status_code == 302  # Redirects to login if not authenticated 