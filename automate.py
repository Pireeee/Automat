from operator import ne
from JSON import JSON

class Automate():
    def __init__(self,filename):
        self.JSON = JSON("","",filename).lire_json()

    
    def determiniser(self): #fonction a appeller pour lancer agregation et completion       
        if len(self.JSON['Etat initial']) != 1:
            self.agreg(self.JSON['Etat initial'])
        listetatalp = self.listalph()
        alph = self.JSON["Alphabet"]
        i = 0
        for y in listetatalp:
            for x in alph:
                if x not in y:
                    
                    name = str(y[0]) + ",trash" +" oper"+ str(i)
                    self.JSON["Transitions"][0][name] = x
                    i += 1


    def agreg(self,listetat):
        nam = "("
        for x in listetat:
            nam += x+","
        nam =()
        dico = self.dictalpha(listetat)
        fdico = {}
        for y in self.JSON["Alphabet"]:
            temp = {}
            for x in listetat:
                if y in dico[x]:
                    temp[x] = dico[x][y]
            fdico[y] = temp
        for x in self.JSON["Alphabet"]:
            for y in fdico[x]:
                for z in fdico[x]:
                    if fdico[x][z] != fdico[x][y] and y != z:
                        print(fdico[x][z],fdico[x][y])
                        new_key = "("+z+","+y+")"
                        old = y+","+z
                        try:
                            self.JSON["Transitions"][0][new_key] = self.JSON["Transitions"][0].pop(old)
                        except KeyError:
                            pass
                        l = [fdico[x][z],fdico[x][y]]
                        self.agreg(l)

    def dictalpha(self,listeetat):
        transition = self.JSON["Transitions"][0]
        sor = {}
        for y in listeetat:
            temp = {}
            for x in transition:
                if x[:2] == y:
                    temp[transition[x]] = x[3:]
            sor[y] = temp
        return sor

    def listalph(self):
        transition = self.JSON["Transitions"][0]
        listeetat = self.JSON["Etats"]
        sor = []
        for y in listeetat:
            temp = [y]
            for x in transition:
                if x[:2] == y:
                    temp.append(transition[x])
            sor.append(temp)
        return sor

