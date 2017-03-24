print ("-----programa 6- suma de intervalo de los primero n numeros al cubo--")
print ("----------------------------------------------------------------------")

final=input("ingrese el final del intervalo")
suma =0.0
final2=int(final)
lista=[]
print (final2)
for i in range(1,final2+1):
    suma=suma+(i**3)
    lista.append(i**3)
print ("lista de numeros a la potencia 3: ", lista)
print ("la suma de los elemento de la lista es: ", suma)

    
    
