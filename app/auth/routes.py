from flask import request, jsonify
from app.auth import auth_bp
from app.auth.services import authenticate_user, register_user
from app.common.utils import success_response, error_response

@auth_bp.route('/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    
    if not data:
        return error_response(message="无效的请求数据", status_code=400)
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return error_response(message="用户名和密码不能为空", status_code=400)
    
    # 在实际应用中，这里应该调用数据库验证用户
    token = authenticate_user(username, password)
    
    if not token:
        return error_response(message="用户名或密码错误", status_code=401)
    
    return success_response(
        data={"token": token, "username": username},
        message="登录成功"
    )

@auth_bp.route('/register', methods=['POST'])
def register():
    """用户注册"""
    data = request.get_json()
    
    if not data:
        return error_response(message="无效的请求数据", status_code=400)
    
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    if not username or not password or not email:
        return error_response(message="用户名、密码和邮箱不能为空", status_code=400)
    
    # 在实际应用中，这里应该将用户信息保存到数据库
    success = register_user(username, password, email)
    
    if not success:
        return error_response(message="注册失败，用户名或邮箱已存在", status_code=409)
    
    return success_response(message="注册成功", status_code=201) 