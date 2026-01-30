from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("Génération des clés...")
key = RSA.generate(2048)
public_key = key.publickey()

message = b"Ceci est un test RSA simple."

cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
print(f"Message chiffré (hex) : {ciphertext.hex()[:40]}...")


decipher = PKCS1_OAEP.new(key)
plaintext = decipher.decrypt(ciphertext)
print(f"Message déchiffré : {plaintext.decode('utf-8')}")
