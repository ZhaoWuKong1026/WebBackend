# Flask后端项目

一个使用Flask框架的后端项目，采用蓝图结构组织代码。

## 项目结构

```
/project_name
    /app
        /__init__.py    - Flask应用初始化
        /config.py      - 配置文件
        /extensions.py  - 扩展初始化
        /api            - API相关模块
            /__init__.py
            /v1         - API版本1
                /__init__.py
                /routes.py    - API路由
                /schemas.py   - 数据验证模式
        /auth           - 认证相关模块
            /__init__.py
            /models.py  - 用户模型
            /routes.py  - 认证路由
            /services.py - 认证服务
        /common         - 通用功能模块
            /__init__.py
            /utils.py   - 工具函数
        /static         - 静态文件
        /templates      - HTML模板
    requirements.txt    - 依赖包
    run.py             - 启动脚本
```

## 安装与使用

1. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建一个`.env`文件，包含以下内容：
```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key-replace-me
```

4. 初始化数据库
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. 运行应用
```bash
flask run
# 或者
python run.py
```

## API端点

### 认证相关

- POST /auth/login - 用户登录
- POST /auth/register - 用户注册

### API相关

- GET /api/v1/health - 健康检查
- GET /api/v1/resources - 获取资源列表
- GET /api/v1/resources/{id} - 获取单个资源 