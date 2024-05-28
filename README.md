
# Solana Keypair Generator from Mnemonic

This project demonstrates how to generate multiple Solana keypairs from a mnemonic phrase using Python. The keypairs are derived using the BIP44 standard derivation path.

## Prerequisites

Before running the script, you need to install the required libraries:

```bash
pip install solders mnemonic bip_utils base58
```

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/solana-keypair-generator.git
   cd solana-keypair-generator
   ```

2. **Edit the Script**

   Open the `generate_keypairs.py` file and replace `"your twelve word mnemonic phrase here"` with your own mnemonic phrase.

3. **Run the Script**

   ```bash
   python generate_keypairs.py
   ```

## Script

The script generates a specified number of keypairs from the provided mnemonic and prints their details. Each keypair includes the public key, private key, and a JSON formatted private key for easy import into Phantom wallet.

```python
from bip_utils import Bip39SeedGenerator, Bip44Coins
from solders.keypair import Keypair
from mnemonic import Mnemonic
import json
import base58

# Provided mnemonic
mnemonic = "your twelve word mnemonic phrase here"
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
```

## Output

The script will output the public and private keys for each keypair in the following format:

```
Address 0: <public_key_base58>
Public Key 0: <public_key_base58>
Private Key 0: <private_key_list>
Private Key JSON 0 for Phantom: <private_key_json>

Address 1: <public_key_base58>
Public Key 1: <public_key_base58>
Private Key 1: <private_key_list>
Private Key JSON 1 for Phantom: <private_key_json>
...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
