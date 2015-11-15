class ClassMother:
    pass
class ClassFather:
    pass


class Son(ClassMother, ClassFather):
    pass;

myson = Son()

class Eggs(Son):
    cookingStyle = "mediterranea"
        
    def __init__(self, *cookingStyle):
        self.cookingStyle = cookingStyle
        # Son.__init__(self)
        # initialization (constructor) code goes here
    def anotherFunction(self, mediterranea):
        if mediterranea:
            print self.cookingStyle
        else:
            self.cookingStyle = 'peruana'
            print self.cookingStyle

theseEggsInMyProgram = Eggs()
theseEggsInMyProgram.anotherFunction(True)
