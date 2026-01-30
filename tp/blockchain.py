from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.ajout_du_premier_block()]

    def ajout_du_premier_block(self):
        return Block(0, "Block zero", "0", signature="Block de depart")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        last_block = self.get_latest_block()

        if new_block.previous_hash != last_block.hash:
            return False

        if new_block.index != last_block.index + 1:
            return False

        self.chain.append(new_block)
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.previous_hash != previous_block.hash:
                print(f"Lien cassé au bloc {i}")
                return False

            if current_block.hash != current_block.calcul_de_hash():
                print(f"Le bloc {i} a été modifié frauduleusement")
                return False

        return True

    def __repr__(self):
        MAGENTA = '\033[95m'
        BOLD = '\033[1m'
        ENDC = '\033[0m'
        affichage = "\n" + MAGENTA + "="*60 + ENDC + "\n"
        affichage += f"""{BOLD} {'AFFICHAGE DE TOUTE LA BLOCKCHAIN'.center(50)} {ENDC} ({len(self.chain)} blocs)\n"""
        affichage += MAGENTA + "="*60 + ENDC + "\n"

        for bloc in self.chain:
            affichage += str(bloc)  + "\n"
            affichage += MAGENTA + "-" * 60 + ENDC + "\n"
        return affichage
