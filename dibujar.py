from tkinter import *
from api import API
import os
import pyttsx3
import time 

class Draw():
	def __init__(self, x=150, y=50):
		self.ventana = Tk()
		self.ventana.title("Automata De Pila Impar ")
		self.palabra = StringVar(self.ventana)
		Entry(self.ventana, textvariable=self.palabra, width=100).pack()
		Button(self.ventana, text="Ingrese La Palabra", command=self.validar).pack()
		self.list = Listbox(self.ventana)
		self.list.pack(side=LEFT, fill=BOTH, expand=1)
		self.list2 = Listbox(self.ventana)
		self.list2.pack(side=RIGHT, fill=BOTH, expand=1)
		self.w = Canvas(self.ventana, width=800, height=300,background='#D3CECE')
		self.w.pack()
		self.x = x
		self.y = y
		Label(self.ventana,text="ELABORADO POR: MICHAEL HIDALGO , BREINER PATRON",background='#D3CECE').place(x=170,y=330)
		self.w.config(scrollregion=self.w.bbox("all"))
		self.dibujar()
		self.mostrar()

	def validar(self):                               
		clear = lambda: os.system('cls')
		clear()
		self.list.delete(0, END)
		self.w.delete("all")
		self.dibujar()
		eng = pyttsx3.init()
		voices = eng.getProperty('voices')       #para reproducir la voz
		eng.setProperty('voice', voices[1].id)
		eng.setProperty('rate', 118)
		try:
			if len(self.palabra.get())%2 == 0:
				automata = APP("ab", self)
				aux = automata.crear_matriz()
				self.isPalindromePar(aux, "ab", self.palabra.get())
			else:
				automata = API("ab", "c", self)
				aux = automata.crear_matriz()
				self.isPalindromeImpar(self.palabra.get(), aux, "ab")
			self.list.insert(END, "Palabra Aceptada")
			eng.say("palabra aceptada")
			eng.runAndWait()
		except:
			self.list.insert(END, "Palabra No Aceptada")
			print(False)
			eng.say("palabra no aceptada")
			eng.runAndWait()

	def insertar(self, palabra):
		self.list.insert(END, pal)

	def isPalindromeImpar(self, palabra, matriz, lenguaje):   #palindromeimpar
		estado = "p"
		pila="#"
		count = j = -1
		for a in palabra+"_":
			j += 1
			i = -1
			for b in matriz[0]:
				i += 1
				if a == b:
					break

			for b in range((len(lenguaje)+1)*2+1):	
				if matriz[b][0] == estado+","+pila[len(pila)-1:]:
					aux = matriz[b][i].split(",")
					count += 1
					pal = "["+a+","+ pila[len(pila)-1:]+"/"+aux[1]+"]"
					self.list.insert(END, pal)
					self.list2.delete(0, END)
					self.list2.insert(END, pila)
					time.sleep(3)
					self.w.update()
					print([a, pila[len(pila)-1:],aux[1]], "\t"+estado+"\t ", palabra[j:]+"\t ", pila)
					estado = aux[0]
					if a == "_" and pila == "#" and estado == "R":
						return True
					elif len(aux) == 2:
						pila = pila[:-1] + aux[1]
						break
					else:
						return False

	def dibujar(self, estados=["P1", "Q2", "R"]):    #dibujando el automata
{ñpoi43 
		count = 0
		x = self.x
		y = self.y
		self.w.create_line(x-50,y+50,x,y+50, fill='#211717')
		points = [x-10,y+40,x,y+50, x-10, y+60]
		self.w.create_polygon(points, width=3, fill='#484c7f')
		for i in range(5):
			if i%2 != 0:
				self.w.create_line(x,y+50,100+x,y+50, fill='#211717')
				points = [x+90,y+40,x+100,y+50, x+90, y+60]
				self.w.create_polygon(points, width=3,fill='#484c7f')
			else:
				self.w.create_oval(x,y,x+100,y+100, width=2, fill='#ac8daf')
				self.w.create_text(x+50, y+50, text=estados[count])
				count += 1
				if i == 4:
				        self.w.create_oval(x+6,y+6,x+100-6,y+100-6, width=2)
				else:
					xy = x-50, y+50, x+50, y+150
					self.w.create_arc(xy, start = 90, extent = 270, style=ARC )
					points = [x+40,y+110,x+50,y+100, x+60, y+110]
					self.w.create_polygon(points, width=3, fill='#484c7f')
			x += 100
			
	def dar_estado1(self, transicion, pos, tam):         #transciicones de los tres estados
		xy = self.x-25, pos*10+self.y+160
		if tam > 6:
			if pos < 3:
				self.w.create_text(xy, text=transicion,fill='black')
			elif pos <6:
				self.w.create_text(xy, text=".",fill='black')
			if pos + 1 == tam:
				xy = self.x-25, 60+self.y+160
				self.w.create_text(xy, text=transicion,fill='black')
		else:
			self.w.create_text(xy, text=transicion,fill='black')


	def dar_estado_1_2(self, transicion, pos, tam):
		xy = self.x+130, self.y-pos*10+40
		if tam > 5:
			if pos < 3:
				self.w.create_text(xy, text=transicion,fill='black')	
			elif pos <6:
				self.w.create_text(xy, text=".",fill='black')
			elif pos == tam:
				xy = self.x+130, self.y-60+40
				self.w.create_text(xy, text=transicion,fill='black')
		else:	
			self.w.create_text(xy, text=transicion,fill='black')

	def dar_estado2(self, transicion, pos, tam):
		xy = self.x-25+200, pos*10+self.y+160
		if tam > 5:
			if pos < 3:
				self.w.create_text(xy, text=transicion,fill='black')	
			elif pos <6:
				self.w.create_text(xy, text=".",fill='black')
			if pos + 1 == tam:
				xy = self.x-25+200, 60+self.y+160
				self.w.create_text(xy, text=transicion,fill='black')
		else:	
			self.w.create_text(xy, text=transicion,fill='black')

	def dar_estado_2_3(self, transicion, pos=0):
		xy = self.x+330, self.y-pos*10+40
		self.w.create_text(xy, text=transicion,fill='black')	

	def mostrar(self):
		mainloop()
