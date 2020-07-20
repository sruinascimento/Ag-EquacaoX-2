from individuo6 import Individuo 
from numpy import array
from random import sample, randint, random
import matplotlib.pyplot as plt

class Ambiente:
	def __init__(self):
		self.tamanho_populacao = 10
		self.calc_fitness = (lambda xy: sum(xy**2))
		self.melhor_individuo = None
		self.taxa_crossing_over = 0.9
		self.taxa_mutacao = 0.02
		self.geracao_parada = 1000

		#self.fitness_all = []

	def start(self):
		populacao = self.geraPopulacaoInicial()
		self.avalia(populacao)
		for _ in range(self.geracao_parada):
		#while self.geracao_parada > 0 or self.melhor_individuo.fitness != 0:
			populacao = self.reproduz(populacao)
			self.avalia(populacao)
			#self.geracao_parada -= 1
			#self.fitness_all.append(self.melhor_individuo.fitness)

		#plt.plot(range(100), self.fitness_all)
		#plt.title('AG e**2')
		#plt.show()
		return self.melhor_individuo

	def geraPopulacaoInicial(self):
		populacao_temp = [Individuo() for _ in range(self.tamanho_populacao)]
		self.melhor_individuo = populacao_temp[0]
		return populacao_temp

	def avalia(self, populacao:list) -> None:
		for individuo in populacao:
			xy = array(individuo.cromossomo)
			individuo.fitness = self.calc_fitness(xy)
			self.melhorIndividuo(individuo)

	def melhorIndividuo(self, individuo:Individuo) -> None:
		if self.melhor_individuo.fitness > individuo.fitness:
			self.melhor_individuo = individuo.copia()
			return

	def seleciona(self, populacao:list) -> list:
		quantidade = int(self.taxa_crossing_over * self.tamanho_populacao)
		piscina = []
		for _ in range(quantidade):
			selecionados = sample(populacao, 3)
			selecionados.sort(key=lambda individuo: individuo.fitness)
			piscina.append(selecionados[0])
		return piscina

	def cruza(self, selecionados:list) -> list:
		quantidade = int(self.tamanho_populacao * self.taxa_crossing_over)
		novos_individuos = []
		for _ in range(quantidade):
			indv1, indv2 = sample(selecionados, 2)
			filho1, filho2 = self.umPonto(indv1, indv2)
			novos_individuos.extend((filho1, filho2)) 
		return novos_individuos

	def umPonto(self, indv1, indv2):
		ponto_corte = randint(0, Individuo().tamanho)
		filho1 = indv1.cromossomo[:ponto_corte] + indv2.cromossomo[ponto_corte:]
		filho2 = indv2.cromossomo[:ponto_corte] + indv2.cromossomo[ponto_corte:]
		return (Individuo(filho1), Individuo(filho2))

	def muta(self, populacao:list) -> None:
		for individuo in populacao:
			if random() < self.taxa_mutacao:
				self.permuta(individuo)


	def permuta(self, individuo:Individuo) -> None:
		a = individuo.cromossomo
		p1, p2 = sample(range(Individuo().tamanho), 2)
		a[p1], a[p2] = a[p2], a[p1]

	def reproduz(self, populacao:list) -> list:
		populacao.sort(key=lambda individuo: individuo.fitness, reverse=True)
		quantidade = int(self.tamanho_populacao * self.taxa_crossing_over)
		selecionados = self.seleciona(populacao)
		populacao_temp = self.cruza(selecionados)
		nova_populacao = populacao_temp + populacao[quantidade:]
		self.muta(nova_populacao)
		return nova_populacao


if __name__ == '__main__':
	pass