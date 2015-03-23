# -*- coding: utf-8 -*-


class Config(object):
    MAIL_PORT = 32


class TestConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'DB': 'test'
    }


class ProdConfig(Config):
    """Production configuration."""
    DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    MONGODB_SETTINGS = {
        'DB': 'production'
    }
    MAIL_SUPPRESS_SEND = True


class DevConfig(Config):
    """Development configuration."""
    DEBUG = True
    MONGODB_SETTINGS = {
        'DB': 'development'
    }
    MAIL_SUPPRESS_SEND = True



