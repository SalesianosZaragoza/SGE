import random

class Juego:
	def __init__(self, jugador1, jugador2):
		self.jugador1 = jugador1
		self.jugador2 = jugador2

	def turno(self):
		self.jugador1.pegar(self.jugador2)
		self.jugador2.pegar(self.jugador1)



class Jugador:
	def __init_(self, vida, ataque, damage, precision):
		self._vida = vida
		self._ataque = ataque
		self._damage = damage
		self._precision = precision

	def pegar(self, rival):
		if random.random() <= self._precision:
			rival.herir(self._damage)

	def herir(self, damage):
		self._vida -= damage

	

class Personaje(Jugador):
	def __init__(self, nombre, vida, ataque, damage, precision):
		#super.__init__(self, vida, ataque, damage, precision)
		self._vida = vida
		self._ataque = ataque
		self._damage = damage
		self._precision = precision
		self.nombre = nombre



__newpj = Personaje("Pedro", 10, "patada", 5, 0.9)

print(__newpj._vida)