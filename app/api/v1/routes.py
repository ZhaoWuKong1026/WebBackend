from flask import jsonify, request
from app.api import api_bp
from app.api.v1.schemas import resource_schema
from app.common.utils import success_response, error_response

@api_bp.route('/v1/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({"status": "healthy", "version": "1.0.0"})

@api_bp.route('/v1/resources', methods=['GET'])
def get_resources():
    """获取资源列表"""
    # 这里应该从数据库获取数据
    resources = [
        {"id": 1, "name": "资源1"},
        {"id": 2, "name": "资源2"}
    ]
    return success_response(data=resources, message="获取资源成功")

@api_bp.route('/v1/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """获取单个资源"""
    # 这里应该从数据库获取数据
    resource = {"id": resource_id, "name": f"资源{resource_id}"}
    return success_response(data=resource, message="获取资源成功") 