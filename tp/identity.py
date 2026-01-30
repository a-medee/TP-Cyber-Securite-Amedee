from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

class Identity:
    def __init__(self):
        # Generation de cles paire de clés
        self.key_pair = RSA.generate(1024)

    def cle_public(self):
        return self.key_pair.publickey().export_key().decode('utf-8')

    def signature_de_donnee(self, data):
        h = SHA256.new(data.encode('utf-8'))
        signature = pkcs1_15.new(self.key_pair).sign(h)

        return binascii.hexlify(signature).decode('utf-8')

    def __repr__(self):
        return (f"Cle publique:\n {self.key_pair.public_key().exportKey().decode('utf-8')}")

    @staticmethod
    def verification_de_signature(data_string, signature_hex, public_key_pem):
        try:
            data_hash = SHA256.new(data_string.encode('utf-8'))
            signature = binascii.unhexlify(signature_hex)
            key = RSA.import_key(public_key_pem)
            pkcs1_15.new(key).verify(data_hash, signature)
            return True
        except (ValueError, TypeError):
            return False
