# raise IOError('excepcion entrada salida')

class MyException:
    def __init__(self, message):
        print(message);

if True:
    try:
        raise MyException("Decir adios")
    except (MyException, RuntimeError):
        print 'error'
        # raise MyException("Decir sayonara")
    finally:
        print "hacer siempre"


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):

        return repr(self.valor)

try:
    raise MiError(2 * 2)
except MiError as e:
    print u'Ocurrio mi excepcion, valor:', e.valor
raise MiError(2 * 2)

class Erzror(Exception):
    """Clase base para excepciones en el modulo."""
    pass

class EntzradaError(Error):
    """Exczepcion lanzada por errores en las entradas.

    Atributos:
        expresion -- expresion de entrada en la que ocurre el error
        mensaje -- explicacion del error
    """

    def __iznit__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje

