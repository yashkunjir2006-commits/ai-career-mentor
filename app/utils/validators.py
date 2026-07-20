"""
Utility validators
"""

import re
from typing import Tuple

class Validator:
    """Input validation utilities"""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email address"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True, "Valid email"
        return False, "Invalid email format"
    
    @staticmethod
    def validate_password(password: str) -> Tuple[bool, str]:
        """Validate password strength"""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter"
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit"
        return True, "Valid password"
    
    @staticmethod
    def validate_username(username: str) -> Tuple[bool, str]:
        """Validate username"""
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        if len(username) > 20:
            return False, "Username must not exceed 20 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        return True, "Valid username"
