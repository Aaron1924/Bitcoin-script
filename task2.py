import hashlib
import requests
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2SHBitcoinAddress, CBitcoinAddress
from bitcoin.core import CMutableOutPoint, CMutableTxIn, CMutableTxOut, CTransaction, COutPoint, CMutableTransaction, COIN, lx, b2x
from bitcoin.core.script import CScript, CScriptWitness, SIGHASH_ALL, SignatureHash, OP_0, OP_2, OP_CHECKMULTISIG, OP_CHECKSIG
import random
import os

# Set the URL for the testnet blockchain
url = 'https://blockstream.info/testnet/api/tx/send'

SelectParams('testnet')
# Generate two private key using string as seed
# Users have to remember the seed to recover the private keys
private_key1 = CBitcoinSecret.from_secret_bytes(hashlib.sha256(b'bench horn couple biology stem shove salad first').digest())
private_key2 = CBitcoinSecret.from_secret_bytes(hashlib.sha256(b'bench horn couple biology stem shove salad second').digest())

public_key1 = private_key1.pub
public_key2 = private_key2.pub


print("Public Key 1: ", public_key1)
print("Public Key 2: ", public_key2)
redeem_script = CScript([OP_2, public_key1, public_key2, OP_2, OP_CHECKMULTISIG])
address = P2SHBitcoinAddress.from_redeemScript(redeem_script)
print("Address: ", str(address))

print("Redeem Script: ", redeem_script.hex())
print("Private Key 1: ", private_key1)
print("Private Key 2: ", private_key2)

def create_txin(txid,output_index):
    return CMutableTxIn(COutPoint(lx(txid), output_index))

def create_txout(amount, destination_address):
    return CMutableTxOut(amount, CBitcoinAddress(destination_address).to_scriptPubKey())

def create_signed_transaction(txin, txout, private_key1, private_key2, redeem_script):
    # create unsigned transaction
    tx = CMutableTransaction([txin],[txout])
    # calculate signature hash for this transaction
    sigHash = SignatureHash(
        script = redeem_script,
        txTo = tx,
        inIdx = 0,
        hashtype = SIGHASH_ALL,
        amount = amount
    )

    # sign the transaction. Append the type of signature we want to the end of the signature hash (type:SIGHASH_ALL)
    sig1 = private_key1.sign(sigHash) + bytes([SIGHASH_ALL])
    sig2 = private_key2.sign(sigHash) + bytes([SIGHASH_ALL])

    # create the witness
    txin.scriptSig = CScript([sig1, sig2, redeem_script])
    return tx

def broadcast_tx(tx_hex):
    # broadcast the transaction
    None

amount = int(1 * COIN)
# Calculate an amount for the upcoming new UTXO that is 99% of the original amount
amount_less_fee = amount * 0.99 

#Create a transaction input (TXIN)
txid ='e8f580dea89b5e8158a2e309fc0377d9333ecf0d1ec100a5d6e8f102ecfab65a'
output_index = 0
txin = create_txin(txid,output_index)

#Create a transaction output to destination address (TXOUT)
destination_address = '2N8SSs85Zym1DRe1c6pTkx7iFhpzyfSVdfw'
txout = create_txout(amount_less_fee, destination_address)

tx = create_signed_transaction(txin, txout, private_key1, private_key2, redeem_script)

print(b2x(tx.serialize()))








