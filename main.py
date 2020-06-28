"""
Primary entry-point for application
"""
from waitress import serve
from config import EnvConfig
from web_app.routes import app

env = EnvConfig()

if __name__ == 'main':
    serve(
        app,
        host=env.host,
        port=env.port
    )
