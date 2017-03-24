print ('suma cuadrado de n numeros usando recursividad')
lis=eval(input("ingrese una lista como por ejemplo [2,3,4,5]"))

def suma(lista):
    if lista == []:
        return "error"
    elif len(lista) == 1:
        return lista
    else:
        return suma_aux(lista,0)

def suma_aux(lista,resultado):
    if lista == []:
        return resultado
    else:

        resultado = resultado + (lista[0]**2)
        print (resultado)
        #print (lista)
        return suma_aux(lista[1:],resultado)


suma(lis)

