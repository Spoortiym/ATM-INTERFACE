from app import app

def login():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def balance_inquiry():
    tester = app.test_client()
    response = tester.get('/balance_inquiry')
    assert response.status_code == 200

