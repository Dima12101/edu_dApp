import requests
from app import contract, w3
from flask import abort, Response
from json import dumps
from web3.exceptions import ContractLogicError

def _get_metadata_from_url(url):
    return requests.get(url).json()


def get_nft_img_url(name):
    
    _get_metadata_from_url
    
    if name == 'Rock': id = contract.functions.Rock().call()
    if name == 'Paper': id = contract.functions.Paper().call()
    if name == 'Scissors': id = contract.functions.Scissors().call()
        
    metadata = _get_metadata_from_url(contract.functions.uri(id).call())
    
    return metadata['image']

def create_tr_mint_nft(from_address, name):
    if name == 'Rock': func = contract.functions.mintRock
    if name == 'Paper': func = contract.functions.mintPaper
    if name == 'Scissors': func = contract.functions.mintScissors
    
    from_address = w3.toChecksumAddress(from_address)
    nonce = w3.toHex(w3.eth.getTransactionCount(from_address))
    
    try:
        tr = func().buildTransaction({'nonce': nonce, 'from': from_address})
    except ContractLogicError as err:
        # error_message = dumps({'Message':  str(err)})
        abort(Response(str(err), 400))
    
    # tr['value'] = w3.toHex(w3.toWei(0.0001, 'ether')) # TODO
    tr['gas'] = w3.toHex(tr['gas'])
    tr['maxFeePerGas'] = w3.toHex(tr['maxFeePerGas'])
    tr['maxPriorityFeePerGas'] = w3.toHex(tr['maxPriorityFeePerGas'])
    return tr
