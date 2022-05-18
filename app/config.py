"""All configs of app"""

import os
from pathlib import Path

BASE_DIR = Path("app").absolute()

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', default=str(os.urandom(24)))
    WEB3_ALCHEMY_PROJECT_ID = os.environ.get('WEB3_ALCHEMY_PROJECT_ID')
    WEB3_URL = f"https://eth-rinkeby.alchemyapi.io/v2/{WEB3_ALCHEMY_PROJECT_ID}"
    ACCOUNT_PRIVATE_KEY = os.environ.get('ACCOUNT_PRIVATE_KEY')
    ACCOUNT_ADDRESS = os.environ.get('ACCOUNT_ADDRESS')
    CONTRACT_ADDRESS = os.environ.get('CONTRACT_ADDRESS')
