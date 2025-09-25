import heapq

class Graph:
    def __init__(self):
        # Representação: {nó: [(vizinho, peso), ...]}
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        # Adiciona aresta de u -> v (direcionado)
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        
        
    def dijkstra(self, start):
        # Inicialização
        distances = {node: float("inf") for node in self.adj_list}
        distances[start] = 0
        predecessors = {node: None for node in self.adj_list}

        # Fila de prioridade (distância acumulada, nó)
        pq = [(0, start)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            # Ignora se já encontrou caminho menor antes
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.adj_list[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, predecessors


    def shortest_path(self, start, end):
        distances, predecessors = self.dijkstra(start)

        if distances[end] == float("inf"):
            return None, float("inf")  # sem caminho

        # Reconstruir caminho
        path = []
        node = end
        while node is not None:
            path.insert(0, node)
            node = predecessors[node]

        return path, distances[end]


def test_graph():
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)

    # Teste 1: caminho normal
    path, dist = g.shortest_path("A", "D")
    print("Caminho A → D:", path, "| Distância:", dist)

    # Teste 2: nó desconectado
    g.add_edge("E", "F", 1)
    path, dist = g.shortest_path("A", "F")
    print("Caminho A → F:", path, "| Distância:", dist)
    
    
    
if __name__ == "__main__":
    test_graph()


