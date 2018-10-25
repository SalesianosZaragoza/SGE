# -*- coding: iso-8859-1 -*-

def ventadequeso(tipo, *argumentos):
    print "-- ¿Tiene", tipo, "?"
    print "-- Lo siento, nos quedamos sin", tipo
    print argumentos[0]
    for arg in argumentos:
        print arg
        
ventadequeso("Kingurger", "Es muy liquido, sr.",
           1,"")