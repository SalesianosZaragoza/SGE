lista = []

for n in range(0,10):
	lista.append(n)

print lista

lista = [n for n in range(0,10)]

print lista

cuadrados = [n * i for n in range(0, 10) 
			for i in range(0, 10)]





array2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



array2D = []

for i in range(0, 3):
	array2D.append([])
	for j in range(0, 3):
		array2D[i].append(j + (i*3) + 1)


for lista in array2D:
	print lista

array2D = [
	[j + (i*3) + 1 for j in range(0,3)] 
	for i in range(0,3)]

print array2D

array = [range(0, 9)]

print array

otro_nombre = list(array)

array[0] = "hola"

print otro_nombre

