import requests
from app import contract

def _get_metadata_from_url(url):
    return requests.get(url).json()


def get_nft_img_url(name):
    
    _get_metadata_from_url
    
    if name == 'Rock': id = contract.functions.Rock().call()
    if name == 'Paper': id = contract.functions.Paper().call()
    if name == 'Scissors': id = contract.functions.Scissors().call()
        
    metadata = _get_metadata_from_url(contract.functions.uri(id).call())
    
    return metadata['image']
