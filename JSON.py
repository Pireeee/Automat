#from dbm import gnu
import json

class JSON(): #dans la vi il faut commenter surtout si on est en groupes
    def __init__(self,action,resultat, file):
        self.action = action
        self.resultat = resultat
        self.input_dict = ""
        self.auto_file = file

    def lire_json(self): #retoune le JSON
        with open(self.auto_file, 'r') as input:
            self.input_dict = json.load(input)
        return self.input_dict

    #def get_input_dict(self):
    #    return self.input_dict


    def generer_json(self):
        contenu = json.dumps({
            "action": self.action,
            "resultat": self.resultat,
            
            "etats initial":"1",
            "etats finaux":"2:3"
        }, sort_keys=True, indent=4)

        fichier = open("automate_input.json","w")
        fichier.write(contenu)
        fichier.close()

    

#def afficher_automate():

#def successors(dfa, state):
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

#def list_accessible(dfa):
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

#def accessible(dfa, state):
#   if state not in dfa.states:
#       print("error : state '" + state + "' ne fait pas partie de l'automate.")
#       return False
#
#   return state in list_accessible(dfa)

#def accessible(dfa):
#   return len(dfa.states) == len(list_accessible(dfa))
    

#def list_co-accessible(dfa):
#   
#
#
#
#
#
#



#def save_json():

#trouver library img