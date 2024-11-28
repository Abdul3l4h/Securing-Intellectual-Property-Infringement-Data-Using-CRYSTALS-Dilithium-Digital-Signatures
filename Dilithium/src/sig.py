# Signature Python example

import oqs
from pprint import pprint
import os

def read_file(filename):
    with open(filename,'rb') as f:
        return f.read()

def write_file(filename,data):
    with open(filename,'wb') as f:
        f.write(data)

print("liboqs version:", oqs.oqs_version())
print("liboqs-python version:", oqs.oqs_python_version())
print("Enabled signature mechanisms:")
sigs = oqs.get_enabled_sig_mechanisms()
pprint(sigs, compact=True)

#message = "This is the message to sign".encode()
# Create signer and verifier with sample signature mechanisms
def sign_file(filename,pub_key_path,priv_key_path,signature_file):

    message = read_file(filename)
    print(f"\nOriginal file size: {len(message)} bytes")
    sigalg = "Dilithium2"
    with oqs.Signature(sigalg) as signer:
        print("\nSignature details:")
        pprint(signer.details)

        # Signer generates its keypair
        signer_public_key = signer.generate_keypair()
        signer_private_key = signer.export_secret_key()
        # Optionally, the secret key can be obtained by calling export_secret_key()
        # and the signer can later be re-instantiated with the key pair:
        # secret_key = signer.export_secret_key()

        # Store key pair, wait... (session resumption):
        # signer = oqs.Signature(sigalg, secret_key)
        # Signer signs the message
        signature = signer.sign(message)
        print(f"Generated signature size: {len(signature)} bytes")
        write_file(pub_key_path, signer_public_key)
        write_file(priv_key_path,signer_private_key)
        write_file(signature_file,signature)

        # Verifier verifies the signature
        # is_valid = verifier.verify(message, signature, signer_public_key)

        # print("\nValid signature?", is_valid)

def verify_signature(filename, pub_key_path,signature_file):
    message = read_file(filename)
    public_key = read_file(pub_key_path)
    signature = read_file(signature_file)

    sigalg = "Dilithium2"

    with oqs.Signature(sigalg) as verifier:
        is_valid = verifier.verify(message, signature, public_key)
        print("\nValid signature?", is_valid)
        return is_valid


if __name__ == "__main__":
    filename = "../Test-Data/Infringement Data.txt"
    pub_key_path = "../Test-Data/pub_key.key"
    priv_key_path = "../Test-Data/private_key.key"
    signature_file = "../Test-Data/sigfile.sig"
    if not os.path.exists(filename):
        print(f"Error:{filename} not found")
    else:
        sign_file(filename,pub_key_path,priv_key_path, signature_file)
        verify_signature(filename,pub_key_path,signature_file)