from JSON import JSON
from Display import Display
from automate import Automate


def Generer_Json():
    alphabet = []
    etats_finaux = []
    transitions = {}
    etats = []

    # INPUT ETATS
    etat_possible = input(
        "Etat possible (1 par 1 s'il vous plait)(to quit: input quit)")
    while etat_possible != "quit":
        if etat_possible[:1] != 'q':
            etat_possible = 'q' + etat_possible
        etats .append(etat_possible)
        etat_possible = input(
            "Etat possible(to quit: input quit)")

    # INPUT TRANSITIONS A FINIR
    etat_premier = input(
        "Entrez etat avant transition(1 par 1 s'il vous plait)(to quit: input quit)")
    action = input(
        "entrée action (1 par 1 s'il vous plait)(to quit: input quit)")
    resultat = input(
        "entree resultat (1 par 1 s'il vous plait)(to quit: input quit)")
    while etat_premier != "quit" or action != "quit" or resultat != 'quit':
        if etat_premier[:1] != 'q':
            etat_premier = 'q' + etat_premier
        if resultat[:1] != 'q':
            resultat = 'q' + resultat
        les_etats = etat_premier + ',' + resultat
        transitions[les_etats] = action

        etat_premier = input(
            "Entrez etat avant transition(to quit: input quit)")
        action = input("entrée action (to quit: input quit)")
        resultat = input("entree resultat (to quit: input quit)")

    # INPUT ALPHABET
    lettre = input("Alphabet (1 par 1 s'il vous plait)(to quit: input quit)")
    while lettre != "quit":
        alphabet.append(lettre)
        lettre = input("Alphabet (to quit: input quit)")

    # INPUT ETAT INITIAL
    etat_initial = input("Etat intial")
    if etat_initial[:1] != 'q':
        etat_initial = 'q' + etat_initial

    # INPUT ETATS FINAUX
    etat_final = input(
        "Etat final (1 par 1 s'il vous plait)(to quit: input quit)")
    while etat_final != "quit":
        if etat_final[:1] != 'q':
            etat_final = 'q' + etat_final
        etats_finaux.append(etat_final)
        etat_final = input(
            "Etat final (to quit: input quit)")

    transi_finale = [transitions]

    temp = JSON(etats, alphabet, transi_finale,
                etat_initial, etats_finaux, "nouvel_automate.json")
    temp.generer_json()


def Afficher():  # appele la class Display pour pouvoir la tester
    var = Display("nouvel_automate.json")
    var.generate_tuples_node()
    var.draw_graph()


# Generer_Json()
Afficher()

"""def successors(dfa, state):
   if state not in dfa.states:
       print("error : l'etat specifié '" + state + "' ne fait pas partie de l'automate.")
       return

   ret = []
   for (symbol, dst_state) in dfa.transitions[state]:
       if dst_state not in ret:
           ret.append(dst_state)

   return ret
def list_accessible(dfa):
   visited = []
   to_visit = [dfa.init]

   while len(to_visit) > 0:
       state = to_visit.pop()
       visited.append(state)
       for succ in successors(dfa, state):
           if succ not in visited and succ not in to_visit:
               to_visit.append(succ)

   return visited
def accessible(dfa, state):
   if state not in dfa.states:
       print("error : etat '" + state + "' ne fait pas partie de l'automate.")
       return False

   return state in list_accessible(dfa)
def accessible(dfa):
   return len(dfa.states) == len(list_accessible(dfa))



def predecessors(dfa, state):
    if state not in dfa.states:
        print("error : l'etat specifié '" + state + "' ne fait pas partie de l'automate.")
        return
 
    ret = []
    for src_state in dfa.states:
        for (symbol, dst_state) in dfa.transitions[src_state]:
            if dst_state == state and src_state not in ret:
                ret.append(src_state)
 
    return ret
    
def list_coaccessible(dfa):
    visited = []
    to_visit = dfa.finals.copy()

    while len(to_visit) > 0:
        state = to_visit.pop()
        visited.append(state)
        for pred in predecessors(dfa, state):
            if pred not in visited and pred not in to_visit:
                to_visit.append(pred)

    return visited

def coaccessible(dfa, state):
    if state not in dfa.states:
        print("error : etat '" + state + "' ne fait pas partie de l'automate.")
        return

    return state in list_coaccessible(dfa)

def coaccessible(dfa):
    return len(dfa.states) == len(list_coaccessible(dfa))"""


automate_test = Automate("nouvel_automate.json")
automate_test.determiniser()
