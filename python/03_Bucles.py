# mi primer if

variable = 0
print variable

if variable == 0:
    print "soy un cero"
elif variable == 1:
    print "soy un uno"
else :
    print "no se sabe lo que soy"

a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print i, a[i]

indice = 30
step = 10

for i in range(indice, 100, step):
    print i

a = ['bruja','pikachu', 'xyzzy']
for i in a[0:2]:
    print i,


tuplasSi = ('s', 'S', 'si', 'Si', 'SI')
tuplasNo = ('n', 'no', 'No', 'NO')
tuplasPuede = ('puede', 'posiblemente', 'quizas')
ok = 'no';
if (ok in tuplasSi or ok in tuplasPuede):
    print "Aqui no se encuentra"
if ok in tuplasNo:
    print "Aqui se ha encontrado"

#while True:
#   pass
