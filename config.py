"""
Config for main application
"""
import os


class EnvConfig:
    """
    Config based on ENV variables
    """
    @property
    def port(self):
        """
        Server port number
        """
        return int(os.environ.get('APP_PORT', 8080))

    @property
    def host(self):
        """
        Server hostname
        """
        return str(os.environ.get('APP_HOST', 'localhost'))

    @property
    def debug_database(self):
        """
        True if echo is enabled for SQLAlchemy, False otherwise
        """
        return bool(os.environ.get('DATABASE_LOGGING', False))

    @property
    def database_url(self):
        """
        Full database URL, e.g. mysql://admin:password123@192.168.1.5:8180
        """
        return str(os.environ.get('DATABASE_URL', 'sqlite:///:memory:'))

    @property
    def environment(self):
        """
        Environment in which the application is running (development/production)
        """
        return str(os.environ.get('ENVIRONMENT', 'development'))
