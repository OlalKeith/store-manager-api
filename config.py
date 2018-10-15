# import os
class Config(object):
    """Parent configuration class"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration """
    TESTING = True


app_config = {

    'testing': TestingConfig
}
