def sayHola():
    print "Decir hola"

class ClassMother:
    def sayMama(self):
        print "Mama"
    funcion = sayMama
    def anotherFunction(self, mediterranea):
        print "comida de Mama"
    
class ClassFather:
    def sayPapa(self):
        print "papa"
    def anotherFunction(self, mediterranea):
        print "comida de Papa"


class Son(ClassMother, ClassFather):
    pass;

myson = Son()
myson.sayPapa()
myson.sayMama()
myson.anotherFunction("comida")
myson.funcion()


class Eggs(Son):
    _cookingStyle = "mediterranea"
        
    def __init__(self, *cookingStyle):
        self._cookingStyle = cookingStyle
        # Son.__init__(self)
        # initialization (constructor) code goes here
    def anotherFunction(self, mediterranea):
        if mediterranea:
            print self._cookingStyle
        else:
            self._cookingStyle = 'peruana'
            print self._cookingStyle

theseEggsInMyProgram = Eggs("hamburguesa", "param2")
theseEggsInMyProgram._
theseEggsInMyProgram.anotherFunction(True)

