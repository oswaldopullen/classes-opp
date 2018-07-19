	
class Registro:
	lista_montada = []
	arquivo = ''
	def __init__(self, arquivo, arquivo_ordenado, pos_chave_inicial, pos_chave_final):
		self.pos_chave_inicial = pos_chave_inicial
		self.pos_chave_final = pos_chave_final
		self.lista = []
		self.arquivo = arquivo
		self.arquivo_ordenado = arquivo_ordenado
		self.fp = open(self.arquivo, 'r')
		
	def __del__(self):
		self.fp.close()
		self.fp = open(self.arquivo_ordenado, 'w')
		self.fp.writelines(self.lista_montada)
		self.fp.close()
		
	def leitura_arq(self):
		self.lista = self.fp.readlines()
		
	def sort(self, posinit=0, posfim=3):
		
		for i in range (len(self.lista)):
			self.lista_montada.append(self.monta_chave(self.lista[i],self.pos_chave_inicial,self.pos_chave_final))
		for i in range (len(self.lista_montada)):
			min = i
			for j in range (i + 1, len(self.lista)):
				if self.lista_montada[j][0] < self.lista_montada[min][0]:
					self.lista_montada[min], self.lista_montada[j] = self.lista_montada[j], self.lista_montada[min]
			if self.lista_montada[j][0] != self.lista_montada[min][0]:
				self.lista_montada[i], self.lista_montada[min]= self.lista_montada[min], self.lista_montada[i]
		return self.reune_lista(self.lista_montada)	
		

	def monta_chave(self,item, pos_chave_inicial, pos_chave_final):
		lista_trab=[]
		chave = int(item[pos_chave_inicial:pos_chave_final+1])
		lista_trab.append(chave)
		lista_trab.append(item[4:])
		return lista_trab
		
	def reune_lista(self,lista):
		str_trab = ''
		for i in range (0,len(lista)):
			elemento =lista[i][0]
			str_trab2 = str(elemento)
			j = len(str_trab2)
			while j<4:
				str_trab2 = '0' + str_trab2
				j+=1
			lista[i][0] = str_trab2
			str_trab= ''.join(lista[i])
			lista[i] = str_trab
		
		return lista
	
	def printa_resultado(self, lista, quantos):
		for i in range (0,quantos):
			print(lista[i])
	
	
reg = Registro('resultados.txt', 'ordenados.txt',0,4)
reg.leitura_arq()
lista_montada = reg.sort() 

#reg.printa_resultado(lista_montada,2)
del reg

