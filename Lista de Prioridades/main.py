import min_heap

def test_min_heap():
    print("=== Testando mib (Heap manual) ===")
    pq = min_heap()

    # adicionando tarefas
    pq.insert("Tarefa A", 3)
    pq.insert("Tarefa B", 1)
    pq.insert("Tarefa C", 4)
    pq.insert("Tarefa D", 2)
    print("Lista inicial:", pq)

    # inserindo nova tarefa
    pq.insert("Tarefa E", 0)
    print("Após inserir Tarefa E (prioridade 0):", pq)

    # removendo menor prioridade
    item, prio = pq.remove_min()
    print(f"Removido: {item} (prioridade {prio})")
    print("Após remoção:", pq)

    # alterando prioridade
    pq.change_priority("Tarefa C", 0)
    print("Após alterar prioridade da Tarefa C para 0:", pq)

    # removendo todos para testar ordem
    while True:
        try:
            item, prio = pq.remove_min()
            print(f"Removido: {item} (prioridade {prio})")
        except IndexError:
            print("Fila vazia.")
            break
