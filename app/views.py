from app import app
from flask import render_template, session, jsonify
from app.service import get_nft_img_url, create_tr_mint_nft

@app.route('/')
def index():
    return render_template("home.html", nfts_img={
        'rock_url': get_nft_img_url('Rock'),
        'paper_url': get_nft_img_url('Paper'),
        'scissors_url': get_nft_img_url('Scissors')
    })
    # return render_template("home.html", nfts_img={
    #     'rock_url': "https://ipfs.io/ipfs/bafkreibe6myordolezhyk5m5r76dkitmdq2mopn44thd4m3kxmd3ma4cza",
    #     'paper_url': "https://ipfs.io/ipfs/bafkreifkn3whx5ntbxjj3vwrhtxjktzqx35gjsp2c3fceuuanwo57bl72u",
    #     'scissors_url': "https://ipfs.io/ipfs/bafkreiax5x6sxnr466akmtvybwcprblcstioji5pe6aw5bfnwsq4wk2o3e"
    # })

@app.get('/set_wallet/<wallet_address>')
def set_wallet_session(wallet_address):
    session['wallet_address'] = wallet_address
    return 'OK'


@app.post('/mint/<name>')
def mint(name):
    tr = create_tr_mint_nft(
        from_address=session['wallet_address'],
        name=name
    )
    return jsonify(tr)
