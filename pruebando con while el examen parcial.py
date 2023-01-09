while True:
    num=int(input("por favor ingrese el numero al que vamos a hallar su factorial\n"))
    acum=1
    i=1
    while i<=num:
        acum*=i 
        i+=1
    print("el resultado de la operacion es:",acum)
