class Team:
    def __init__(self, nev, projekt, feladatkor):
        self.nev=nev
        self.projekt=projekt
        self.feladatkor=feladatkor

        print("-- Developer létrehozva --")
        print(self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben.")

    def __str__(self):
       return self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben."

    def __eq__(self, other):
        return self.nev==other.nev and self.projekt==other.projekt and self.feladatkor==other.feladatkor

def check():
    devek=[Team("Ricsi","SolArch","Frontend"),Team("Angéla","ZerTeng","Tesztelő"),Team("Peti","KefERP","Backend"),Team("Éva","KefERP","Frontend")]

    print()
    gyujtd=[]
    for x in range(0,len(devek)):
        for y in range(0, len(devek)):
            if y==x:
                pass
#projekt egyezés
            elif devek[x].projekt==devek[y].projekt and y>x:
                #gyujtd.append(devek[x])
                #gyujtd.append(devek[y])
                print(devek[x].nev+" és "+devek[y].nev+" dolgoznak egy projekten.")


#duplikáció kiszűrés
    #szurve=[]
    #[szurve.append(x) for x in gyujtd if x not in szurve]

#kollegák
    #megvoltak=[]
    #for x in range(0,len(szurve)):
    #    for y in range(0,len(szurve)):
    #        if x!=y and (szurve[y] not in megvoltak) and szurve[x].projekt==szurve[y].projekt:
    #            megvoltak.append(szurve[x])
    #            print(szurve[x].nev + " és " + szurve[y].nev + " dolgoznak egy projekten")

if __name__=="__main__":
    check()