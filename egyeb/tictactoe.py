retry=True

#          szimbolum valasztas

while retry:
    playersym = str(input("choose X or O: "))
    playersym=playersym.upper()
    if "X" in playersym or "O" in playersym:
        retry=False


print()
print("Your symbol is: "+playersym)

if "X" in playersym:
    botsym="O"
else:
    botsym="X"

############################################
#      tabla
table = [" "," "," "," "," "," "," "," "," "]

if "X" in playersym:
    print(" "+table[0]+" | "+table[1]+" | "+table[2])
    print("---|---|---")
    print(" "+table[3]+" | "+table[4]+" | "+table[5])
    print("---|---|---")
    print(" "+table[6]+" | "+table[7]+" | "+table[8])

################################################
#jatek

match=True
wrongP=True
wrongM=True
winner=""

# a jatekos x
if "X" in playersym:
    while match:

#jatekos lepes

        while wrongP:
            move=int(input("type cell number (1-9): "))
            if move > 9 or move < 1:
                print("Wrong number!")
                continue
            if table[move-1] in " ":
                wrongP=False
                table[move-1]=playersym
            else:
                print("Cell is taken!")

#vizszintes check
        if table[0]!=" " and table[1]!=" " and table[2]!=" " and table[0] in table[1] and table[1] in table[2]:
            winner=table[1]
            match=False
            break
        if table[3]!=" " and table[4]!=" " and table[5]!=" " and table[3] in table[4] and table[4] in table[5]:
            winner=table[4]
            match=False
            break
        if table[6]!=" " and table[7]!=" " and table[8]!=" " and table[6] in table[7] and table[7] in table[8]:
            winner=table[7]
            match=False
            break
#fuggoleges check
        if table[0]!=" " and table[3]!=" " and table[6]!=" " and table[0] in table[3] and table[3] in table[6]:
            winner=table[3]
            match=False
            break
        if table[1]!=" " and table[4]!=" " and table[7]!=" " and table[1] in table[4] and table[4] in table[7]:
            winner=table[4]
            match=False
            break
        if table[2]!=" " and table[5]!=" " and table[8]!=" " and table[2] in table[5] and table[5] in table[8]:
            winner=table[5]
            match=False
            break
#atlos check
        if table[0]!=" " and table[4]!=" " and table[8]!=" " and table[0] in table[4] and table[4] in table[8]:
            winner=table[4]
            match=False
            break
        if table[2]!=" " and table[4]!=" " and table[6]!=" " and table[2] in table[4] and table[4] in table[6]:
            winner=table[3]
            match=False
            break




#gep lepes


        import random

        while wrongM:
            botmove=random.randrange(0,8)
            if table[botmove] in " ":
                wrongM=False
                table[botmove]=botsym




        print(" " + table[0] + " | " + table[1] + " | " + table[2])
        print("---|---|---")
        print(" " + table[3] + " | " + table[4] + " | " + table[5])
        print("---|---|---")
        print(" " + table[6] + " | " + table[7] + " | " + table[8])

#vizszintes check
        if table[0]!=" " and table[1]!=" " and table[2]!=" " and table[0] in table[1] and table[1] in table[2]:
            winner=table[1]
            match=False
        if table[3]!=" " and table[4]!=" " and table[5]!=" " and table[3] in table[4] and table[4] in table[5]:
            winner=table[4]
            match=False
        if table[6]!=" " and table[7]!=" " and table[8]!=" " and table[6] in table[7] and table[7] in table[8]:
            winner=table[7]
            match=False
#fuggoleges check
        if table[0]!=" " and table[3]!=" " and table[6]!=" " and table[0] in table[3] and table[3] in table[6]:
            winner=table[3]
            match=False
        if table[1]!=" " and table[4]!=" " and table[7]!=" " and table[1] in table[4] and table[4] in table[7]:
            winner=table[4]
            match=False
        if table[2]!=" " and table[5]!=" " and table[8]!=" " and table[2] in table[5] and table[5] in table[8]:
            winner=table[5]
            match=False
#atlos check
        if table[0]!=" " and table[4]!=" " and table[8]!=" " and table[0] in table[4] and table[4] in table[8]:
            winner=table[4]
            match=False
        if table[2]!=" " and table[4]!=" " and table[6]!=" " and table[2] in table[4] and table[4] in table[6]:
            winner=table[4]
            match=False

        wrongP=True
        wrongM=True


else:
# a gep x
    while match:
        # gep lepes

        import random

        while wrongM:
            botmove = random.randrange(0, 8)
            if table[botmove] in " ":
                wrongM = False
                table[botmove] = botsym

        print(" " + table[0] + " | " + table[1] + " | " + table[2])
        print("---|---|---")
        print(" " + table[3] + " | " + table[4] + " | " + table[5])
        print("---|---|---")
        print(" " + table[6] + " | " + table[7] + " | " + table[8])


        # vizszintes check
        if table[0] != " " and table[1] != " " and table[2] != " " and table[0] in table[1] and table[1] in table[2]:
            winner = table[1]
            match = False
            break
        if table[3] != " " and table[4] != " " and table[5] != " " and table[3] in table[4] and table[4] in table[5]:
            winner = table[4]
            match = False
            break
        if table[6] != " " and table[7] != " " and table[8] != " " and table[6] in table[7] and table[7] in table[8]:
            winner = table[7]
            match = False
            break
        # fuggoleges check
        if table[0] != " " and table[3] != " " and table[6] != " " and table[0] in table[3] and table[3] in table[6]:
            winner = table[3]
            match = False
            break
        if table[1] != " " and table[4] != " " and table[7] != " " and table[1] in table[4] and table[4] in table[7]:
            winner = table[4]
            match = False
            break
        if table[2] != " " and table[5] != " " and table[8] != " " and table[2] in table[5] and table[5] in table[8]:
            winner = table[5]
            match = False
            break
        # atlos check
        if table[0] != " " and table[4] != " " and table[8] != " " and table[0] in table[4] and table[4] in table[8]:
            winner = table[4]
            match = False
            break
        if table[2] != " " and table[4] != " " and table[6] != " " and table[2] in table[4] and table[4] in table[6]:
            winner = table[3]
            match = False
            break



        # jatekos lepes

        while wrongP:
            move = int(input("type cell number (1-9): "))
            if move > 9 or move < 1:
                print("Wrong number!")
                continue
            if table[move - 1] in " ":
                wrongP = False
                table[move - 1] = playersym
            else:
                print("Cell is taken!")

        # vizszintes check
        if table[0] != " " and table[1] != " " and table[2] != " " and table[0] in table[1] and table[1] in table[2]:
            winner = table[1]
            match = False
        if table[3] != " " and table[4] != " " and table[5] != " " and table[3] in table[4] and table[4] in table[5]:
            winner = table[4]
            match = False
        if table[6] != " " and table[7] != " " and table[8] != " " and table[6] in table[7] and table[7] in table[8]:
            winner = table[7]
            match = False
        # fuggoleges check
        if table[0] != " " and table[3] != " " and table[6] != " " and table[0] in table[3] and table[3] in table[6]:
            winner = table[3]
            match = False
        if table[1] != " " and table[4] != " " and table[7] != " " and table[1] in table[4] and table[4] in table[7]:
            winner = table[4]
            match = False
        if table[2] != " " and table[5] != " " and table[8] != " " and table[2] in table[5] and table[5] in table[8]:
            winner = table[5]
            match = False
        # atlos check
        if table[0] != " " and table[4] != " " and table[8] != " " and table[0] in table[4] and table[4] in table[8]:
            winner = table[4]
            match = False
        if table[2] != " " and table[4] != " " and table[6] != " " and table[2] in table[4] and table[4] in table[6]:
            winner = table[4]
            match = False

        wrongP = True
        wrongM = True


print()
print()

print(" " + table[0] + " | " + table[1] + " | " + table[2])
print("---|---|---")
print(" " + table[3] + " | " + table[4] + " | " + table[5])
print("---|---|---")
print(" " + table[6] + " | " + table[7] + " | " + table[8])

print()
print(winner+" won!")