print ("MAXIMO DE 3 NUMEROS")
print ("--------------------")

x=input("Escriba el dato 1: ")
y=input("Escriba el dato 2: ")
z=input("Escriba el dato 3: ")

print ("numeros:", x, y, z)

mayor=0

if x > y:
    mayor=x
elif y>x:
    mayor=y
if mayor>z:
    mayor=mayor
elif z>mayor:
        mayor=z
    



print ("el mayor de los 3 numeros es:", mayor)
                
                
