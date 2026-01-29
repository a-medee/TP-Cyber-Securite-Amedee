#! /usr/bin/python3

import sys
import os
from block import Block
from identity import Identity
from blockchain import Blockchain

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"{Colors.HEADER}{Colors.BOLD}" + "="*50)
    print("                     TP CRYPTOGRAPHIE  ")
    print("="*50 + f"{Colors.ENDC}\n")

def menu():
    print("Initialisation de la blockchain...", end="")
    blockchain = Blockchain()
    wallet = Identity()
    print(f"{Colors.GREEN} OK {Colors.ENDC}")

    while True:
        clear_screen()
        print_header()

        print(f"{Colors.BLUE}Identité active :{Colors.ENDC} ...{wallet.cle_public()[-50:]}")
        print(f"{Colors.BLUE}Blocs dans la chaîne :{Colors.ENDC} {len(blockchain.chain)}")
        print("-" * 50)

        print("1. Créer une transaction")
        print("2. Voir toute la Blockchain")
        print("3. Vérifier l'intégrité de la chaîne")
        print("4.‍ Simulation d'attaque")
        print("5. Générer une nouvelle identité")
        print("6. Quitter")

        choice = input(f"\n{Colors.BOLD}Votre choix [1-6]: {Colors.ENDC}")

        if choice == '1':
            print(f"\n{Colors.HEADER}--- NOUVEAU BLOC ---{Colors.ENDC}")
            receiver = input("Destinataire : ")
            amount = input("Montant: ")

            transaction_data = f"Envoie de {amount} à {receiver}"
            signature = wallet.signature_de_donnee(transaction_data)

            last_block = blockchain.get_latest_block()
            new_index = last_block.index + 1
            previous_hash = last_block.hash

            new_block = Block(new_index, transaction_data, previous_hash, signature)

            if blockchain.add_block(new_block):
                print(f"\n{Colors.GREEN}Succès ! Bloc #{new_index} ajouté à la chaîne.{Colors.ENDC}")
            else:
                print(f"\n{Colors.FAIL}Erreur : Le bloc a été rejeté.{Colors.ENDC}")

            input("\nAppuyez sur Entrée pour continuer...")

        elif choice == '2':
            print(f"\n{Colors.HEADER}--- LE REGISTRE ---{Colors.ENDC}")
            print(blockchain)
            input("\nAppuyez sur Entrée pour continuer...")

        elif choice == '3':
            print(f"\n{Colors.HEADER}--- VERIFICATION DE SEC ---{Colors.ENDC}")
            if blockchain.is_chain_valid():
                print(f"{Colors.GREEN}La chaîne est VALIDE. Aucune modification détectée.{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}ALERTE : La chaîne est INVALIDE !{Colors.ENDC}")
                print("Astuce : Utilisez l'option 2 pour voir où les hashs ne correspondent plus.")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choice == '4':
            print(f"\n{Colors.HEADER}--- SIMULATION D'ATTAQUE ---{Colors.ENDC}")
            # On affiche la liste des index disponibles
            print(f"Index disponibles : de 0 à {len(blockchain.chain) - 1}")

            try:
                target_index = int(input(f"Quel numéro de bloc voulez-vous pirater ? : "))


                if 0 <= target_index < len(blockchain.chain):
                    target_block = blockchain.chain[target_index]

                    print(f"\n{Colors.BLUE}Donnée actuelle :{Colors.ENDC} {target_block.data}")
                    print(f"{Colors.BLUE}Hash actuel :{Colors.ENDC} {target_block.hash}")

                    new_data = input(f"\n{Colors.WARNING}Entrez la nouvelle donnée frauduleuse : {Colors.ENDC}")

                    blockchain.chain[target_index].data = new_data

                    print(f"\n{Colors.FAIL}PIRATAGE RÉUSSI !{Colors.ENDC}")
                    print(f"Le bloc #{target_index} contient maintenant : '{new_data}'")
                    print("Cependant, le hash n'a pas été mis à jour...")
                else:
                    print(f"{Colors.FAIL}Erreur : Ce bloc n'existe pas.{Colors.ENDC}")

            except ValueError:
                print(f"{Colors.FAIL}Erreur : Veuillez entrer un nombre entier.{Colors.ENDC}")

            input("\nAppuyez sur Entrée pour continuer...")

        elif choice == '5':
            wallet = Identity()
            print(f"\n{Colors.GREEN}Nouvelle paire de clés générée !{Colors.ENDC}")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choice == '6':
            print("Fermeture...")
            sys.exit()

if __name__ == "__main__":
    try:
        import Crypto
    except ImportError:
        print("Erreur: La librairie 'pycryptodome' manque.")
        sys.exit()
    menu()
