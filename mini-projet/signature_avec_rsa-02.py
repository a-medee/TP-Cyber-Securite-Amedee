from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


key = RSA.generate(2048)
public_key = key.publickey()

message = b"Duis vel nulla luctus, aliquet nisl in, euismod dui"
print(f"Document : {message.decode()}")

h = SHA256.new(message)
print(f"Empreinte (Hash) : {h.hexdigest()}")

signature = pkcs1_15.new(key).sign(h)
print("Signature cryptographique générée.")

print("\n--- Test de validité ---")
try:
    h_verif = SHA256.new(message)
    pkcs1_15.new(public_key).verify(h_verif, signature)
    print("La signature est VALIDE. Le document est authentique.")
except (ValueError, TypeError):
    print("La signature est INVALIDE.")

    print("\n--- Test de falsification (Hacker) ---")
    message_faux = b"Ceci est un contrat important signe numeriquement." + b" (Modifie par hacker)"

    try:
        h_fake = SHA256.new(message_faux)
        pkcs1_15.new(public_key).verify(h_fake, signature) # On essaie de valider le faux message avec la vraie signature
        print("Faux positif")
    except (ValueError, TypeError):
        print(f"[SUCCÈS] Le système a détecté la modification du fichier '{message_faux.decode()}'")
