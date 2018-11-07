# -*- coding: iso-8859-1 -*-
defaultVarForParam1 = 1;
defaultVarForParam2 = 2;
def sumatory(param1=defaultVarForParam1, param2=defaultVarForParam2):
    result = param1 + param2
    print "Resultado de la suma %d" % (result)
    return (param1, param2)

integer1 = 3;
integer2 = 4;
sumatory(integer1, integer2)
a, b = sumatory();#  (1, 2)
print a
print b
c = sumatory();
print c
sumatory(integer1)
sumatory(param2=integer1)

# Los valores por omision son evaluados
# en el momento de la definicion
# de la funcion y es sólo válido
# en el ambito de la definicion de la misma 
# (función), entonces:
i = 5

def f(number=i):
    print number

i = 6
f()

# Advertencia importante: El valor por omision 
# es evaluado solo una vez. 
# Existe una diferencia cuando el valor por
# omision es un objeto mutable como una lista,
# diccionario, o instancia de la
# mayoria de las clases. Por ejemplo,
# la siguiente función acumula 
# los argumentos que se le
# pasan en subsiguientes llamadas:

def f1(a, L=[]):
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)

# Si no se quiere que el valor por omision 
# sea compartido entre subsiguientes llamadas,
#  se pueden escribir la función así:
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1)
print f2(2)


def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print "-- ¿Tiene", tipo, "?"
    print "-- Lo siento, nos quedamos sin", tipo
    for arg in argumentos:
        print arg
    print "-"*40
    claves = palabrasclaves.keys()
    claves.sort()
    for c in claves:
        print c, ":", palabrasclaves[c]

ventadequeso("Kingurger", "Es muy liquido, sr.",
           "Realmente es muy muy liquido, sr.",
           cliente="Juan Garau",
           vendedor="Miguel Paez",
           puesto="Venta de Queso Peruano")

def loro(tension, estado='rostizado', accion='explotar'):
    print "-- Este loro no va a", accion,
    print "si le aplicas", tension, "voltios.",
    print "Esta", estado, "!"

d = {"tension": "cuatro millones", "estado": "demacrado",
     "accion": "VOLAR"}

loro(**d)
