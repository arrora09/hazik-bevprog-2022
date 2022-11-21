if __name__=="__main__":
    lista=[2,5,6,8,13,32,42,50,53,62,66,70,80,89,91]
    start=0
    stop=len(lista)-1
    print(f"start: {start}\nstop: {stop}")
    keresett=89
    print()
    counter=1

    if keresett in lista:
        while start < stop:
            print(f"{counter}. próba")
            k = int((start + stop) / 2)

            if keresett < lista[k]:
                stop = k - 1
                print(f"start: {start}\nstop: {stop}")

            elif keresett > lista[k]:
                start = k + 1
                print(f"start: {start}\nstop: {stop}")

            else:

                break
            print()
            counter=counter+1

        print("Megvan!")
        print(f"start: {start}\nstop: {stop}")
    else:
        print("hiba")


