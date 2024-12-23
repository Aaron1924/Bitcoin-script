from bitcoin import *  # Import all functions from the bitcoin library
from bitcoin.main import random_key, encode_privkey, privtopub  # Import the random_key, encode_privkey, and privtopub functions explicitly


# Generate a random private key
private_key = random_key()
print("Private Key (hex):", private_key)

# Save the private key in WIF format (for broader compatibility)
private_key_wif = encode_privkey(private_key, 'wif_testnet') # Use wif_testnet for testnet
print("Private Key (WIF):", private_key_wif)

# Derive the public key
public_key = privtopub(private_key)
print("Public Key (hex):", public_key)

# Create a P2PKH testnet address
testnet_address = pubtoaddr(public_key, 111)  # 111 is the testnet address prefix
print("Testnet Address:", testnet_address)