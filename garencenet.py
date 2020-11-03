# account_one: aaron wallet = node1
# account_two: kyle wallet = node2
# send transaction from account_one to account_two


from web3 import Web3
from dotenv import load_dotenv
load_dotenv()
import os
from eth_account import Account 



w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) # to mak econnection with blockchain
print(w3.eth.blockNumber)

print(w3.eth.getBalance('0x78A47Ef95A669e53FFDBa941ceCfD71d459633F5')) # aaron wallet in garence net
print(w3.eth.getBalance('0x1c431Dc9B65A1bDC78c4a7ecc9eC05Aa292631F6')) # kyle wallet in garence net

private_key = os.getenv('AARON_PRIVATE_KEY') # which is account_one 
account_one=Account.from_key(private_key)


# create a function to create new transactions using parameters
# helper function to create a given transaction
def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

# Helper function to proceed sending the transaction
# tx: is the previous transaction we created in create_raw_tx function
# signed_tx: is the hash of transaction
# result: takes the raw signed transaction bites & send it to the node you are connected to
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()


send_tx(account_one, '0x1c431Dc9B65A1bDC78c4a7ecc9eC05Aa292631F6', 1000000000)