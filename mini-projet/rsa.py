from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from colorama import init, Fore, Style

init()

def demo():
    key = RSA.generate(2048)
    text = "Projet rsa"
    print(f"Document : {Fore.YELLOW}{text}{Style.RESET_ALL}")

    h = SHA256.new(text.encode('utf-8'))
    signature = pkcs1_15.new(key).sign(h)
    print(f"{Fore.GREEN}[+] Document signé.{Style.RESET_ALL}")

    print("\n--- Vérification ---")
    try:
        h_verif = SHA256.new(text.encode('utf-8'))
        pkcs1_15.new(key.publickey()).verify(h_verif, signature)
        print(f"{Fore.GREEN}[OK] Signature VALIDE.{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[ERREUR] Signature INVALIDE.{Style.RESET_ALL}")

    fake_text = "Je certifie que ce TP est NUL."
    print(f"Modification : {Fore.RED}{fake_text}{Style.RESET_ALL}")
    try:
        h_fake = SHA256.new(fake_text.encode('utf-8'))
        pkcs1_15.new(key.publickey()).verify(h_fake, signature)
    except:
        print(f"{Fore.GREEN}La falsification a été détectée (Signature rejetée).{Style.RESET_ALL}")

if __name__ == "__main__":
    demo()
