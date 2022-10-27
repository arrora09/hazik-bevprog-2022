def table():
    tabla="{0:>4}{1:>1}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}{13:>5}"

    print(tabla.format(""," ","1","2","3","4","5","6","7","8","9","10","11","12"))
    print("    :--------------------------------------------------------------")
    list=[]
    for i in range(0,12):
        for j in range(1,13):
            list.append(j*(i+1))

        print(tabla.format(str(i+1),":",list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11]))
        list=[]



if __name__=="__main__":
    table()


