from JSON import JSON
import json


def Prepar():
    Action  = ""
    Resultat = ""
    a = True
    while a:
        action = input("entrée action ")
        if action == "quit":
            break
        resultat = input("entree resultat ")
        Action = Action + ";" + action
        Resultat = Resultat +";"+ resultat
    bie = JSON(Action,Resultat)
    bie.generer_json()




def test():
    lire  = JSON("","")
    input_dict = lire.lire_json()
    for clef in input_dict:
        print(clef,input_dict[clef])
       
#resultat:

#action ;ss;gg;gl
#etats finaux 2:3
#etats initial 1

#test()