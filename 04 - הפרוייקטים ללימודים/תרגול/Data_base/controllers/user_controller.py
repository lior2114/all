from flask import request, jsonify
from models.user_model import UserModel
import re

class UserController:
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def login():
        """Login user"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data.get('email') or not data.get('password'):
                return jsonify({
                    'success': False,
                    'error': 'Email and password are required'
                }), 400
            
            # Validate email format
            if not UserController.validate_email(data['email']):
                return jsonify({
                    'success': False,
                    'error': 'Invalid email format'
                }), 400
            
            # Try to find user by email
            user = UserModel.get_user_by_email(data['email'])
            if not user:
                return jsonify({
                    'success': False,
                    'error': 'No users found with this email'
                }), 404
            
            # Check password
            hashed_password = UserModel.hash_password(data['password'])
            if user['password'] != hashed_password:
                return jsonify({
                    'success': False,
                    'error': 'Email or password are wrong'
                }), 401
            
            # Remove password from response
            user.pop('password', None)
            
            return jsonify({
                'success': True,
                'data': user,
                'message': 'Login successful'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        try:
            users = UserModel.get_all_users()
            
            # Remove password from response
            for user in users:
                user.pop('password', None)
            
            return jsonify({
                'success': True,
                'data': users,
                'count': len(users)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID"""
        try:
            user = UserModel.get_user_by_id(user_id)
            if not user:
                return jsonify({
                    'success': False,
                    'error': 'User not found'
                }), 404
            
            # Remove password from response
            user.pop('password', None)
            
            return jsonify({
                'success': True,
                'data': user
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def create_user():
        """Create a new user"""
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['username', 'email', 'password']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        'success': False,
                        'error': f'{field} is required'
                    }), 400
            
            # Validate email format
            if not UserController.validate_email(data['email']):
                return jsonify({
                    'success': False,
                    'error': 'Invalid email format'
                }), 400
            
            # Validate password length
            if len(data['password']) < 6:
                return jsonify({
                    'success': False,
                    'error': 'Password must be at least 6 characters long'
                }), 400
            
            # Create new user
            user_id = UserModel.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            
            # Get the created user
            user = UserModel.get_user_by_id(user_id)
            user.pop('password', None)
            
            return jsonify({
                'success': True,
                'data': user,
                'message': 'User created successfully'
            }), 201
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def update_user(user_id):
        """Update user by ID"""
        try:
            # Check if user exists
            existing_user = UserModel.get_user_by_id(user_id)
            if not existing_user:
                return jsonify({
                    'success': False,
                    'error': 'User not found'
                }), 404
            
            data = request.get_json()
            if not data:
                return jsonify({
                    'success': False,
                    'error': 'No data provided for update'
                }), 400
            
            # Validate email format if provided
            if 'email' in data and not UserController.validate_email(data['email']):
                return jsonify({
                    'success': False,
                    'error': 'Invalid email format'
                }), 400
            
            # Validate password length if provided
            if 'password' in data and len(data['password']) < 6:
                return jsonify({
                    'success': False,
                    'error': 'Password must be at least 6 characters long'
                }), 400
            
            # Update user
            success = UserModel.update_user(user_id, **data)
            
            if not success:
                return jsonify({
                    'success': False,
                    'error': 'Failed to update user'
                }), 500
            
            # Get updated user
            updated_user = UserModel.get_user_by_id(user_id)
            updated_user.pop('password', None)
            
            return jsonify({
                'success': True,
                'data': updated_user,
                'message': 'User updated successfully'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def delete_user(user_id):
        """Delete user by ID"""
        try:
            # Check if user exists
            existing_user = UserModel.get_user_by_id(user_id)
            if not existing_user:
                return jsonify({
                    'success': False,
                    'error': 'User not found'
                }), 404
            
            # Delete user
            success = UserModel.delete_user(user_id)
            
            if not success:
                return jsonify({
                    'success': False,
                    'error': 'Failed to delete user'
                }), 500
            
            return jsonify({
                'success': True,
                'message': 'User deleted successfully'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
