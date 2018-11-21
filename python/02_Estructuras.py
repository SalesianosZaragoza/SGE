'''
emptyTuple = ()
emptyTuple = tuple()

print(emptyTuple)
singleItemTuple = ("spam",)  # fijarse en la coma
print(singleItemTuple)

print(singleItemTuple[0])
'''


#print singleItemTuple[1]
'''
mytuple1 = 12, 89, 'a'
mytuple2 = (13, 14, 'a')
mytuple3 = mytuple1 + mytuple2
print(mytuple3)
print(mytuple3 * 5)
'''

# trabajando con listas
a = ['pan', 'huevos', 100, 1234]
print(len(a))
print(a[0:-1])
print(a[:2])
print(a[:2] + ['carne', 2 * 2]) 

matrix =[ [1,2,3] , [6,5,4], [7,9,8]]
print(matrix)

#print 2 * (a[:2] + ['Boo!'])
# A  diferencia de las cadenas de texto,
# que son inmutables, es posible cambiar
# un elemento individual de una lista:
a = ['pan', 'huevos', 100, 1234]
a[2] = a[2] + 23
print(a[2])
print(a)
# reemplazar algunos
a[0:2] = [1, 12, 14]
print(a)
# borrar algunos
a[0:2] = [] # a[0:2] = list()
print(a)
# insertar algunos
a[1] = ['bruja', 'xyzzy']
print(a)
# Reemplazar algunos elementos:

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)


thelist = [5, 3, 'p', 9, 'e']
print thelist[0]
print thelist[4]
# print thelist[5] lanza una excepcion
print thelist[-1]
print thelist[-2]



# trabajando con diccionarios
emptyDict = {}
thisdict = {'a':1, 'b':23, 'c':"eggs"}
del thisdict['b']
print thisdict;


