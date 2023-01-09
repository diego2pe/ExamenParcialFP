# crear un algoritmo para hallar el factorial de un numero ingresado por el usuario
while True:
    num=int(input("por favor ingrese el numero del que vamos a hallar su factorial\n"))
    acum=1
    for i in range(1,num+1):
        acum*=i 
        i+=1
    print("el resultado de la operacion es:",acum)

