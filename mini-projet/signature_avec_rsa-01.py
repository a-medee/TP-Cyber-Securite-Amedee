from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

key = RSA.generate(2048)
public_key = key.publickey()

message_texte = "Fusce dapibus semper libero vitae vehicula."
print(f"Message original : {message_texte}")

m = bytes_to_long(message_texte.encode('utf-8'))

signature = pow(m, key.d, key.n)
print(f"Signature générée (nombre) : {str(signature)[:30]}...")

m_verif_int = pow(signature, public_key.e, public_key.n)
message_verifie = long_to_bytes(m_verif_int).decode('utf-8')
print(f"Message vérifié  : {message_verifie}")

if message_texte == message_verifie:
    print("La signature est valide.")
else:
    print("Signature invalide.")
