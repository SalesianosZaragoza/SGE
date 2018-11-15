import math
l = [1, 2, 3, 4]

def cuadrado(n):    return n ** 2
l2 = map(cuadrado, l)
   

def raiz(n):    return math.sqrt(n)
l2 = map(raiz, l)

def es_par(n):    
    return (n % 2.0 == 0)
l2 = filter(es_par, l)

def sumar(x, y):    
    sum = x + y
    return sum    
    
l2 = reduce(sumar, map(cuadrado, l))
print(l2)
l2 = reduce(sumar, map(raiz, l))
def sumAndPow2(l):
    sum = 0
    for i in range(l):
        sum = i ** 2 + sum

def sumAndSquare(l):
    sum = 0
    for i in range(l):
        sum = math.sqrt(i) + sum       

filter(lambda n: n % 2.0 == 0, l)

l2 = [x for x in l if x % 2.0 == 0]
print l2

def saludar(lang):    
    def saludar_es():
        print "Hola"
    def saludar_en():        
        print "Hi"
    def saludar_fr():        
        print "Salut"
    lang_func = {"es": saludar_es, "en": saludar_en, "fr": saludar_fr}    
    return lang_func[lang]
f = saludar("es") 
f()



def mi_decorador(funcion):    
    def nueva(*args):        
        print "Llamada a la funcion", funcion.__name__        
        retorno = funcion(*args)        
        return retorno    
    return nueva


def imp(arg):
    print arg

mi_decorador(imp)("hola")
