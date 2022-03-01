import networkx as nx
import matplotlib.pyplot as plt

def _build_graph(show=True):
    """Load word dependencies into graph using networkx. Enables easy traversal of dependencies for parsing particular patterns.
    One graph is created for each sentence.

    Args:
        show (bool): If set to True, labeled visualization of network will be opened via matplotlib for each sentence

    Returns:
        None: Global variable G is set from within function

    """
    global G
    G = nx.Graph()
    node_labels, edge_labels = {}, {}
    for idx, dep in enumerate(A.deps):

        types = ["dependent", "governor"]

        # nodes, labels
        for x in types:
            G.add_node(str(dep[x]), word=dep[x + "Gloss"], pos=A.lookup[dep[x]]["pos"])
            node_labels[str(dep[x])] = dep[x + "Gloss"] + " : " + A.lookup[dep[x]]["pos"]

        # edges, labels
        G.add_edge(str(dep[types[0]]), str(dep[types[1]]), dep=dep["dep"])
        edge_labels[(str(dep[types[0]]), str(dep[types[1]]))] = dep["dep"]

    if show == True:
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos=pos, labels=node_labels, node_color="white", alpha=.5)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
        plt.show()


#########################################
# Dependency / POS parsing functions
######################################### 