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
#print("Enabled signature mechanisms:")
sigs = oqs.get_enabled_sig_mechanisms()
#pprint(sigs, compact=True)

# Create signer and verifier with sample signature mechanisms
def sign_file(filename, pub_key_path, priv_key_path, signed_file):

    message = read_file(filename)
    print(f"\nOriginal file size: {len(message)} bytes")
    sigalg = "Dilithium2"
    with oqs.Signature(sigalg) as signer:
        print("\nSignature details:")
        pprint(signer.details)
        
        # Signer generates its keypair
        signer_public_key = signer.generate_keypair()
        signer_private_key = signer.export_secret_key()
        signature = signer.sign(message)
        print(f"Generated signature size: {len(signature)} bytes")

        write_file(pub_key_path, signer_public_key)
        write_file(priv_key_path,signer_private_key)
        write_file(signed_file,signature)

def verify_signature(filename, pub_key_path, signed_file):
    message = read_file(filename)
    public_key = read_file(pub_key_path)
    signature = read_file(signed_file)
    sigalg = "Dilithium2"

    with oqs.Signature(sigalg) as verifier:
        is_valid = verifier.verify(message, signature, public_key)
        print("\nIs the signature verified and validated?", is_valid)
        return is_valid

def owner_update(filename, priv_key_path, new_signature_filepath):
    message = read_file(filename)
    private_key = read_file(priv_key_path)

    sigalg = "Dilithium2"
    with oqs.Signature(sigalg,private_key) as signer:
        new_signature = signer.sign(message)
        write_file(new_signature_filepath,new_signature)


if __name__ == "__main__":
    filename = "../Test-Data/Infringement Data.txt"
    pub_key_path = "../Test-Data/pub_key.key"
    priv_key_path = "../Test-Data/private_key.key"
    signed_file = "../Test-Data/original_signed_file.sig"
    new_signature_filepath = "../Test-Data/new_signed_file.sig"
    modified_file = "../Test-Data/Modified_Infringement_Data.txt"
    if not os.path.exists(filename):
        print(f"Error:{filename} not found")
    else:
        #sign the file and save the public,privte keys and the signatures to the paths given
        sign_file(filename,pub_key_path,priv_key_path, signed_file)
        verify_signature(filename,pub_key_path,signed_file)

        #update file from owner update
        content = read_file(filename)
        new_content = content + b"Modified"
        write_file(modified_file,new_content)

        #update the signature with the same private key
        owner_update(modified_file,priv_key_path,new_signature_filepath)
        verify_signature(modified_file,pub_key_path,new_signature_filepath)