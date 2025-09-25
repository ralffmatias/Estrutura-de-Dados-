# main.py
import time
import matplotlib.pyplot as plt
from produtos import Produto
from sort import Ordenacao

# ------------------------------
# 1. Geração de dados
# ------------------------------
N = 100000
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