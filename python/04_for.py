lista = []

for n in range(0,10):
	lista.append(n)

print lista

lista = [n for n in range(0,10)]

print lista
print("cuadrados")
cuadrados = [n * n for n in range(0, 10) ]
print cuadrados
cuadrados = [n * i for n in range(0, 10) 
			for i in range(0, 10)]
print cuadrados




array2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



array2D = []

for i in range(0, 3):
	array2D.append([])
	for j in range(0, 3):
		array2D[i].append(j + (i*3) + 1)

print("lista creada")
for lista in array2D:
	print lista

array2D = [
	[j + (i*3) + 1 for j in range(0,3)] 
	for i in range(0,3)]

print array2D

orignal = [range(0, 9)]

print orignal

copia = list(orignal)

orignal[0] = "hola"
print orignal
print copia

