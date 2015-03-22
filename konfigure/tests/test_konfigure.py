import os
from nose.tools import raises
import unittest
import konfigure
from settings import DevConfig


class Test:
    FOO = "FOO"


class TestKonfigure(unittest.TestCase):
    def test_handles_special_environment_mapping(self):
        mapping = {"FOO": "ENV", "BAZ": "BAZ"}
        res = konfigure.find_env_mapping(mapping)
        assert res == "FOO"

    @raises(KeyError)
    def test_fails_when_mapping_undefined(self):
        mapping = {"FOO": "FOO", "BAZ": "BAZ"}
        konfigure.find_env_mapping(mapping)

    def test_maps_an_environment(self):
        configs = {"foo": Test}
        res = konfigure._load_env_mapping("foo", configs)
        assert isinstance(res, Test)

    @raises(KeyError)
    def test_fails_for_missing_environment(self):
        configs = {"foo": Test}
        konfigure._load_env_mapping("baz", configs)

    def test_override_with_environment_variable(self):
        env = {"FOO": "BAR"}
        config = Test()
        konfigure.merge_from_env(config, env)
        assert config.FOO == "BAR"

    def test_handle_special_remapping(self):
        mapping = {"SAM": "CRAM"}
        osenv = {"SAM": "YOU"}
        config = Test()
        konfigure.merge_special_mappings(config, mapping, osenv)
        assert config.CRAM == "YOU"

    def test_ignores_environment_in_special_mapping(self):
        mapping = {"SAM": "ENV"}
        osenv = {"SAM": "YOU"}
        config = Test()
        konfigure.merge_special_mappings(config, mapping, osenv)
        assert not hasattr(config, "ENV")

    def test_default_constructor_creates_development_config(self):
        res = konfigure.Konfigure()
        print res.config
        assert isinstance(res.config, DevConfig)
        assert res.config.ENV == "development"

    # def test_actually_read_os_env(self):
    #     os.environ["MAIL_PORT"] = "22"
    #     res = konfigure.Konfigure()
    #     assert res.config.MAIL_PORT == "22"









