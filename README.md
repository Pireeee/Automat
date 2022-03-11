Automat
voici le format du JSON
    "Etats":liste de str ,
    "Alphabet":liste de str,
    "Transitions":dictionaire avec comme format <"etat_départ,etat_arrivé":"mot">,
    "Etat initial":str,
    "Etats finaux":liste de str ,
    "Layout":str ("spring" par défaut)

lors de l'affichage vous pouvez changer les layouts (dispostion des nodes) les disponibles sont :
-random
-spectral
-shell
-spring(defaut)