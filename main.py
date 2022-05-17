from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv() # load ENV variables

URL = f"https://eth-rinkeby.alchemyapi.io/v2/{os.getenv('ALCHEMY_KEY')}"


if __name__ == '__main__':
    w3 = Web3(HTTPProvider(URL))
    print(w3.isConnected())
