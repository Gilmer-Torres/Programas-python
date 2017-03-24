print ("--intervalos de n numeros entre 20 y 60--")
print ("-----------------------------------------")
print (" ")

try:
    num=int(input("ingrese el total de numeros a usar en el intervalo"))
    lista=[]
    for i in range(20,(20+num)+1):
        lista.append(i)
    print (lista)
except ValueError:
        print ("###favor de ingresar un numero!!###")
