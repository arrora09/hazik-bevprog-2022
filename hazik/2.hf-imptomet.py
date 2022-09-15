print("Adjon meg egy számot és egy mértékegységet (cm/inch):")

hossz=float(input())

#rMertekE=True
#while rMertekE:

while True:
    mertekE=str(input())

    if "cm" in mertekE or "inch" in mertekE:
        #rMertekE=False
        break

    else:
        print("Not correct unit!")



if "inch" in mertekE:
    eredmeny=hossz*2.54
    print("{} centimeters".format(eredmeny))
if "cm" in mertekE:

    eredmeny=hossz/2.54
    print("{} inches".format(eredmeny))

####      eltér az "elvárt kimenettől", mert 1 inch = 2,54 cm tudtommal... de ha rosszul tudom, itt az alternatíva
#if "cm" in mertekE:
#    eredmeny=hossz*2.54
#    print("{} inches".format(eredmeny))
#if "inch" in mertekE:
#    eredmeny=hossz/2.54
#    print("{} centiemters".format(eredmeny))