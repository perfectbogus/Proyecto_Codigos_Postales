class Archivo:
	def __init__(self,nombreArchivo="CPdescarga.csv")

		self.nombreArchivo = nombreArchivo
		self.cadena = open(nombreArchivo,"r")
		self.lista = []
		
	def imprimirArchivo(self):
		for datos in self.cadena:
			print(datos)
			
	def listarEstados(self):
		temp = []
		self.lista = [datos.split(",")[4] for datos in self.cadena]
		self.lista.sort()
		for aux1 in self.lista:#Se ordena la lista
			temp.append(aux1)
			while aux1 in self.lista:
				self.lista.remove(aux1)
		self.imprimirLista(temp)		
		
	def imprimirLista(self,datos):
		i = 1
		for aux in datos:
			print(i,aux)
			i += 1
	def listarMunicipios(self):
		temp = []
		self.lista = [datos.split(",")[3:5] for datos in self.cadena]
		
		self.lista.sort()
		self.imprimirLista(self.lista)
