print ("-----rotar lista-----")
print (".....................")
#[1,2,3,4]
#2 3 4 1
#3 4 1 2
#4 1 2 3
#.append agrga
#.pop() elimina el ul y guarda
#
lis=eval(input("ingrese una lista como por ejemplo: [3,4,2...N]" ))
#lis=[1,2,3,4]
#lista=input("ingrese la lista ejmplo: [2,3,4...N]")
#lis=[int(i) for i in lis]
#lista2=[]
print (lis)
tam=len(lis)
print (tam)
for j in range(1,tam):
	for i in range(1,tam):
		print (tam)
		val=lis[i-1]
		#val2=lis[1:tam]  
		lis [i-1] = lis [i]
		lis [i] = val
	print (lis)