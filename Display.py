import networkx as nx
import matplotlib.pyplot as plt
from JSON import JSON
import json
#cette partie nécéssite de

class Display(): #il me reste: gérer état initial et final, les noms sur les fleches

    def __init__(self):
        self.list_tuple_nodes=[]
        self.edge_labels=dict()
        self.tuple_edge=()
        self.initial=''
        self.finaux=[]
        self.transitions=dict()
        self.layout=''



    def generate_tuples_node(self): #créé une liste de 2-tuples à partir du JSON et un dictionnaire avec comme clefs les 2-tuples
        self.mon_json = JSON('','')
        self.mon_json=  self.mon_json.lire_json()
        self.layout= 'nx.'+self.mon_json["Layout"]+'_layout(G)'
        self.initial= self.mon_json["Etat initial"]
        self.finaux = self.mon_json["Etats finaux"]
        self.transitions=self.mon_json["Transitions"][0]
        for keys in self.transitions.keys(): #boucle qui sépare les clefs du dictionaire transition dans une liste
            liste = keys.split(',')

            for i in range(len(liste)): #on parcours la nouvelle liste pour vérifier si les états son initiaux
                if (liste[i]== self.initial):
                    liste[i]= "*" + liste[i]

                for j in range(len(self.finaux)): #on parcour toute la liste des etats finaux 
                    if(liste[i] == self.finaux[j]):
                        liste[i] = self.finaux[j] + "->"

            tuple_node = tuple(liste) #crée un tuple a partir de la liste 
            self.edge_labels[tuple_node]=self.transitions[keys] 
            self.list_tuple_nodes.append(tuple_node)
        print(self.layout)

    
    def draw_graph(self): #génere le graphique 
        G = nx.DiGraph()
        G.add_edges_from(self.list_tuple_nodes) #nome les nodes et leurs affiliations
        if (self.layout == 'shell'):#le layout dans lequel va se former le graph il y à le choix entre random,shell,spectral et par défault c'est spring
            pos=nx.shell_layout(G)
        elif (self.layout == 'random'):
             pos=nx.random_layout(G)
        elif (self.layout == 'spectral'):
             pos=nx.spectral_layout(G)
        else:
            pos=nx.shell_layout(G)

        nodes = nx.draw_networkx_nodes(G, pos, node_size=1000,node_color="#FFFFFF")#place les nodes (cercles) et donne la taille
        nodes.set_edgecolor('black')
        print(nodes)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(),connectionstyle="arc3,rad=0.17",arrows=True,arrowsize=10,width=1.5,node_size=1000) #place les fleches (defini couleur et le radius des arc)
        nx.draw_networkx_labels(G, pos) #place les noms dans les nodes
        nx.draw_networkx_edge_labels( #crée les noms nur les fleches
            G,pos,
            edge_labels=self.edge_labels, #dictionaire
            label_pos=0.7#espacement
        )
        plt.axis('off')
        plt.show()
