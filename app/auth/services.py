import jwt
import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.auth.models import User

def authenticate_user(username, password):
    """
    验证用户并生成JWT令牌
    
    在实际应用中，这里应当从数据库查询用户信息
    这是一个模拟实现
    """
    # 示例用户 - 在实际应用中会从数据库获取
    if username == "admin" and password == "password":
        return generate_token(username)
    return None

def register_user(username, password, email):
    """
    注册新用户
    
    在实际应用中，这里应该检查用户是否已存在，然后将新用户保存到数据库
    这是一个模拟实现
    """
    # 示例实现 - 在实际应用中会保存到数据库
    if username == "existing_user":
        return False
    return True

def generate_token(username):
    """生成JWT令牌"""
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow(),
        'sub': username
    }
    return jwt.encode(
        payload,
        os.getenv('SECRET_KEY', 'dev-key'),
        algorithm='HS256'
    )

def decode_token(token):
    """解码JWT令牌"""
    try:
        payload = jwt.decode(
            token,
            os.getenv('SECRET_KEY', 'dev-key'),
            algorithms=['HS256']
        )
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None 