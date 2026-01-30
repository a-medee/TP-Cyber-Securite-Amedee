import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

def get_key_from_password(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

        with open(output_file, 'wb') as f:
            f.write(cipher.iv)
            f.write(ciphertext)

        print(f"\nFichier chiffré sauvegardé sous : {output_file}")

    except FileNotFoundError:
        print(f"\n[ERREUR] Le fichier '{input_file}' est introuvable.")
    except Exception as e:
        print(f"\n[ERREUR] {e}")

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(output_file, 'wb') as f:
            f.write(plaintext)

        print(f"\nFichier déchiffré sauvegardé sous : {output_file}")

    except ValueError:
        print("\n Mauvaise cle.")
    except FileNotFoundError:
        print(f"\nLe fichier '{input_file}' est introuvable.")

def main():
    while True:
        print("\n" + "="*30)
        print("   APPLICATION DE CHIFFREMENT")
        print("="*30)
        print("1. Chiffrer un fichier")
        print("2. Déchiffrer un fichier")
        print("3. Quitter")

        choix = input("\nVotre choix (1-3) : ")

        if choix == '3':
            print("Au revoir")
            break

        if choix in ['1', '2']:
            fichier_entree = input("Nom du fichier à traiter: ")

            if not os.path.exists(fichier_entree):
                print(f"Le fichier {fichier_entree} n'existe pas dans le dossier.")
                continue

            mot_de_passe = input("Cle de chiffrement : ")
            cle = get_key_from_password(mot_de_passe)

            if choix == '1':
                fichier_sortie = input("Nom du fichier de sortie : ")
                encrypt_file(fichier_entree, fichier_sortie, cle)

            elif choix == '2':
                fichier_sortie = input("Nom du fichier de sortie : ")
                decrypt_file(fichier_entree, fichier_sortie, cle)
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
