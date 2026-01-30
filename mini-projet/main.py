import sys
from colorama import init, Fore, Style

# Import des modules créés juste avant
import projet_hybride
import projet_signature

init()

def main():
    while True:
        print("\n" + "="*35)
        print(f"{Fore.CYAN}   MENU MINI-PROJETS CRYPTO{Style.RESET_ALL}")
        print("="*35)
        print("1. Chiffrement Hybride (RSA + AES)")
        print("2. Signature Numérique")
        print("3. Diffie-Hellman")
        print(f"{Fore.RED}4. Quitter{Style.RESET_ALL}")
        choix = input("\nVotre choix : ")

        if choix == '1':
            projet_hybride.demo()
        elif choix == '2':
            projet_signature.demo()
        elif choix == '3':
            projet_diffie_hellman.demo()
        elif choix == '4':
            print("Au revoir.")
            sys.exit()
        else:
            print("Choix invalide.")
        input(f"\n{Style.DIM}Appuyez sur Entrée...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
