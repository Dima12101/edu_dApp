from app import app
from flask import render_template
from app.service import get_nft_img_url

@app.route('/')
def index():
    return render_template("home.html", nfts_img={
        'rock_url': get_nft_img_url('Rock'),
        'paper_url': get_nft_img_url('Paper'),
        'scissors_url': get_nft_img_url('Scissors')
    })
