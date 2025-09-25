import random
import datetime
import time

class Produto:      

	def __init__(self, nome, preco, avaliacao, data_adicao, categoria):
		self.nome = nome
		self.preco = preco
		self.avaliacao = avaliacao
		self.data_adicao = data_adicao
		self.categoria = categoria  
		
		
	def __repr__(self):
		return f"{self.nome}: {self.preco}, {self.avaliacao}, {self.data_adicao}, {self.categoria}"
		
	
	@staticmethod
	def gerar_produtos(n): 
		nomes = ["Produto" + str(i) for i in range(n)]
		precos = [round(random.uniform(10, 1000), 2) for _ in range(n)] 
		avaliacoes = [round(random.uniform(0, 5), 2) for _ in range(n)] 
		datas = [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)) for _ in range(n)] 
		categorias = ["Categoria" + str(random.randint(1, 5)) for _ in range(n)]  
		produtos = [Produto(nomes[i], precos[i], avaliacoes[i], datas[i], categorias[i]) for i in range(n)]
		
		return produtos
		