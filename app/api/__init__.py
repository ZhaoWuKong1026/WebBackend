from flask import Blueprint

api_bp = Blueprint('api', __name__)

# 导入路由以确保它们被注册
from app.api.v1 import routes 