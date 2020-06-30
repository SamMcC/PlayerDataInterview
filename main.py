"""
Primary entry-point for application
"""
from waitress import serve
from config import EnvConfig
from db.database import Database
from web_app.routes import app

env = EnvConfig()

if __name__ == '__main__':
    if not env.environment == 'production':
        Database.init_db()
    serve(
        app,
        host=env.host,
        port=env.port
    )
