#from dbm import gnu
import json


class JSON():  # dans la vi il faut commenter surtout si on est en groupes
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_finaux, file):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux
        self.input_dict = ""
        self.auto_file = file

    def lire_json(self):  # retoune le JSON
        with open(self.auto_file, 'r') as input:
            self.input_dict = json.load(input)
        return self.input_dict

    def generer_json(self):
        contenu = json.dumps({
            "Etats": self.etats,
            "Alphabet": self.alphabet,
            "Transitions": self.transitions,
            "Etat initial": self.etat_initial,
            "Etats finaux": self.etats_finaux,
            "Layout": "spring"
        }, indent=4)
        print(contenu)
        with open(self.auto_file, "w") as fichier:
            fichier.write(contenu)
            fichier.close()
