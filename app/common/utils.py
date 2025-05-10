from flask import jsonify

def success_response(data=None, message="成功", status_code=200):
    """
    返回统一的成功响应格式
    """
    response = {
        "success": True,
        "message": message
    }
    
    if data is not None:
        response["data"] = data
    
    return jsonify(response), status_code

def error_response(message="错误", errors=None, status_code=400):
    """
    返回统一的错误响应格式
    """
    response = {
        "success": False,
        "message": message
    }
    
    if errors is not None:
        response["errors"] = errors
    
    return jsonify(response), status_code

def validate_request_data(data, schema):
    """
    验证请求数据是否符合指定的模式
    这是一个简单实现，实际项目可以使用marshmallow等库
    """
    errors = {}
    
    for field, rules in schema.items():
        # 检查必填字段
        if rules.get('required', False) and field not in data:
            errors[field] = f"{field}是必填项"
            continue
            
        if field not in data:
            continue
            
        # 检查类型
        field_type = rules.get('type')
        if field_type == 'string' and not isinstance(data[field], str):
            errors[field] = f"{field}必须是字符串"
        elif field_type == 'integer' and not isinstance(data[field], int):
            errors[field] = f"{field}必须是整数"
        # 可以添加更多类型的验证
    
    return len(errors) == 0, errors 