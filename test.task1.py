from bit import PrivateKeyTestnet

my_key = PrivateKeyTestnet('cQhRgVqZKKYJpFHjJc6ARDGQUFXzRCdk38xEwVwFnQcERTXY1JHv')
print(my_key.version)
print("lol")
print(my_key.to_wif())
print(my_key.address)
tx_hash = my_key.send([('mk779LgGoN9VbtssS2STRHwePoDMyErNzU', 0.001, 'usd')])
print(tx_hash)