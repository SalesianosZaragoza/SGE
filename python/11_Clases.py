def sayHola():
    print("Decir hola")


def sayAdios(funcion):
    funcion()
    print("Decir adios")


decirhola = sayHola
decirHolaYAdios = sayAdios
decirHolaYAdios(decirhola)
class Abuelo:
    def sayName(self):
        print("soy el abuelo")
    pass
class Abuela:
    pass


class ClassMother(Abuela,Abuelo):
    def sayMama(self):
        print("Mama")
    funcion = sayMama


class ClassFather(Abuelo):
    def sayPapa(self):
        print("papa")

    def anotherFunction(self, mediterranea):
        print("comida de papa")

    def sayName(self):
        print("soy papa")


class Son(ClassMother, ClassFather):
    def __init__(self):
        pass


myson = Son()
myson.sayName()
myson.sayPapa()
myson.sayMama()
myson.anotherFunction("comida")
myson.funcion()


class Eggs(Son):
    _cookingStyle = "mediterranea"

    def __init__(self, *cookingStyle):
        self._cookingStyle = cookingStyle
        Son.__init__(self)
        # initialization (constructor) code goes here

    def anotherFunction(self, mediterranea):
        if mediterranea:
            print(self._cookingStyle)
        else:
            self._cookingStyle = 'peruana'
            print(self._cookingStyle)


theseEggsInMyProgram = Eggs("hamburguesa", "param2")
theseEggsInMyProgram.anotherFunction(True)
