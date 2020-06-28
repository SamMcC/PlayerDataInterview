"""
Config for main application, mostly ENV variables
"""
import os


class EnvConfig:
    @property
    def port(self):
        return str(os.environ.get('APP_PORT', 8080))

    @property
    def host(self):
        return str(os.environ.get('APP_HOST', 'localhost'))

    @property
    def debug_database(self):
        return bool(os.environ.get('DATABASE_LOGGING', False))

    @property
    def database_url(self):
        return str(os.environ.get('DATABASE_URL', 'sqlite:///:memory:'))
