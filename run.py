import os
from dotenv import load_dotenv
from app import create_app

# 加载环境变量
load_dotenv()

# 创建应用实例
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # 启动应用
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 