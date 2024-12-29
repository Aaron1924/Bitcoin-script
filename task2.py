import hashlib
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2SHBitcoinAddress
from bitcoin.core.script import CScript, CScriptWitness, OP_0, OP_2, OP_CHECKMULTISIG
import random
import os

private_key1 = CBitcoinSecret.from_secret_bytes(os.urandom(32))
private_key2 = CBitcoinSecret.from_secret_bytes(os.urandom(32))

public_key1 = private_key1.pub
public_key2 = private_key2.pub

print("Public Key 1: ", public_key1)
print("Public Key 2: ", public_key2)
redeem_script = CScript([OP_2, public_key1, public_key2, OP_2, OP_CHECKMULTISIG])
address = P2SHBitcoinAddress.from_redeemScript(redeem_script)
print("Address: ", address)

print("Redeem Script: ", redeem_script.hex())
print("Private Key 1: ", private_key1)
print("Private Key 2: ", private_key2)


