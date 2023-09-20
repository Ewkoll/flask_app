#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Description: 应用配置。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:11:52
LastEditTime: 2023-09-17 23:28:28
"""
from configparser import ConfigParser
from koca.utils import str_to_bool, make_path, CustomDict
import os
import logging

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = BASE_DIR + "/data"


class Config(CustomDict):
    def __init__(self):
        self.LOGGER_LEVEL = logging.WARNING
        self.APP_NAME = "Python Web App"
        self.CONFIG_FILENAME = ".config.ini"
        self.CONFIG_SECTION = None
        self.TOKEN_EXPIRE_TIME = 1000 * 60 * 15
        self.API_PACKAGE_NAME = "business"
        
        # Flask模板加载顺序，应用模板-插件模板-蓝图模板（根据蓝图顺序加载，同名蓝图优先使用第一个加载的文件）
        self.JSON_RECORD_LIMIT = 1000
        self.PRETTY_PRINT = False
        self.LOG_FUNC_INVOKE = False
        self.LOGGER_NAME = "log"
        self.LOGGER_PATH = "log"
        self.LOGGER_FORMAT = None
        self.ASYNC_LOGGING = True

        # python -c 'import secrets; print(secrets.token_hex())'
        self.SECRET_KEY = (
            os.environ.get("SECRET_KEY")
            or "2ad0caed25282cac639455ab2733acafffecf69e5af87a00791b7e439bb30727"
        )
        self.init_attr()
        self.load_config()

    def init_attr(self):
        self.APP_VERSION = "1.0.0"
        self.APP_EMAIL = "ideath@operatorworld.com"

    def load_config(self):
        config_path = os.path.join(BASE_DIR, self.CONFIG_FILENAME)
        config = ConfigParser()
        if config.read(config_path):
            self.SQLALCHEMY_DATABASE_URI = (
                self.load_string(config, "url") or self.SQLALCHEMY_DATABASE_URI
            )

    def load_string(self, config, key):
        if config.has_option(self.CONFIG_SECTION, key):
            return config.get(self.CONFIG_SECTION, key)

    def load_bool(self, config, key):
        if config.has_option(self.CONFIG_SECTION, key):
            return str_to_bool(config.get(self.CONFIG_SECTION, key))

    def load_config_section(self, section):
        config_path = os.path.join(BASE_DIR, self.CONFIG_FILENAME)
        config = ConfigParser()
        if config.read(config_path):
            if config.has_section(section):
                return dict(config.items(section))
        return None


class DevConfig(Config):
    def init_attr(self):
        super().init_attr()
        self.CONFIG_SECTION = "dev"
        self.DEBUG = True
        self.ENV = "development"
        self.PRETTY_PRINT = True
        self.LOGGER_LEVEL = logging.DEBUG
        self.SQLALCHEMY_ECHO = True
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
            DATA_DIR, "ewkoll-dev.sqlite"
        )


class ProConfig(Config):
    def init_attr(self):
        super().init_attr()
        self.CONFIG_SECTION = "pro"
        self.DEBUG = False
        self.ENV = "production"
        self.SQLALCHEMY_ECHO = False
        self.SQLALCHEMY_POOL_SIZE = 10
        self.SQLALCHEMY_POOL_TIMEOUT = 60
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
            DATA_DIR, "ewkoll-pro.sqlite"
        )


Config = {"development": DevConfig(), "production": ProConfig()}
