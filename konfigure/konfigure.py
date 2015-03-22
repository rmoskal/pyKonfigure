__author__ = 'rob'
import os
import inspect
import importlib


class Konfigure:
    def __init__(self, mappings={"FLASK_ENV": "ENV"}, env_keys={'test': 'TestConfig',
                                                                'development': 'DevConfig',
                                                                'production': 'ProdConfig'},
                 settings_loc='settings'):

        self.config = {}

        env_var = find_env_mapping(mappings)
        env = "development"
        if env_var in os.environ:
            env = os.environ[env_var]

        print "loading %s" % env

        self.config = load_env_mapping(settings_loc, env, env_keys)
        merge_from_env(self.config, os.environ)

        setattr(self.config, "ENV", env)


def find_env_mapping(mappings):
    """
    Overrides the default mapping for the environment variable
    :param mappings:
    :return:
    """
    found = False
    for each in mappings.iteritems():
        if each[1] == "ENV":
            found = each[0]
            break
    if not found:
        raise KeyError("ENV mapping required")

    return found


def load_env_mapping(settings_loc, key, env_keys):
    """
    Instantiates an arbitrary set of popo configuration objects
    from a pointer to a settings module and a dictionary full of
    configuration classes as strings with the key as the environment
    {'development':'DevConfig'}
    :param settings_loc:
    :param key:
    :param env_keys:
    :return:
    """
    module = importlib.import_module(settings_loc)
    konfigs = {}
    for k, v in env_keys.iteritems():
        class_ = getattr(module, v)
        konfigs[k] = class_
    return _load_env_mapping(key, konfigs)



def _load_env_mapping(key, env_keys):
    """
    Instantiates an environment configuration by key
    :param key:
    :param env_keys:
    :return:
    """
    if key in env_keys:
        return env_keys[key]()
    raise KeyError("No %s configuration found" % key)


def merge_from_env(config, env):
    """

    :param config:
    :param env:
    :return:
    """
    attributes = inspect.getmembers(config, lambda a: not (inspect.isroutine(a)))
    attributes = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
    for each in attributes:
        if each[0] not in env:
            continue
        setattr(config, each[0], env[each[0]])


def merge_special_mappings(config, mappings, env):
    """

    :param config:
    :param mappings:
    :param env:
    :return:
    """
    for each in mappings.iteritems():
        if each[1] == "ENV":
            continue
        if each[0] not in env:
            continue
        setattr(config, each[1], env[each[0]])








