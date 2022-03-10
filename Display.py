from msilib.schema import Class
import networkx as nx
import matplotlib.pyplot as plt
from JSON import JSON
import json


class Display(): #il me reste: gérer état initial et final, les noms sur les fleches

    def __init__(self):
        self.list_tuple_nodes=[]
        self.edge_labels={}
        self.tuple_edge=()
        self.initial=''
        self.finaux=[]
        self.transitions=dict()



    def generate_tuples_node(self): #créé une liste de 2-tuples à partir du JSON
        self.mon_json = JSON('','')
        self.mon_json=  self.mon_json.lire_json()
        self.initial= self.mon_json["Etat initial"]
        self.finaux = self.mon_json["Etats finaux"]
        self.transitions=self.mon_json["Transitions"][0]
        for keys in self.transitions.keys(): #boucle qui sépare les clefs du dictionaire transition dans une liste
            liste = keys.split(',')

            for i in range(len(liste)): #on parcour la nouvelle liste pour vérifier si les etats son initiaux
                if (liste[i]== self.initial):
                    liste[i]= "*" + liste[i]

                for j in range(len(self.finaux)): #on parcour toute la liste des etats finaux 
                    if(liste[i] == self.finaux[j]):
                        liste[i] = self.finaux[j] + "->"

            tuple_node = tuple(liste) #crée un tuple a partir de la liste
            self.list_tuple_nodes.append(tuple_node) # crée une liste de 2-tuple 
        #self.edge_labels ={
        #    ('*q','B'):'a',
        #    ('A*','C'):'b',
        #    ('C','A*'):'c'
        #}

    #def generate_edge_labels(self): #doit créer un dictionaire avec comme clefs des 2-tuples

        

    def draw_graph(self): #génere le graphique 
        G = nx.DiGraph()
        G.add_edges_from(self.list_tuple_nodes) #nome les nodes et leurs affiliations
        pos = nx.spring_layout(G)   #le layout dans lequel va se former le graph https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html
        nx.draw_networkx_nodes(G, pos, node_size=1000)#place les nodes (cercles) et donne la taille
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='hotpink',connectionstyle="arc3,rad=0.15",arrows=True,arrowsize=10,width=2,node_size=1000) #place les fleches (defini couleur et le radius des arc)
        nx.draw_networkx_labels(G, pos)
        #dessine les noms des nodes
        #nx.draw_networkx_edge_labels( #crée les noms nur les fleches
        #    G,pos,
        #    edge_labels=self.transitions,
        #    font_color='hotpink',#couleur de la fleche
        #    label_pos=0.7#espacement
        #)
        plt.axis('off')
        plt.show()
        #
