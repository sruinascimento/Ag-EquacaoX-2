from random import uniform


class Individuo:
	def __init__(self, cromossomo=None):
		self.tamanho = 5
		self.cromossomo = self.geraCromossomoALeatorio() if not cromossomo else cromossomo
		self.fitness = None

	def geraCromossomoALeatorio(self):
		self.cromossomo = [uniform(-5.12, 5.12) for _ in range(self.tamanho)]
		return self.cromossomo

	def copia(self):
		indv_temp = Individuo(self.cromossomo)
		indv_temp.fitness = self.fitness
		return indv_temp

	def __repr__(self):
		return f'Cromossomo: {self.cromossomo}\nFitness: {self.fitness}'
