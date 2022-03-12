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


automate_test = Automate("nouvel_automate.json")
automate_test.determiniser()

Afficher()
