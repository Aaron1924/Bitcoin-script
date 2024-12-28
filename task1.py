from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import *
from bitcoinlib.keys import HDKey
# from bitcoin.rpc import RawProxy


# Account Details
PRIVATE_KEY = 'cQhRgVqZKKYJpFHjJc6ARDGQUFXzRCdk38xEwVwFnQcERTXY1JHv'
PUBLIC_KEY = '020fa6370c382c7fa18a81be242f4d855b9e3c3cf035f9a351e1998c8bc4d7a472'
ADDRESS = 'mnHSDQtXztz1BShbVzudWiSH3CuAfL12vk'
BALANCE = 0.17756  # in BTC
NETWORK = 'testnet'

# Delete existing wallet if exists
try:
    wallet = Wallet('testnet_wallet3')
    wallet.delete_wallet()
    print("Deleted existing wallet")
except:
    pass

# Create wallet with hardcoded private key
wallet = Wallet.create(
    'testnet_wallet7',
    keys=PRIVATE_KEY,
    network=NETWORK
)

# Verify wallet details
key = wallet.get_key()
print("Private key:", PRIVATE_KEY)
print("Public key:", PUBLIC_KEY) 
print("Bitcoin address:", ADDRESS)
print("Balance:", BALANCE, "BTC")

def create_txin(txid, output_index):
    """Create a transaction input (UTXO reference)"""
    return {"txid": txid, "output_n": output_index}

def create_txout(amount, destination_address):
    """Create a transaction output"""
    return {"address": destination_address, "value": int(amount * 1e8)}

def create_signed_transaction(txins, txouts, private_key):
    """Create and sign a transaction"""
    tx = Transaction(network=NETWORK)
    for txin in txins:
        tx.add_input(txin["txid"], txin["output_n"])
    for txout in txouts:
        tx.add_output(txout["value"], txout["address"])
    tx.sign(private_key)
    return tx.raw()

# def broadcast_tx(tx_hex):
#     """Broadcast transaction to Bitcoin testnet"""
#     bitcoinlib.transactions.broadcast(tx_hex)
#     print("Transaction broadcasted. TXID:", tx_hex)

# Create transaction input (UTXO)
txid = '7409a9e853050fbc200c2e35df39e5d06755f654252a1e5677a2e6112e0aa92f'
output_index = 0

txin = create_txin(txid, output_index)

# Create transaction output
destination_address = 'n2kvEFhZZnzaJu1QSFtp7ucb2gLXWkzGEt'
amount_to_send = 0.0000001

try:
    txout = create_txout(amount_to_send, destination_address)
except Exception as e:
    print("Error creating transaction output:", e)
    exit()

# Create and sign transaction
try:
    tx_hex = create_signed_transaction([txin], [txout], PRIVATE_KEY)
except Exception as e:
    print("Error signing the transaction:", e)
    exit()

# Broadcast transaction
# try:
#     broadcast_tx(tx_hex)
# except Exception as e:
#     print("Error broadcasting the transaction:", e)
