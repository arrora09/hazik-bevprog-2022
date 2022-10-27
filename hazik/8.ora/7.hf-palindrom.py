
def pcheck(mondat):
    emondat=""

    for x in mondat:
        emondat=emondat+x

    ujm=""
    for x in mondat:
        ujm=x+ujm
    emondat=emondat.lower()
    listm = emondat.split(" ")
    emondat=""
    for x in listm:
        emondat=emondat+x
    jtm=""

    import string
    for c in emondat:
        if c not in string.punctuation and c!="," and c!="." and c!="’":
            #print(c)
            jtm = jtm + c

    #print(jtm)
    emondat=jtm


    csakchecke = []
    csakcheckf=[]
    karakter=""
    mod=0
    counter=0
    dzs=False
    if emondat.__contains__("gy") or emondat.__contains__("ny") or emondat.__contains__("sz") or emondat.__contains__("dz") or emondat.__contains__("dzs") or emondat.__contains__("zs") or emondat.__contains__("ty") or emondat.__contains__("ly") or emondat.__contains__("cs"):
        #for i in range(1,len(mondat)):
        l = []
        for x in emondat:
            l.append(x)
        l.append("")
        l.append("")
        while(True):

            #print(l)
            karakter=l[counter]
            #print(counter," " + karakter)
            kerdes=l[counter]+l[counter+1]
            #print("nezi:"+ kerdes)
            #print("lista hossza: ", len(l))



            if kerdes.__eq__("ny"):
                #print("check:"+mondat[i-1]+mondat[i])
                csakcheckf.insert(0,l[counter+1])
                csakcheckf.insert(0,l[counter])
                csakchecke.append(l[counter])
                csakchecke.append(l[counter+1])
                del l[counter+1]
                #l.insert(counter," ")
                #counter = counter + 1

            elif kerdes.__eq__("dz"):
                kerdes=kerdes+l[counter+2]
                #print(kerdes)
                if kerdes.__eq__("dzs"):
                    csakcheckf.insert(0,l[counter+2])
                    csakcheckf.insert(0,l[counter+1])
                    csakcheckf.insert(0,l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter+1])
                    csakchecke.append(l[counter+2])


                    del l[counter+2]

                    counter=counter+1

                else:
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    del l[counter + 1]





            elif emondat[0:2].__eq__("sz") and emondat[-2:].__eq__("zs") or emondat[0:2].__eq__("zs") and emondat[-2:].__eq__("sz"):
                #print(emondat[0:1]+" "+emondat[-3:-1])
                pass

            elif kerdes.__eq__("sz"):
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    del l[counter + 1]
            elif kerdes.__eq__("ss"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("ssz"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1




            elif kerdes.__eq__("ty"):
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    del l[counter + 1]
            elif kerdes.__eq__("tt"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("tty"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1


            elif kerdes.__eq__("ny"):
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    del l[counter + 1]
            elif kerdes.__eq__("nn"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("nny"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1




            elif kerdes.__eq__("dd"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("ddz"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1





            elif kerdes.__eq__("gy"):
                csakcheckf.insert(0, l[counter + 1])
                csakcheckf.insert(0, l[counter])
                csakchecke.append(l[counter])
                csakchecke.append(l[counter + 1])
                del l[counter + 1]
            elif kerdes.__eq__("gg"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("ggy"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1





            elif kerdes.__eq__("ly"):
                csakcheckf.insert(0, l[counter + 1])
                csakcheckf.insert(0, l[counter])
                csakchecke.append(l[counter])
                csakchecke.append(l[counter + 1])
                del l[counter + 1]
            elif kerdes.__eq__("ll"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("lly"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1








            elif kerdes.__eq__("cs"):
                csakcheckf.insert(0, l[counter + 1])
                csakcheckf.insert(0, l[counter])
                csakchecke.append(l[counter])
                csakchecke.append(l[counter + 1])
                del l[counter + 1]
            elif kerdes.__eq__("cc"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("ccs"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1





            elif kerdes.__eq__("zs"):
                csakcheckf.insert(0, l[counter + 1])
                csakcheckf.insert(0, l[counter])
                csakchecke.append(l[counter])
                csakchecke.append(l[counter + 1])
                del l[counter + 1]
            elif kerdes.__eq__("zz"):
                kerdes = kerdes+l[counter+1]
                #print(kerdes)
                if kerdes.__eq__("zzs"):
                    csakcheckf.insert(0, l[counter + 2])
                    csakcheckf.insert(0, l[counter + 1])
                    csakcheckf.insert(0, l[counter])
                    csakchecke.append(l[counter])
                    csakchecke.append(l[counter + 1])
                    csakchecke.append(l[counter + 2])

                    del l[counter + 2]

                    counter = counter + 1

            #elif kerdes=="  ":
             #   csakcheckf.insert(0, karakter)
              #  csakchecke.append(karakter)
                #print(karakter)
                #counter = counter + 1
            else:
                csakcheckf.insert(0, karakter)
                csakchecke.append(karakter)
                #counter=counter+1





            if l[counter+1]=="" or counter+1>len(l):
               break
            #print(csakcheckf)
            #print(csakchecke)
            #print("lista counterje: ", l[counter])
            #print("lista új hossza: ",len(l))
            counter = counter + 1
            #print("új counter:", counter)


    else:
        for x in emondat:
            csakcheckf.insert(0,x)
            csakchecke.append(x)

    if csakchecke.__contains__("á") or csakchecke.__contains__("é") or csakchecke.__contains__("í") or csakchecke.__contains__("ó") or csakchecke.__contains__("ő") or csakchecke.__contains__("ú") or csakchecke.__contains__("ű"):
        for i in range(0,len(csakchecke)):
            if csakchecke[i].__eq__("á"):
                csakchecke[i]="a"
            elif csakchecke[i].__eq__("é"):
                csakchecke[i]="e"
            elif csakchecke[i].__eq__("í"):
                csakchecke[i]="i"
            elif csakchecke[i].__eq__("ó"):
                csakchecke[i]="o"
            elif csakchecke[i].__eq__("ő"):
                csakchecke[i]="ö"
            elif csakchecke[i].__eq__("ű"):
                csakchecke[i]="ü"
            elif csakchecke[i].__eq__("ú"):
                csakchecke[i] = "u"
    if csakcheckf.__contains__("á") or csakcheckf.__contains__("é") or csakcheckf.__contains__("í") or csakcheckf.__contains__("ó") or csakcheckf.__contains__("ő") or csakcheckf.__contains__("ú") or csakcheckf.__contains__("ű"):
        for i in range(0,len(csakcheckf)):
            if csakcheckf[i].__eq__("á"):
                csakcheckf[i]="a"
            elif csakcheckf[i].__eq__("é"):
                csakcheckf[i]="e"
            elif csakcheckf[i].__eq__("í"):
                csakcheckf[i]="i"
            elif csakcheckf[i].__eq__("ó"):
                csakcheckf[i]="o"
            elif csakcheckf[i].__eq__("ő"):
                csakcheckf[i]="ö"
            elif csakcheckf[i].__eq__("ű"):
                csakcheckf[i]="ü"
            elif csakcheckf[i].__eq__("ú"):
                csakcheckf[i] = "u"



    listu=""

    mindentelen1=""
    mindentelen2=""

    for x in csakchecke:
        mindentelen1=mindentelen1+x

    for x in csakcheckf:
        mindentelen2=mindentelen2+x

    print()
    #print(mindentelen1)
    #print(mindentelen2)
    print()

    if mindentelen1.__eq__(mindentelen2):
        print("A mondat palindróm! ")
        print("Az eredeti mondat: "+mondat)
        print("A mondat megfordítva: "+ujm)
    else:
        print("A mondat nem palindróm!")



if __name__=="__main__":
    mondat = str(input("Írjon be egy mondatot! "))
    pcheck(mondat)