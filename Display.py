from msilib.schema import Class
import networkx as nx
import matplotlib.pyplot as plt
from JSON import JSON
import json


class Display():

    def __init__(self):
        self.list_tuple_nodes=[]
        self.tuple_edge=()
        self.initial=''
        self.final=''
        self.actions=''
        self.transitions=dict()


    def generate_tuples(self): #créé deux liste de tuples à partir du JSON
        self.mon_json = JSON('','')
        self.mon_json=  self.mon_json.lire_json()
        print(self.mon_json)
        liste=[]
        self.transitions=self.mon_json["Transitions"][0]
        for keys in self.transitions.keys():
            liste = keys.split(',')
            tuple_node = tuple(liste)
            self.list_tuple_nodes.append(tuple_node) 
        print(self.list_tuple_nodes)
        #print(self.list_tuple_nodes)


    def draw_graph(self): #génere le graphique 
        G = nx.DiGraph()
        G.add_edges_from(self.list_tuple_nodes) #nome les nodes et leurs affiliations
        pos = nx.spring_layout(G)   #le layout dans lequel va se former le graph https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html
        nx.draw_networkx_nodes(G, pos, node_size=500)#place les nodes (cercles) et donne la taille
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='hotpink',connectionstyle="arc3,rad=0.15") #place les fleches (defini couleur et le radius des arc)
        nx.draw_networkx_labels(G, pos)#dessine les noms des nodes
    #    nx.draw_networkx_edge_labels( #crée les noms nur les fleches
    #        G,pos,
    #        edge_labels={('A*','B'):'a',
    #                    ('A*','C'):'b',
    #                    ('C','A*'):'c'},
    #        font_color='hotpink',#couleur de la fleche
    #        label_pos=0.7#espacement
    #    )
        plt.axis('off')
        plt.show()
