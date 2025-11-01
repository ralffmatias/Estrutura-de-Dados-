import random
import datetime
import time
import datetime
import matplotlib.pyplot as plt

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



# -------------------------------
# Classe de Ordenação
# -------------------------------
class Ordenacao:

    @staticmethod
    def bubble_sort(arr, key=lambda x: x, reverse=False):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (key(arr[j]) > key(arr[j+1]) and not reverse) or (key(arr[j]) < key(arr[j+1]) and reverse):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def quick_sort(arr, key=lambda x: x, reverse=False):
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr)//2])
        left = [x for x in arr if (key(x) < pivot and not reverse) or (key(x) > pivot and reverse)]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if (key(x) > pivot and not reverse) or (key(x) < pivot and reverse)]
        return Ordenacao.quick_sort(left, key, reverse) + middle + Ordenacao.quick_sort(right, key, reverse)

    @staticmethod
    def merge_sort(arr, key=lambda x: x, reverse=False):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = Ordenacao.merge_sort(arr[:mid], key, reverse)
        right = Ordenacao.merge_sort(arr[mid:], key, reverse)

        return Ordenacao._merge(left, right, key, reverse)

    @staticmethod
    def _merge(left, right, key, reverse):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (key(left[i]) <= key(right[j]) and not reverse) or (key(left[i]) >= key(right[j]) and reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    @staticmethod
    def _heapify(arr, n, i, key, reverse):
        """Mantém a propriedade do heap para o nó i."""
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and ((key(arr[l]) > key(arr[largest]) and not reverse) or
                      (key(arr[l]) < key(arr[largest]) and reverse)):
            largest = l
        if r < n and ((key(arr[r]) > key(arr[largest]) and not reverse) or
                      (key(arr[r]) < key(arr[largest]) and reverse)):
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Ordenacao._heapify(arr, n, largest, key, reverse)

    @staticmethod
    def heap_sort(arr, key=lambda x: x, reverse=False):
        """Ordena usando Heap Sort."""
        arr = arr.copy()
        n = len(arr)

        # Construção do Max-Heap / Min-Heap
        for i in range(n // 2 - 1, -1, -1):
            Ordenacao._heapify(arr, n, i, key, reverse)

        # Extração de elementos do heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            Ordenacao._heapify(arr, i, 0, key, reverse)

        return arr

# main.py

# ------------------------------
# 1. Geração de dados
# ------------------------------
N = 1000
produtos = Produto.gerar_produtos(N)

# ------------------------------
# 2. Critérios de ordenação
# ------------------------------
criterios = {
    "Preço ↑": (lambda p: p.preco, False),
    "Preço ↓": (lambda p: p.preco, True),
    "Avaliação ↑": (lambda p: p.avaliacao, False),
    "Avaliação ↓": (lambda p: p.avaliacao, True),
    "Data (Recente)": (lambda p: p.data_adicao, True),
    "Data (Antiga)": (lambda p: p.data_adicao, False),
    "Categoria": (lambda p: p.categoria, False)
}

# ------------------------------
# 3. Algoritmos
# ------------------------------
algoritmos = {
    "Bubble Sort": Ordenacao.bubble_sort,
    "Quick Sort": Ordenacao.quick_sort,
    "Merge Sort": Ordenacao.merge_sort,
    "Heap Sort": Ordenacao.heap_sort
}

# ------------------------------
# 4. Funções auxiliares
# ------------------------------
def medir_tempo(algoritmo, lista, key, reverse):
    inicio = time.time()
    resultado = algoritmo(lista, key=key, reverse=reverse)
    fim = time.time()
    return resultado, fim - inicio

def is_sorted(lst, key, reverse=False):
    for a, b in zip(lst, lst[1:]):
        if not reverse and key(a) > key(b):
            return False
        if reverse and key(a) < key(b):
            return False
    return True

# ------------------------------
# 5. Execução + coleta dos tempos
# ------------------------------
resultados = {alg_nome: {} for alg_nome in algoritmos.keys()}

print("\n=== Comparação de desempenho ===\n")

for crit_nome, (key, reverse) in criterios.items():
    print(f"\n--- Critério: {crit_nome} ---")
    for alg_nome, alg_func in algoritmos.items():
        ordenado, tempo = medir_tempo(alg_func, produtos, key, reverse)

        if not is_sorted(ordenado, key, reverse):
            print(f"[ERRO] {alg_nome} falhou em {crit_nome}")
        else:
            print(f"{alg_nome:12} -> {tempo:.6f}s")
            resultados[alg_nome][crit_nome] = tempo

# ------------------------------
# 6. Gráfico agrupado
# ------------------------------
import numpy as np

criterios_lista = list(criterios.keys())
algoritmos_lista = list(algoritmos.keys())

x = np.arange(len(algoritmos_lista))  # posições dos algoritmos no eixo X
largura = 0.12  # largura das barras
fig, ax = plt.subplots(figsize=(12, 6))

for i, crit_nome in enumerate(criterios_lista):
    tempos = [resultados[alg][crit_nome] for alg in algoritmos_lista]
    ax.bar(x + i*largura, tempos, largura, label=crit_nome)

ax.set_xlabel("Algoritmos")
ax.set_ylabel("Tempo (s)")
ax.set_title("Desempenho de algoritmos em diferentes critérios")
ax.set_xticks(x + largura*(len(criterios_lista)/2))
ax.set_xticklabels(algoritmos_lista)
ax.legend()
plt.tight_layout()
plt.show()

