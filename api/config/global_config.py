from typing import Any

from pyaml_env import parse_config
import os

from api.config.singleton_meta import SingletonMeta


class Config:
    """

    Config is created from config.yml file consist of different properties related to Spark, Cerberus and etc.

    """

    def __init__(self, config_dict):
        if config_dict:
            self.__dict__.update(
                **{
                    k: v
                    for k, v in self.__class__.__dict__.items()
                    if "__" not in k and not callable(v)
                }
            )
            self.__dict__.update(**config_dict)
        self.__dict__ = self.__handle_inner_structures()

    def __handle_inner_structures(self):
        for k, v in self.__dict__.items():
            if isinstance(v, dict):
                self.__dict__[k] = Config(v)
        return self.__dict__

    def items(self) -> Any:
        return self.__dict__.items()

    def get(self, field_name: str, default=None) -> Any:
        return self.__dict__.get(field_name, default)

    def __getattr__(self, field_name: str) -> Any:
        return self.__dict__.get(field_name)


class GlobalConfig(Config, metaclass=SingletonMeta):
    def __init__(self):
        config_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "config.yml")
        )
        super().__init__(parse_config(config_path))
