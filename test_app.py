import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that the index page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that the login page loads successfully."""
    response = client.get('/login')
    assert response.status_code == 200

def test_menu_page(client):
    """Test that the menu page loads successfully."""
    response = client.get('/menu')
    assert response.status_code == 200

def test_balance_inquiry_page(client):
    """Test that the balance inquiry page loads successfully."""
    response = client.get('/balance_inquiry')
    assert response.status_code == 200

def test_withdraw_page(client):
    """Test that the withdraw page loads successfully."""
    response = client.get('/withdraw')
    assert response.status_code == 200

def test_mini_statement_page(client):
    """Test that the mini statement page loads successfully."""
    response = client.get('/mini_statement')
    assert response.status_code == 200

def test_change_pin_page(client):
    """Test that the change pin page loads successfully."""
    response = client.get('/change_pin')
    assert response.status_code == 200 