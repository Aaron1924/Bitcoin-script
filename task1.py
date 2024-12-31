from bit import PrivateKeyTestnet
from bit import SUPPORTED_CURRENCIES
from bit.network import NetworkAPI
import requests
import time


my_key = PrivateKeyTestnet('cQhRgVqZKKYJpFHjJc6ARDGQUFXzRCdk38xEwVwFnQcERTXY1JHv')
print(my_key.to_wif())
print(my_key.address)
print(my_key.get_balance('satoshi'))
# print(my_key.get_transactions())   
#use utxo to create transaction
print(my_key.get_unspents())
# txid=my_key.create_transaction([('n2kvEFhZZnzaJu1QSFtp7ucb2gLXWkzGEt', 190, 'satoshi')])
# bit.Key.broadcast_tx_testnet(txid)
# print("successful")
# tx_hash = my_key.send([('mk779LgGoN9VbtssS2STRHwePoDMyErNzU', 0.001, 'usd')])
# print(tx_hash)

def verify_transaction_multiple(tx_hash):
    """Verify transaction using multiple testnet APIs"""
    # Updated API endpoints
    apis = {
        'Blockstream': f'https://blockstream.info/testnet/api/tx/{tx_hash}',
        'Mempool': f'https://mempool.space/testnet/api/tx/{tx_hash}',
        'BlockCypher': f'https://api.blockcypher.com/v1/btc/test3/txs/{tx_hash}',
        'Blockchain.info': f'https://api.blockchain.info/haskoin-store/btc-test/transaction/{tx_hash}',
        'Smartbit': f'https://testnet-api.smartbit.com.au/v1/blockchain/tx/{tx_hash}/hex',
    }
    
    success = False
    for api_name, url in apis.items():
        try:
            print(f"\nChecking {api_name}...")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✓ Transaction found on {api_name}")
                success = True
                break
        except requests.exceptions.RequestException as e:
            print(f"✗ Error with {api_name}: {str(e)}")
            continue
    
    return success

# Create and broadcast transaction
my_key = PrivateKeyTestnet('cQhRgVqZKKYJpFHjJc6ARDGQUFXzRCdk38xEwVwFnQcERTXY1JHv')
tx_hash = my_key.send([
    ('n2kvEFhZZnzaJu1QSFtp7ucb2gLXWkzGEt', 190, 'satoshi')
])
print(f"\nTransaction hash: {tx_hash}")

# Verify transaction with retries
max_attempts = 3
for attempt in range(max_attempts):
    print(f"\nVerification attempt {attempt + 1}/{max_attempts}")
    if verify_transaction_multiple(tx_hash):
        print("\nTransaction successfully verified!")
        break
    time.sleep(5)  # Wait 5 seconds between attempts
else:
    print("\nCould not verify transaction after multiple attempts")
# try:
#     # Create transaction
#     txid = my_key.create_transaction([
#         ('n2kvEFhZZnzaJu1QSFtp7ucb2gLXWkzGEt', 190, 'satoshi')
#     ])
    
#     # Broadcast transaction
#     NetworkAPI.broadcast_tx_testnet(txid)
#     print(f"Transaction broadcasted successfully: {txid}")
# except Exception as e:
#     print(f"Error broadcasting transaction: {e}")