"""Test authentication"""

import pytest
from app import db
from app.auth.models import User

class TestAuthentication:
    """Test authentication routes"""
    
    def test_user_registration(self, client):
        """Test user registration"""
        response = client.post('/api/auth/register', json={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'NewPassword123',
            'first_name': 'New',
            'last_name': 'User'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['user']['username'] == 'newuser'
        assert data['user']['email'] == 'new@example.com'
    
    def test_user_login(self, client, test_user):
        """Test user login"""
        response = client.post('/api/auth/login', json={
            'username': 'testuser',
            'password': 'TestPassword123'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'access_token' in data
        assert data['user']['username'] == 'testuser'
    
    def test_invalid_login(self, client):
        """Test login with invalid credentials"""
        response = client.post('/api/auth/login', json={
            'username': 'nonexistent',
            'password': 'WrongPassword'
        })
        
        assert response.status_code == 401
    
    def test_get_profile(self, client, auth_headers):
        """Test getting user profile"""
        response = client.get('/api/auth/profile', headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['username'] == 'testuser'
