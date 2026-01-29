#! /usr/bin/python3
from Crypto.Hash import SHA256
import time

class Block:
    def __init__(self, index, data, previous_hash, signature):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.signature = signature
        self.hash = self.calcul_de_hash()

    def calcul_de_hash(self):
        section_to_be_harshed = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.signature}"

        # hachage SHA256
        hasher = SHA256.new()
        hasher.update(section_to_be_harshed.encode('utf-8'))

        # résultat en hexadécimal
        return hasher.hexdigest()

    def __repr__(self):
        CYAN = '\033[96m'   # Pour les clés (Index, Hash...)
        GREEN = '\033[92m'  # Pour les valeurs importantes
        YELLOW = '\033[93m' # Pour la date
        ENDC = '\033[0m'    # Pour réinitialiser
        BOLD = '\033[1m'

        return (f"""{CYAN}{BOLD}Index:{ENDC}       {self.index}\n{CYAN}{BOLD}Heure:{ENDC}{YELLOW}{self.timestamp}{ENDC}\n{CYAN}{BOLD}Data:{ENDC}        {self.data}\n{CYAN}{BOLD}Hash:{ENDC}        {GREEN}{self.hash}{ENDC}\n{CYAN}{BOLD}Prev Hash:{ENDC}   {self.previous_hash}\n{CYAN}{BOLD}Signature:{ENDC}   {self.signature}""")

if __name__ == "__main__":
    debut = Block(0, "Test de debut", None, None)
    print(debut)
