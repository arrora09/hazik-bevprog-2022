def szovBe():
    with open("hazi.txt","r",encoding= "UTF-8") as f:
        list=[]
        sor= f.readline()
        while sor:
            list.append(sor)
            sor=f.readline()

        for i in range(0,len(list)-1):
            list[i]=list[i][0:len(list[i])-1]


        import string
        szurtlist=[]

        for x in list:
            szurtlist.append("")

        for i in range(0,len(list)):
            for x in list[i]:
                if x not in string.punctuation:
                    szurtlist[i]=szurtlist[i]+x

        nemures=[]
        for x in szurtlist:
            if not x.__eq__(""):
                nemures.append(x)

        mgh=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
        nagymgh=["A","Á","E","É","I","Í","O","Ó","Ö","Ő","U","Ú","Ü","Ű"]

        csakmsh=[]
        for x in nemures:
            csakmsh.append("")

        for i in range(0, len(nemures)):
            for x in nemures[i]:
                if x not in mgh and x not in nagymgh:
                    csakmsh[i]=csakmsh[i]+x


        helytelen=[]
        for x in nemures:
            helytelen.append("")

        for i in range(0,len(csakmsh)-1):
            for x in csakmsh[i]:
                if not x.__eq__(" "):
                    helytelen[i]=helytelen[i]+x
        


    with open("ki.txt","w",encoding="utf-8") as f:

        for i in range(1,len(helytelen)):
            if i % 3==0:
                f.write(helytelen[i-1]+"\n")




if __name__=="__main__":
    szovBe()

