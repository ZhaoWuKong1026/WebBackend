"""
API 数据模式定义

这里可以定义数据验证和序列化的模式，如果使用marshmallow等库的话。
这个示例使用了简单的字典来模拟schema验证。
"""

resource_schema = {
    "id": {"type": "integer", "required": True},
    "name": {"type": "string", "required": True},
    "description": {"type": "string", "required": False},
    "created_at": {"type": "string", "format": "date-time", "required": False}
} 