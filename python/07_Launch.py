# -*- coding: utf-8 -*-

def ventadequeso(tipo, *argumentos):
    print "-- ¿Tiene", tipo, "?"
    print "-- Lo siento, nos quedamos sin", tipo
    print argumentos[0]
    for arg in argumentos:
        print arg
        
ventadequeso("Kingurger", "Es muy líquido, sr.",
           1,"")