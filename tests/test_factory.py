from flask import current_app
from flaskr import create_app

def test_config():
    app = create_app({'TESTING': True})
    assert not app.config['TESTING']
    assert app.testing

def test_hello(client):
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        response = client.get('/hello')
        assert response.data == b'hello world'
