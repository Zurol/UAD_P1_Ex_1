import os

def imprimeFibonacci():

    tope = int(input("\n\nIntroduce el número máximo para la secuencia."))

    print("\n\n Ahora introduce el rango que no va a mostrarse")
    min = int(input("Introduce el número min:"))
    max = int(input("Introduce el número max:"))



    numeroFib = 0
    numeroViejo = 0
    suma = 0

    while (numeroFib <= tope):
        #print ("numeroFib{0} - {1}".format(numeroFib, numeroViejo))

        if ( not (numeroFib > min and numeroFib < max ) ):
            print ("{0}".format(numeroFib, numeroViejo))

        if numeroFib == 0:
            numeroViejo = numeroFib
            numeroFib = 1

        else :

            #numeroFib += numeroViejo
            suma = numeroViejo + numeroFib
            numeroViejo = numeroFib
            numeroFib = suma





response = ""

while(response!="NO"):
    response = input("¿Deseas continuar con el programa? ([NO] para salir)")

    imprimeFibonacci()

    #os.system('cls')
