from flask import Flask,render_template,request,session
from web3 import Web3,HTTPProvider
import json

blockchainServer='http://127.0.0.1:7545'

# artifact
artifactPath='../build/contracts/election.json'

def connect_with_blockchain(walletAddress):
    web3=Web3(HTTPProvider(blockchainServer))
    web3.eth.defaultAccount=walletAddress

    with open(artifactPath) as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)

    return (contract,web3)

frontend=Flask(__name__)
frontend.secret_key='m@dhu'

@frontend.route('/')
def homePage():
    return render_template('index.html')

@frontend.route('/submitWalletAddress',methods=['post'])
def submitWalletAddress():
    walletAddress=request.form['walletaddress']
    session['username']=walletAddress
    return render_template('index.html',result1='Wallet Address Added')

@frontend.route('/result')
def resultPage():
    contract,web3=connect_with_blockchain('0x82CDaAdC2b2aB7a80eBdf59278C33A962C9fca4d')
    votes1,votes2,votes3=contract.functions.viewVotes().call()
    return render_template('result.html',votes1=votes1,votes2=votes2,votes3=votes3)

@frontend.route('/vote/<id>')
def castVote(id):
    id=int(id)
    if id==1:
        try:
            contract,web3=connect_with_blockchain(session['username'])
            tx_hash=contract.functions.contestVote(id).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            return render_template('index.html',result='You have polled for BJP Party')
        except:
            return render_template('index.html',result='You have already polled')
    elif id==2:
        try:
            contract,web3=connect_with_blockchain(session['username'])
            tx_hash=contract.functions.contestVote(id).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            return render_template('index.html',result='You have polled for JSP Party')
        except:
            return render_template('index.html',result='You have already polled')
    elif id==3:
        try:
            contract,web3=connect_with_blockchain(session['username'])
            tx_hash=contract.functions.contestVote(id).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            return render_template('index.html',result='You have polled for YSRCP Party')
        except:
            return render_template('index.html',result='You have already polled')


if __name__=="__main__":
    frontend.run(host='0.0.0.0',debug=True,port=5001)