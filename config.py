import os

import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    dotenv.load_dotenv()
    remote_url: str = os.getenv('URL')
    USR: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESSKEY')
    timeout: float = 10.0
    android_platform_version: str = '9.0'
    android_device_name: str = 'Google Pixel 3'
    ios_platform_version: str = '13.0'
    ios_device_name: str = 'iPhone 11 Pro'
    browserstack_app_url: str = 'bs://sample.app'


config = Config()
