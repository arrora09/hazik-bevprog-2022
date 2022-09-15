print("Adjon meg egy mondatot:")
mondat=str(input())


###########################
# gyakorisag

dict={}

betuk=[x for x in mondat]

charlist=[]
for x in betuk:
    if x in charlist:
        pass
    else:
        charlist.append(x)

for x in charlist:
    szam=0
    for y in mondat:
        if x is y:
            szam=szam+1
    dict.setdefault(x,szam)

print("Betűk gyakorisága: {}".format(dict))


###############################
# forditas

fmondat=""

for x in betuk:
    fmondat=x+fmondat

print("Fordítva: "+fmondat)


###############################
# lista

lista=mondat.split(" ")

print("Listába rendezve szavanként: {}".format(lista))