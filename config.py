import os

import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    dotenv.load_dotenv()

    remote_url: str = os.getenv('URL')
    # USERNAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESSKEY')
    timeout: float = 10.0
    USR: str = os.getenv('USER_NAME')


config = Config()
