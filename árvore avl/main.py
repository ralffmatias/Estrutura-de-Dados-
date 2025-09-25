from avl_node import *

# Criando a árvore
tree = AVLNode(None)  

root = None
for num in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, num)

print("In-order:", tree.inorder(root))   # [10, 20, 25, 30, 40, 50]
print("Pré-order:", tree.preorder(root)) # [30, 20, 10, 25, 40, 50]

# Busca
print("Busca 25:", tree.search(root, 25) is not None)

# Deletando
root = tree.delete(root, 40)
print("In-order após deletar 40:", tree.inorder(root))

