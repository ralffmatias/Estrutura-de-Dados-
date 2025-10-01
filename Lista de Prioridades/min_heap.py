class min_heap:
    def __init__(self):
        self.heap = []  # lista de tuplas (prioridade, item)

    # funções auxiliares para navegar no heap
    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, i):
        """Move o item para cima enquanto for menor que o pai."""
        while i > 0 and self.heap[i][0] < self.heap[self.parent(i)][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def sift_down(self, i):
        """Move o item para baixo para restaurar a propriedade do heap."""
        n = len(self.heap)
        while True:
            left, right = self.left(i), self.right(i)
            smallest = i

            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break
            self.swap(i, smallest)
            i = smallest

    def insert(self, item, priority):
        """Insere um item com prioridade."""
        self.heap.append((priority, item))
        self.sift_up(len(self.heap) - 1)

    def remove_min(self):
        """Remove e retorna o item com menor prioridade."""
        if not self.heap:
            raise IndexError("Heap vazio.")
        self.swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        if self.heap:
            self.sift_down(0)
        return item, priority

    def change_priority(self, item, new_priority):
        """Altera a prioridade de um item existente."""
        for i, (priority, it) in enumerate(self.heap):
            if it == item:
                self.heap[i] = (new_priority, it)
                # decide se sobe ou desce
                self.sift_up(i)
                self.sift_down(i)
                return
        raise ValueError(f"Item '{item}' não encontrado.")

    def __str__(self):
        return str(sorted(self.heap))
