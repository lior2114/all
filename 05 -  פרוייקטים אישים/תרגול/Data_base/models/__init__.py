# Models package 
from .user_model import UserModel

def init_database():
    """Initialize all database tables"""
    UserModel.init_db() 
