from flask import Flask
from app.config import config_by_name
from app.extensions import db, migrate, cors

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # 初始化扩展
    register_extensions(app)
    
    # 注册蓝图
    register_blueprints(app)
    
    return app

def register_extensions(app):
    """注册Flask扩展"""
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

def register_blueprints(app):
    """注册蓝图"""
    from app.api import api_bp
    from app.auth import auth_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth') 