import hashlib
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2SHBitcoinAddress, CBitcoinAddress
from bitcoin.core import CMutableOutPoint, CMutableTxIn, CMutableTxOut, CTransaction, COutPoint, COIN, lx
from bitcoin.core.script import CScript, CScriptWitness, OP_0, OP_2, OP_CHECKMULTISIG, OP_CHECKSIG
import random
import os

SelectParams('testnet')

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
amount = int(1 * COIN)
amount_less_fee = amount *0.99 
txid ='e8f580dea89b5e8158a2e309fc0377d9333ecf0d1ec100a5d6e8f102ecfab65a'
output_index = 0
txin = create_txin(txid,output_index)





