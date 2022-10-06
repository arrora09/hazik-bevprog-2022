class Team:
    def __init__(self, nev, projekt, feladatkor):
        self.nev=nev
        self.projekt=projekt
        self.feladatkor=feladatkor

        print("-- Developer létrehozva --")
        print(self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben.")

    def __str__(self):
       return self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben."

devek=[Team("Ricsi","SolArch","Frontend"),Team("Angéla","ZerTeng","Tesztelő"),Team("Peti","KefERP","Backend"),Team("Éva","KefERP","Frontend")]

print()

for x in range(0,len(devek)):
    for y in range(0, len(devek)-1):
        if devek[x].projekt==devek[y].projekt:
            if devek[x].nev==devek[y].nev and devek[x].feladatkor==devek[y].feladatkor:
                pass
            else:
                print(devek[x].nev+" és "+devek[y].nev+" dolgoznak egy projekten")