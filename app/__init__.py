from flask import Flask
from dotenv import load_dotenv
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from app.config import Config, BASE_DIR
import json

load_dotenv() # load ENV variables

# Init App
app = Flask(__name__)
app.config.from_object(Config)

# Init WEB3
w3 = Web3(HTTPProvider(app.config['WEB3_URL']))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Init Contact
with open(BASE_DIR / 'static' / 'abi.json', 'r') as abi_file:
    abi = json.load(abi_file)
contract = w3.eth.contract(address=app.config['CONTRACT_ADDRESS'],abi=abi)

from app import views
