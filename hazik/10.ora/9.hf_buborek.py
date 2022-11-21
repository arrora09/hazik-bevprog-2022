
if __name__=="__main__":
    lista=[54,76,23,45,21,5,67,22,12,64,26,59,82,99]
    print(lista)
    n=len(lista)
    for i in range(0,n):
        for j in range(1,n-i):
            if lista[j-1]>lista[j]:
                lista[j],lista[j-1]=lista[j-1],lista[j]
                print(lista)

    print(lista)