emptyTuple = ()
print emptyTuple
singleItemTuple = ("spam",)  # fijarse en la coma
print singleItemTuple
mytuple = 12, 89, 'a'
mytuple = (12, 89, 'a')
mytuple = mytuple + mytuple 
print mytuple
print mytuple * 5


# trabajando con listas
a = ['pan', 'huevos', 100, 1234]
print len (a)
print a[1:-1]
print a[:2] + ['carne', 2 * 2]
print 3 * a[:3] + ['Boo!']
# A  diferencia de las cadenas de texto, que son inmutables, es posible cambiar un elemento individual de una lista:
a = ['pan', 'huevos', 100, 1234]
a[2] = a[2] + 23
# reemplazar algunos
a[0:2] = [1, 12]
# borrar algunos
a[0:2] = []
# insertar algunos
a[1:1] = ['bruja', 'xyzzy']
print a
# Reemplazar algunos elementos:

a = [-1, 1, 66.25, 333, 333, 1234.5]
print a
del a[0]
print a
