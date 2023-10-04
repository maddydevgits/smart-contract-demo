# WEB3 - Intermediate Software between Blockchain and Thirdparty Server
# Blockchain is a Server, web3 is now a client which connects with blockchain server

from web3 import Web3,HTTPProvider
import json

# from module importing a class (Web3)

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

try:
    contract,web3=connect_with_blockchain('0x502a7e8f45199464a2C024101e80564c9897817E')
    tx_hash=contract.functions.contestVote(2).transact()
    web3.eth.waitForTransactionReceipt(tx_hash) 

    contract,web3=connect_with_blockchain('0x502a7e8f45199464a2C024101e80564c9897817E')
    votes1,votes2,votes3=contract.functions.viewVotes().call()
    print('Votes1 for BJP: ',votes1)
    print('Votes for TDP + JSP: ',votes2)
    print('Votes for YSRCP: ',votes3)
except:
    print('Your vote has been polled already')
    contract,web3=connect_with_blockchain('0x502a7e8f45199464a2C024101e80564c9897817E')
    votes1,votes2,votes3=contract.functions.viewVotes().call()
    print('Votes1 for BJP: ',votes1)
    print('Votes for TDP + JSP: ',votes2)
    print('Votes for YSRCP: ',votes3)









