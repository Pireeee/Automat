#from dbm import gnu
import json


class JSON():  # dans la vi il faut commenter surtout si on est en groupes
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_finaux):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux
        self.input_dict = ""
        self.auto_file = 'nouveau_automate.json'

    def lire_json(self):  # retoune le JSON
        with open(self.auto_file, 'r') as input:
            self.input_dict = json.load(input)
        return self.input_dict

    # def get_input_dict(self):
    #    return self.input_dict

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
        with open("automate_input.json", "w") as fichier:
            fichier.write(contenu)
            fichier.close()


# def afficher_automate():

# def successors(dfa, state):
#   if state not in dfa.states:
#       print("error : le state specifié '" + state + "' ne fait pas partie de l'automate.")
#       return
#
#   ret = []
#   for (symbol, dst_state) in dfa.transitions[state]:
#       if dst_state not in ret:
#           ret.append(dst_state)
#
#   return ret

# def list_accessible(dfa):
#   visited = []
#   to_visit = [dfa.init]
#
#   while len(to_visit) > 0:
#       state = to_visit.pop()
#       visited.append(state)
#       for succ in successors(dfa, state):
#           if succ not in visited and succ not in to_visit:
#               to_visit.append(succ)
#
#   return visited

# def accessible(dfa, state):
#   if state not in dfa.states:
#       print("error : state '" + state + "' ne fait pas partie de l'automate.")
#       return False
#
#   return state in list_accessible(dfa)

# def accessible(dfa):
#   return len(dfa.states) == len(list_accessible(dfa))


# def list_co-accessible(dfa):
#
#
#
#
#
#
#


# def save_json():

# trouver library img
