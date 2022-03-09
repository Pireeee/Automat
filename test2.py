import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
# Create node characteristics DF

carac = pd.DataFrame({'ID':['Jules\nFisher', 'Peggy\nEisenhauer', 'Jennifer\nTipton', 
                            'Thomas\nSkelton', 'Donald\nHolder', 'Christopher\nAkerlind', 
                            'Howell\nBinkley', 'Jean\nRosenthal', 'Stanley\nMcCandless', 
                            'Brian\nMacDevitt', 'Kenneth\nPosner', 'Natasha\nKatz', 
                            'Jeff\nCroiter', 'Jennifer\nSchriever', 'Roger\nMorgan', 
                            'Paul\nGallo', 'Ming Cho\nLee', 'Ken\nBillington', 
                            'Tharon\nMusser', 'Mike\nBaldassari', 'Brian\nMonahan', 
                            'Peter\nNigrini', 'Richard\nPilbrow', 'Beverly\nEmmons', 
                            'Robert\nOrnbo', 'William\nRitman', 'Yale\nSchool\nof Drama', 
                            'Stephen\nStrawbridge', 'Pat\nCollins', 'David\nLander', 
                            'NYU\nTisch', 'Allen Lee\nHughes', 'Bradley\nKing', 
                            'Dennis\nParichy', 'SUNY\nPurchase', 'Robert\nWierzel', 
                            'Mary Louise\nGeiger', 'Jane\nCox', 'Jo\nMielziner', 
                            'Bill\nMintzer', 'Clifton\nTaylor', 'John\nGleason', 
                            'Rita Kogler\nCarver', 'Peggy\nClark', 'Gilbert\nHemsley Jr', 
                            'Peter\nHunt', 'Williamstown\nTheatre\nFestival', 
                            'James\nIngalls', 'Rui\nRita', 'Lee\nWatson', 'Japhy\nWeideman', 
                            'Kevin\nAdams', 'Richard\nNelson', 'Jay\nWoods', 
                            'Ian\nCalderon', 'Stacey\nBoggs', 'Al\nCrawford', 
                            'Robert\nHenderson'], 
                      
                      'type':['Person','Person','Person','Person', 'Person', 
                              'Person', 'Person', 'Person', 'Person', 
                              'Person', 'Person', 'Person', 'Person',
                              'Person', 'Person', 'Person', 'Person', 'Person',
                              'Person', 'Person', 'Person', 'Person', 'Person',
                              'Person', 'Person', 'Person', 'School', 'Person',
                              'Person', 'Person', 'School', 'Person', 'Person',
                              'Person', 'School', 'Person', 'Person', 'Person',
                              'Person', 'Person',
                              'Person', 'Person', 'Person', 'Person',
                              'Person', 'Person', 'Org', 'Person', 
                              'Person', 'Person', 'Person', 'Person', 
                              'Person', 'Person', 'Person', 'Person', 'Person', 
                              'Person']})

# Create graph object using relationships DF
G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.Graph())

# Set colors by type
carac = carac.set_index('ID')
carac = carac.reindex(G.nodes())
 
carac['type'] = pd.Categorical(carac['type'])
carac['type'].cat.codes

# Set node size by type
node_sizes = [4500 if entry != 'Person' else 1500 for entry in carac.type]

# Set color map
cmap = matplotlib.colors.ListedColormap(['darkorange', 'lightgray', 'dodgerblue'])

# Draw the graph and specify our characteristics
nx.draw(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, 
        node_size=node_sizes, font_size=8, font_weight="bold", width=0.75, 
        edgecolors='gray')

plt.show()