#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import BTC

import json

# HDWallet seed
SEED = "b3337a2fe409afbb257b504e4c09d36b57c32c452b71a0ed413298a5172f727a06bf660548" \
       "8723bc545a4bd51f5cd29a3e8bd1433bd1d26e6bf866ff53d1493f"

# Initialize hdwallet
hdwallet = HDWallet(symbol=BTC)
# Get Bitcoin hdwallet from seed
hdwallet.from_seed(seed=SEED)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all hdwallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Seed:", hdwallet.seed())
print("Root XPrivate Key:", hdwallet.root_xprivate_key())
print("Root XPublic Key:", hdwallet.root_xpublic_key())
print("XPrivate Key:", hdwallet.xprivate_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Path:", hdwallet.path())
print("Address:", hdwallet.address())