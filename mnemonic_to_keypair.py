from bip_utils import Bip39SeedGenerator, Bip44Coins
from solders.keypair import Keypair
from mnemonic import Mnemonic
import json
import base58

# Provided mnemonic
mnemonic = "mnemonic"
passphrase = ""  # Your passphrase if you have one

# Generate seed from mnemonic
mnemo = Mnemonic("english")
seed_bytes = mnemo.to_seed(mnemonic, passphrase)

# Number of keypairs to generate
num_keypairs = 5

for i in range(num_keypairs):
    # Define the derivation path for the current keypair
    derivation_path = f"m/44'/501'/0'/0/{i}"

    # Generate keypair using the seed and derivation path
    keypair = Keypair.from_seed_and_derivation_path(seed_bytes[:64], derivation_path)

    # Get the public key
    public_key_bytes = bytes(keypair.pubkey())

    # Convert public key to base58 format
    public_key_base58 = base58.b58encode(public_key_bytes).decode('utf-8')

    # Convert private key to a list of integers (format expected by Phantom)
    private_key_list = keypair.to_bytes_array()[:32]

    # Print keys
    print(f"Address {i}: {public_key_base58}")
    print(f"Public Key {i}: {public_key_base58}")
    print(f"Private Key {i}: {private_key_list}")

    # Export private key in JSON format for Phantom
    private_key_json = json.dumps(private_key_list)
    print(f"Private Key JSON {i} for Phantom: {private_key_json}\n")
