from functools import partial

def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x

g = partial(f, 3, 1, 4)

print g(5)

def conexion(urljdbc, dabasename, user, password):
    print urljdbc, dabasename, user, password

mysql= partial(conexion,"jdbc:mysql:3306", "mydabase")
mysql("sa","mypassword")