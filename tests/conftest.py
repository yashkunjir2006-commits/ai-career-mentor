"""Pytest configuration and fixtures"""

import pytest
from app import create_app, db
from app.auth.models import User

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app(config_name='testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create CLI runner"""
    return app.test_cli_runner()

@pytest.fixture
def test_user(app):
    """Create test user"""
    user = User(
        username='testuser',
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('TestPassword123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def auth_headers(client, test_user):
    """Get authorization headers"""
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'TestPassword123'
    })
    token = response.get_json()['access_token']
    return {'Authorization': f'Bearer {token}'}
