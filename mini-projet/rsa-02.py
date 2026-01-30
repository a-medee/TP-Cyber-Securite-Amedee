# --- QUESTION 3.1.2 : Protocole Hybride (RSA + AES) ---
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

print("\n=== QUESTION 2 : Protocole Hybride (RSA + AES) ===")

bob_key = RSA.generate(2048)
bob_public = bob_key.publickey()

message_long = b"Etiam in dui aliquet, scelerisque sapien vitae, sodales quam. Duis eget congue leo. Duis vel nulla luctus, aliquet nisl in, euismod dui. Maecenas egestas ante ac magna auctor hendrerit."

session_key = get_random_bytes(16)

cipher_rsa = PKCS1_OAEP.new(bob_public)
enc_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_CBC)
ciphertext = cipher_aes.encrypt(pad(message_long, AES.block_size))

print("Alice a envoyé le paquet sécurisé.")

decipher_rsa = PKCS1_OAEP.new(bob_key)
recup_session_key = decipher_rsa.decrypt(enc_session_key)

decipher_aes = AES.new(recup_session_key, AES.MODE_CBC, cipher_aes.iv)
plaintext = unpad(decipher_aes.decrypt(ciphertext), AES.block_size)

print(f"Bob a lu : {plaintext.decode('utf-8')}")
