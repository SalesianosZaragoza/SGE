frutafresca = ['  banana', '  mora de Logan ', 'maracuya  ']
print [arma.strip() for arma in frutafresca]
vec = [2, 4, 6]
print [3*x for x in vec]
print [3*x for x in vec if x > 3]
print [3*x for x in vec if x < 2]

print [[x,x**2] for x in vec]
# print [x, x**2 for x in vec]   # error - se requieren parentesis para tuplas
print [(x, x**2) for x in vec]
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print [x*y for x in vec1 for y in vec2]
print [x+y for x in vec1 for y in vec2]
print [vec1[i]*vec2[i] for i in range(len(vec1))]


mat = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
      ]

# print [[fila[i] for fila in mat] for i in [0, 1, 2]]

for i in [0, 1, 2]:
    for fila in mat:
        print fila[i],
    print
