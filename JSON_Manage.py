from gettext import translation
from JSON import JSON
import json


def Prepar():  # faut commenter son code
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

    bie = JSON(etats, alphabet, transi_finale,
               etat_initial, etats_finaux)
    bie.generer_json()


def test():    # c koi 7 fonq°
    lire = JSON("", "")
    input_dict = lire.lire_json()
    for clef in input_dict:
        print(clef, input_dict[clef])

# resultat:

#action ;ss;gg;gl
# etats finaux 2:3
# etats initial 1

# test()


Prepar()
