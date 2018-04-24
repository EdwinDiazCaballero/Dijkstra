class nodo:
	pe = -1
	ant = ""
	def __init__(self, inicial, vecinos, aristas):
		self.ini = inicial
		self.vec = vecinos
		self.ari = aristas

def getLista(dic):
	listaFinal = [[]]
	nodos = list(dic.keys())
	tamOrig = len(nodos) - 1
	recor = []
	while len(recor) < tamOrig:
		lista1 = []
		if len(nodos) > 1:
			mayor = dic[nodos[0]].pe
			actual = nodos[0]
			for el in nodos:
				if dic[el].pe > mayor:
					mayor = dic[el].pe
					actual = el
			if actual not in recor:
				while not dic[actual].ini:
					lista1.append(actual)
					if actual not in recor:
						recor.append(actual)
					if actual in nodos:
						nodos.remove(actual)
					try:
						actual = int(dic[actual].ant)
					except:
						actual = dic[actual].ant
				lista1.append(actual)
				lista1.reverse()
				listaFinal.append()
	return listaFinal

def dijkstra(dic):
	i = 0
	no_visit = list(dic.keys())
	for asig in no_visit:
		if dic[asig].ini:
			dic[asig].pe = 0
			actual = asig
		else:
			dic[asig].pe = 2147483647
	while len(no_visit) > 0:
		print('actual')
		print(actual)
		print('no visitados')
		print(no_visit)
		for va in dic[actual].vec:
			print('Vecino actual:')
			print(va)
			new_pe=dic[actual].pe + dic[actual].ari[i]
			if dic[va].pe > new_pe:
				dic[va].pe = new_pe
				dic[va].ant = str(actual)
				print('peso nuevo:')
				print(dic[va].pe)
				print('nodo anterior:')
				print(dic[va].ant)
			else:
				print('¡Peso no actualizado!')
				print('¡Nodo anterior no actualizado!')
			i = i + 1
		i = 0
		no_visit.remove(actual)
		print('no visitados (despues de eliminacion de actual)')
		print(no_visit)
		if len(no_visit) > 0:
			menor = dic[no_visit[0]].pe
			actual = no_visit[0]
			for ree in no_visit:
				if dic[ree].pe < menor:
					menor = dic[ree].pe
					actual = ree
	return getLista(dic)

def tdd(f, grafo, arbol):
	return f(grafo)

print('++++++++++tdd++++++++++')

n1 = nodo(True, ['b','c'],[1,3])
n2 = nodo(False, ['a','c','d'], [1,5,2])
n3 = nodo(False, ['a','b','d'], [3,5,2])
n4 = nodo(False, ['b','c'], [2,2])

print(tdd(dijkstra, {'a':n1, 'b':n2, 'c':n3, 'd':n4}))

print('++++++++++tdd2++++++++++')

a1 = nodo(True, [6,3,2], [14,9,7])
a2 = nodo(False, [1,3,5], [14,2,9])
a3 = nodo(False, [1,6,4,2], [9,2,11,10])
a4 = nodo(False, [1,3,4], [7,10,15])
a5 = nodo(False, [2,3,5], [15,11,6])
a6 = nodo(False, [6,4], [9,6])

print(tdd(dijkstra, {1:a1, 6:a2, 3:a3, 2:a4, 4:a5, 5:a6}))
