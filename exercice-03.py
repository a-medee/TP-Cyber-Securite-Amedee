from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


key = get_random_bytes(32)
message = b"Je n'aime pas le developpement web"
cipher = AES.new(key, AES.MODE_CBC)
message = pad(message, AES.block_size)
ciphertext = cipher.encrypt(message)
iv = cipher.iv

print(f"Cle en HEX: {key.hex()}")
print(f"IV:  {iv.hex()}")
print(f"Message crypté: {ciphertext.hex()}")


decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
message_decrypte = decrypt_cipher.decrypt(ciphertext)
message = unpad(message_decrypte, AES.block_size)
print(f"Message décrypté: {message.decode('utf-8')}")
