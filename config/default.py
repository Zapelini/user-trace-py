"""Main configuration module"""

import os


class Config:
    """
    Base configuration, this class contains most of the variables and default values.
    """
    DEBUG = False
    TESTING = False

    LOCAL_DATABASE_FILE = 'sqlite:///user_trace.db'
    IS_LOCAL_DATABASE = os.environ.get('DATABASE_URL') is None
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_DATABASE_FILE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """Configuration to be used on Production."""
    pass


class Development(Config):
    """Configuration to be used during development."""
    DEBUG = True


class Testing(Development):
    """Testing configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
