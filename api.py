class API(): 
	#Automata palindromo de cardinalidad par

	def __init__(self, leng, char, ventana):
		self.matriz = []
		self.lenguaje = leng
		self.caracter = char
		self.estado1 = "p"
		self.estado2 = "q"
		self.estado3 = "r"
		self.automata = ventana

	def encabezado(self):
		f = ["f:"]
		for a in self.lenguaje:
			f += [a]
		f += [self.caracter]+["_"]
		return self.matriz.append(f)



	def est1(self):
		count = count2 = -1
		tam = len(self.lenguaje)
		for a in "#"+self.lenguaje:
			colum = [self.estado1+","+a]
			for b in self.lenguaje:
				colum += [self.estado1+","+a+b]
				count += 1
				self.automata.dar_estado1(b+","+a+"/"+a+b, count, tam*(1+tam))

			colum += [self.estado2+","+a]
			count2 += 1
			self.automata.dar_estado_1_2(self.caracter+","+a+"/"+a, count2, tam)
			self.matriz.append(colum + [" "])
		return self.matriz

	def est2(self):
		count = -1
		for a in "#"+self.lenguaje:
			colum = [self.estado2+","+a]
			for b in self.lenguaje+" _":
				if a == "#" and b == "_":
					colum += [self.estado3+","+a]
					self.automata.dar_estado_2_3("_,#/#")
				elif a == b:
					colum += [self.estado2+","+""]
					count += 1
					self.automata.dar_estado2(b+","+a+"/_", count, len(self.lenguaje))
				else:
					colum += [" "]
			self.matriz.append(colum)
		return self.matriz


	def crear_matriz(self):
		#self.automata.dibujar()
		self.encabezado()
		self.est1()
		self.est2()
		#self.automata.mostrar()
		return self.matriz

	def isPalindrome(self, palabra):
		estado = self.estado1
		pila="#"
		count = j = -1
		for a in palabra+"_":
			j += 1
			i = -1
			for b in self.matriz[0]:
				i += 1
				if a == b:
					break
			for b in range((len(self.lenguaje)+1)*2+1):	
				if self.matriz[b][0] == estado+","+pila[len(pila)-1:]:
					aux = self.matriz[b][i].split(",")
					count += 1
					automata.insertar("a", count)
					print([a, pila[len(pila)-1:],aux[1]], "\t"+estado+"\t ", palabra[j:]+"\t ", pila)
					estado = aux[0]
					if a == "_" and pila == "#" and estado == self.estado3:
						return True
					elif len(aux) == 2:
						pila = pila[:-1] + aux[1]
						break
					else:
						return False