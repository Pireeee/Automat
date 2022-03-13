Automat
voici le format du JSON
    "Etats":liste de str ,
    "Alphabet":liste de str,
    "Transitions":dictionaire avec comme format <"etat_départ,etat_arrivé":"mot">,
    "Etat initial":str,
    "Etats finaux":liste de str ,
    "Layout":str ("spring" par défaut)

le fichier json de save s'appelle toujours nouvel_automate.json

Pierre sur le display de l'automate
Martin sur l'automate en lui-meme
Nicolas sur l'accessibilité et la co-accessibilité (mis en commentaire)
Raphael sur la lecture et la generation du json ainsi que la liaison des fichier

lors de l'affichage vous pouvez changer les layouts (dispostion des nodes) les disponibles sont :
-random
-spectral
-shell
-spring(defaut)