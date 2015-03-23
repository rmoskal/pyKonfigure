##pyKonfigure
I like to deploy to PAAS providers like heroku and like an easy way to support getting configuration variables from the application environment.
Plus I've been using the same basic code for all my flask applications, supporting different configuration environments by having a POPO per environment
(test, development, production, etc).  You can have as many environments as you want and what they mean is up to you.  A common base class can be used to for settings
that are the same in each.

Here's an example settings file:

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

There are 3 configuration classes and a base class. This is how you create an instance of pyKonfigure:

    cfg = Konfigure( mappings={"FLASK_ENV": "ENV"},
         env_keys={'test': 'TestConfig','development': 'DevConfig','production': 'ProdConfig'},
         settings_loc='settings')
         
those happen to be all the default values.  Starting from the end settings_loc is a string identifying the module containing the 
above configuration fle.  env_keys map each environment to a class containing its settings and mappings is a list of 
        